import os
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture  # definição pra termos uma função baseada nele, como se fosse um padrão
# vai entender q eh uma configuracao pro pytest. Vai sempre executar antes do teste

def driver(request):
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


def test_login_valido(driver):
    driver.get('https://the-internet.herokuapp.com/login')
    driver.find_element(By.ID, 'username').send_keys('tomsmith')
    driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, '#login > button').click()
    assert driver.find_element(By.CSS_SELECTOR, 'div.flash.success').is_displayed()
    print('Login com sucesso')
