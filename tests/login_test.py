
import pytest
from tests.conftest import driver
from pages import login_page

@pytest.fixture  # definição pra termos uma função baseada nele, como se fosse um padrão
# vai entender q é uma configuracao pro pytest. Vai sempre executar antes do teste

def login(driver):
    return login_page.LoginPage(driver) # instanciando a classe LoginPage e passando o Selenium


'''########### MODO ANTIGO DE FAZER ##############
def test_login_valido(driver):
    driver.get('https://the-internet.herokuapp.com/login')
    driver.find_element(By.ID, 'username').send_keys('tomsmith')
    driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, '#login > button').click()
    assert driver.find_element(By.CSS_SELECTOR, 'div.flash.success').is_displayed()
    print('Login com sucesso')
'''


def test_login_successful(login):
    # preenche o usuario e a senha e clica no botao
    login.with_('tomsmith', 'SuperSecretPassword!')
    # validar a msg
    assert login.success_message()


def test_invalid_username(login):
    # preenche o usuario e a senha e clica no botao
    login.with_('aaaaaaa', 'SuperSecretPassword!')
    # validar a msg
    assert login.failure_message()


def test_invalid_password(login):
    # preenche o usuario e a senha e clica no botao
    login.with_('tomsmith', 'asdkskskad')
    # validar a msg
    assert login.failure_message()
