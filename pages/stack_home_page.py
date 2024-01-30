from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class StackHomePage:

    buscador = "//input[@placeholder='Search…']"
    btn_aceptar_cookies = "//button[@id='onetrust-accept-btn-handler']"
    btn_iniciar_sesion = "//a[normalize-space()='Iniciar sesión']"
    btn_registrarse = "//a[normalize-space()='Registrarse']"


    def __init__(self, driver):
        self.driver = driver

    
    def click_aceptar_cookies(self):
        self.driver.find_element(By.XPATH, self.btn_aceptar_cookies).click()
    
    def buscar(self, texto):
        self.driver.find_element(By.XPATH, self.buscador).clear()
        self.driver.find_element(By.XPATH, self.buscador).send_keys(texto)
        self.driver.find_element(By.XPATH, self.buscador).send_keys(Keys.ENTER)
    
    



