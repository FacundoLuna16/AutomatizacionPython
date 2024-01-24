from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class WikiResultadosPage:
    def __init__(self, driver):
        self.driver = driver

    # Elemento de la página identificado por su locator (ID)
    lbl_titulo = (By.ID, "firstHeading")

    def obtener_titulo(self):
        print("Localizar y comprobar que el título esté disponible")
        return self.driver.find_element(*self.lbl_titulo).text

    def validar_titulo(self, wait, titulo):
        wait.until(EC.visibility_of_element_located(self.lbl_titulo))
        titulo_resultado = self.driver.find_element(*self.lbl_titulo)
        assert titulo_resultado.text.contains(titulo), "El título no es el correcto"
        print("Texto encontrado:", titulo_resultado.text)
