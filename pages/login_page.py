# 1 bibliotecas
from selenium.webdriver.common.by import By
from pages.base_page import BasePage  # herança da classe base page


# 2 classe
class LoginPage(BasePage): #faz uso do mapeamento da classe BasePage
    # 2.1 mapeamento dos elementos da página
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _login_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _success_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.success'}
    _failure_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.error'}
    _login_form = {'by': By.ID, 'value': 'login'}

    # 2.2 construtor / inicializador
    def __init__(self, driver):
        # instanciando o selenium:
        self.driver = driver
        # abrindo a pagina alvo
        self._geturl('https://the-internet.herokuapp.com/login')
        # validando se o formulario de login está visível
        assert self._visualize(self._login_form)

    def with_(self, username, password):
        # programaçao com page object
        self._write(self._username_input, username)
        self._write(self._password_input, password)
        self._click(self._login_button)


'''     # programação comum - sem page object   
        self.driver.find_element(self._username_input['by'],
                                 self._username_input['value']).send_keys(username)
        self.driver.find_element(self._password_input['by'],
                                 self._password_input['value']).send_keys(password)
        self.driver.find_element(self._login_button['by'],
                                 self._login_button['value']).click()'''

# 2.3 ações realizadas

def success_message(self):
    return self._visualize(self._success_message, 5)


''' # programaçao sem page object
    return self.driver.find_element(self._success_message['by'],
                                    self._success_message['value']).is_displayed()'''


def failure_message(self):
    return self._visualize(self._failure_message, 5)


''' # programaçao sem page object
    return self.driver.find_element(self._failure_message['by'],
                                    self._failure_message['value']).is_displayed()'''
