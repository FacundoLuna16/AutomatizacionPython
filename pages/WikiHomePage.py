from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
import pytest


class WikiHomePage:
    def __init__(self, driver):
        self.driver = driver

    # ***** IDENTIFICAMOS LOS ELEMENTOS POR SU LOCATOR EJEMPLO ID O XPATH
    idioma_espaniol = (By.ID, "js-link-box-es")
    caja = (By.ID, "searchInput")
    language_combo = (By.ID, "searchLanguage")

    def seleccionar_idioma(self, wait: WebDriverWait, idioma: str):
        try:
            wait.until(EC.visibility_of_element_located(self.language_combo))
            select_buscar = Select(self.driver.find_element(*self.language_combo))
            for option in select_buscar.options:
                if idioma in option.text:
                    self.report("Seleccionamos el Idioma: " + option.text)
                    option.click()
                    break
        except TimeoutException:
            pytest.fail("La caja de búsqueda de idioma no se visualiza.")

    def click_en_espaniol(self):
        self.assert_element_is_displayed(self.idioma_espaniol, "El idioma no se visualiza")
        self.driver.find_element(*self.idioma_espaniol).click()

    def get_caja_text(self):
        self.report("Obtiene el contenido de la caja de búsqueda")
        return self.driver.find_element(*self.caja).text

    def is_caja_displayed(self):
        self.report("Validar que exista la caja de búsqueda")
        return self.assert_element_is_displayed(self.caja)

    def ingresar_dato_caja_busqueda(self, dato):

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.caja))

        self.report("Esperamos, Localizamos y comprobamos que la caja de búsqueda se muestra")
        # verificar que la caja de búsqueda se visualiza
        self.assert_element_is_displayed(self.caja, "La caja de búsqueda NO se visualiza")
        # verificar que la caja de búsqueda está vacía
        self.assert_element_is_empty(self.caja, "La caja de texto NO está vacía")
        self.report("Ingresar la palabra " + dato)
        # ingresar el dato en la caja de búsqueda
        self.driver.find_element(*self.caja).send_keys(dato)
        self.report("Presionar Enter")
        self.driver.find_element(*self.caja).send_keys(Keys.ENTER)

        #esperar 3 segundos
        self.driver.implicitly_wait(3)

    def assert_element_is_displayed(self, locator, error_message):
        assert self.wait_for_element(locator).is_displayed(), error_message

    def assert_element_is_empty(self, locator, error_message):
        assert self.wait_for_element(locator).text.strip() == "", error_message

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

