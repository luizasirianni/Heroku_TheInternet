'''configurar o pytest para trabalhar remotamente em
ambientes distribuídos (saucelabs)'''
import os

import outcome
import pytest
from selenium import webdriver

from tests import config


def pytest_addoption(parser):
    parser.addoption(
        '--baseurl',
        action='store',
        default='https://the-internet.herokuapp.com',
        help='Url base da aplicacao alvo do teste'
    )
    parser.addoption(
        '--host',
        action='store',
        default='saucelabs',
        help='Onde vamos executar nossos testes: localhost ou saucelabs'
    )
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='O nome do navegador utilizado nos testes'
    )
    parser.addoption(
        '--browserversion',
        action='store',
        default='112.0',
        help='Versao do browser'
    )
    parser.addoption(
        '--platform',
        action='store',
        default='Windows 10',
        help='Sistema Operacional a ser utilizado durante os testes'
    )
@pytest.fixture
def driver(request):
    '''Inicialização dos testes - similar ao Before/Setup'''
    config.baseurl = request.config.getoption('--baseurl')
    config.host = request.config.getoption('--host')
    config.browser = request.config.getoption('--browser')
    config.browserversion = request.config.getoption('--browserversion')
    config.platform = request.config.getoption('--platform')

    if config.host == 'saucelabs':
        test_name = request.node.name # nome do teste
        capabilities = {
            'browserName': config.browser,
            'browserVersion': config.browserversion,
            'platformName': config.platform,
            'sauce:options': {
                'name': test_name
            }
        }
        #_credentials = os.environ['oauth-lu.sirianni-118c4'] + ':' + os.environ['c335ffe6-7788-43a7-9f9d-a062b6f03c61']
        #_url = 'https://' + _credentials + '@ondemand.eu-central-1.saucelabs.com:443/wd/hub'
        _url = 'https://oauth-lu.sirianni-118c4:c335ffe6-7788-43a7-9f9d-a062b6f03c61@ondemand.eu-central-1.saucelabs.com:443/wd/hub'
        driver_ = webdriver.Remote(_url, capabilities)
    else: #execuçao local / localhost
        if config.host == 'chrome':
            _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')
            if os.path.isfile(_chromedriver):
                driver_ = webdriver.Chrome(_chromedriver) #primeiro vai tentar utilizar o chromedriver local do projeto
            else:
                driver_ = webdriver.Chrome() #se não tiver um chromedriver local, vai utilizar o das variaveis do ambiente do servidor
        elif config.browser == 'firefox':
            _geckodriver = os.path.join(os.getcwd(), 'vendor', 'geckodriver.exe')
            if os.path.isfile(_geckodriver):
                driver_ = webdriver.Firefox(_geckodriver)
            else:
                driver_ = webdriver.Firefox()

    def quit():
        '''Finalização dos testes - similar ao After ou TearDown'''
        #sinalização se passou ou falhou conforme o retorno da requisição
        sauce_result = 'failed' if request.node.rep_call.failed else 'passed'

        driver_.execute_script('sauce:job-result={}'.format(sauce_result)) #traz o resultado do teste formatado conforme o if acima
        driver_.quit()

    request.addfinalizer(quit) #ao finalizar, chama a função quit
    return driver_

@pytest.hookimpl(hookwrapper=True, tryfirst=True) #implementação de gatilho de comunicação com o saucelabs
def pytest_runtest_makereport(item, call):
    '''parâmetros para geração do relatório'''
    outcome = yield
    rep = outcome.get_result()

    '''definir atributos para o relatório'''
    setattr(item, 'rep_' + rep.when, rep)
