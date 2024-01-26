import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.configurar_browser import BrowserConfig

parametros_busqueda = [
    ("Selenium", "Selenium"),
    # ("TDD", "Desarrollo guiado por pruebas"),
    # ("JAVA", "Java (lenguaje de programación)"),
    # ("DATA DRIVEN TESTING", "Data-driven testing")
]

class TestWiki:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        browser= "edge"
        self.driver = BrowserConfig(browser).select_browser()
        self.driver.maximize_window()
        self.driver.get("http://wikipedia.org")

        yield  # Lo que esté después de yield se ejecuta después de cada test

        print("Cerrar Browser")
        self.driver.quit()

    @pytest.mark.parametrize("var_buscar, resultado", parametros_busqueda)
    def test_validar_caja_texto_nuevo(self, var_buscar, resultado):
        caja_busqueda = self.driver.find_element(By.ID, "searchInput")
        print("Limpiamos la caja de búsqueda")
        caja_busqueda.clear()
        print(f"Ingresamos el valor {var_buscar} en la caja de búsqueda")
        caja_busqueda.send_keys(var_buscar)
        print("Presionamos ENTER")
        caja_busqueda.send_keys(Keys.ENTER)
        titulo_resultados = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "firstHeading")))
        print(f"Validar que el título sea {resultado}")
        assert resultado in titulo_resultados.text, f"El valor {resultado} no se encuentra en el título"

if __name__ == "__main__":
    pytest.main()
