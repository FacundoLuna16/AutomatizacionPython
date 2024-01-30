#https://es.stackoverflow.com/ 
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.stack_home_page import StackHomePage
from pages.stack_result_page import StackResultPage
from time import sleep

parametros_busqueda = [
    ("pytest", "pytest"),
]

class Tests:

    @pytest.mark.parametrize("var_buscar, resultado", parametros_busqueda)
    def test_validar_caja_texto_nuevo(self,var_buscar, resultado,driver):#driver viene de conftest.py los demas parametros vienen del parametrize
        driver.get("https://es.stackoverflow.com/")
        print("Validamos que se cargue la página")
        home_page = StackHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.buscar(var_buscar)

        result_page = StackResultPage(driver)
        result_page.validar_contenido_URL(resultado)
        # sleep(5)


if __name__ == "__main__":
    pytest.main()
