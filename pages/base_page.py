from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests import config

class BasePage():

    def __init__(self, driver):
        self.driver = driver # este é o selenium

    def _geturl(self, url):
        if url.startwith('http'): #se o endereço começa com http ou https
            self.driver.get(url)
        else:
            self.driver.get(config.baseurl + url)
    def _findelement(self, locator):
        #estrutura genérica pra localizar qualquer elemento
        return self.driver.find_element(locator['by'], locator['value'])

    def _click(self, locator):
        self._findelement(locator).click()

    def _write(self, locator, text):
        self._findelement(locator).send_keys(text)

    def _visualize(self, locator, timeout=0):
        #função para os asserts
        #timeout = qual o tempo que vai esperar algo acontecer
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout) #espera explicita
                wait.until(expected_conditions.visibility_of_element_located((locator['by'], locator['value'])))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._findelement(locator).is_displayed()
            except NoSuchElementException:
                return False
