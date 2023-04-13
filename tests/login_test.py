import os
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture  # definição pra termos uma função baseada nele, como se fosse um padrão
# vai entender q eh uma configuracao pro pytest. Vai sempre executar antes do teste

def login(request):
    _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')  # criou um objeto.
    # O underline no inicio significa q esse objeto é privado
    print('CWD ===========>>>> ' + os.getcwd())

    if os.path.isfile(_chromedriver):
        # se existe um chromedriver.exe no projeto, instancie com ele
        driver_ = webdriver.Chrome(_chromedriver)
    else:
        # caso não exista um chromedriver.exe no projeto
        driver_ = webdriver.Chrome()

    def quit():
        driver_.quit()

    # sinalizando o fim da execução para o ambiente
    request.addfinalizer(quit)
    return driver_

'''########### MODO ANTIGO DE FAZER ##############
def test_login_valido(driver):
    driver.get('https://the-internet.herokuapp.com/login')
    driver.find_element(By.ID, 'username').send_keys('tomsmith')
    driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, '#login > button').click()
    assert driver.find_element(By.CSS_SELECTOR, 'div.flash.success').is_displayed()
    print('Login com sucesso')
'''


def test_login_successful(self, login):
    # preenche o usuario e a senha e clica no botao
    login.with_('tomsmith', 'SuperSecretPassword!')
    # validar a msg
    assert login.success_message()


def test_invalid_username(self, login):
    # preenche o usuario e a senha e clica no botao
    login.with_('aaaaaaa', 'SuperSecretPassword!')
    # validar a msg
    assert login.failure_message()


def test_invalid_password(self, login):
    # preenche o usuario e a senha e clica no botao
    login.with_('tomsmith', 'asdkskskad')
    # validar a msg
    assert login.failure_message()