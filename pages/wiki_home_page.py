from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
import pytest
import allure


class WikiHomePage:
    """
    Clase que representa la Page Object de la página principal de Wikipedia.
    """

    idioma_espaniol = (By.ID, "js-link-box-es")
    caja = (By.ID, "searchInput")
    language_combo = (By.XPATH, "//select[@id='searchLanguage']")

    def __init__(self, driver):
        self.driver = driver

    def seleccionar_idioma(self, idioma: str):
        """
        Selección de idioma en la página de Wikipedia.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.language_combo)
        )
        combo = Select(self.driver.find_element(*self.language_combo))
        # metodo para seleccionar el idioma
        combo.select_by_visible_text(idioma)
        assert idioma in combo.first_selected_option.text, f"El idioma seleccionado no es el correcto. Debería ser {
            idioma}"

    def ingresar_dato_caja_busqueda(self, dato):
        """
        Ingreso de un dato en la caja de búsqueda.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.caja)
        )

        self.driver.find_element(*self.caja).clear()
        self.driver.find_element(*self.caja).send_keys(dato)
        self.driver.find_element(*self.caja).send_keys(Keys.ENTER)
