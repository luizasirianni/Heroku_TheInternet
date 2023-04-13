#1 bibliotecas
from selenium.webdriver.common.by import By

#2 classe
class LoginPage():

    #2.1 mapeamento dos elementos da página
    _username_input = {'by': By.ID, 'value': 'username'} #json
    _password_input = {'by': By.ID, 'value': 'password'}
    _login_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _success_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.success'}
    _failure_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.error'}
    #2.2 construtor / inicializador
    def __init__(self, driver):
        self.driver.get('https://the-internet.herokuapp.com/login')

    def with_(self, username, password):
        self.driver.find_element(self._username_input['by'],
                                 self._username_input['value']).send_keys(username)
        self.driver.find_element(self._password_input['by'],
                                 self._password_input['value']).send_keys(password)
        self.driver.find_element(self._login_button['by'],
                                 self._login_button['value']).click()
    #2.3 ações realizadas

    def success_message(self):
        return self.driver.find_element(self._success_message['by'],
                                        self._success_message['value']).is_displayed()
    def failure_message(self):
        return self.driver.find_element(self._failure_message['by'],
                                        self._failure_message['value']).is_displayed()

