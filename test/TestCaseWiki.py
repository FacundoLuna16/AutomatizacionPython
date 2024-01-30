import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
parametros_busqueda = [
    ("Selenium", "Selenium"),
    # ("TDD", "Desarrollo guiado por pruebas"),
    # ("JAVA", "Java (lenguaje de programación)"),
    # ("DATA DRIVEN TESTING", "Data-driven testing")
]

class Tests:

    @pytest.mark.parametrize("var_buscar, resultado", parametros_busqueda)
    def test_validar_caja_texto_nuevo(self, var_buscar, resultado,driver):#driver viene de conftest.py los demas parametros vienen del parametrize
        caja_busqueda = driver.find_element(By.ID, "searchInput")
        print("Limpiamos la caja de búsqueda")
        caja_busqueda.clear()
        print(f"Ingresamos el valor {var_buscar} en la caja de búsqueda")
        caja_busqueda.send_keys(var_buscar)
        print("Presionamos ENTER")
        caja_busqueda.send_keys(Keys.ENTER)
        titulo_resultados = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "firstHeading")))
        print(f"Validar que el título sea {resultado}")
        assert resultado in titulo_resultados.text, f"El valor {resultado} no se encuentra en el título"

if __name__ == "__main__":
    pytest.main()
