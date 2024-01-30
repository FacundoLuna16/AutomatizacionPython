from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class StackHomePage:

    buscador = "//input[@placeholder='Buscar…']"
    btn_aceptar_cookies = "//button[@id='onetrust-accept-btn-handler']"
    btn_iniciar_sesion = "//a[normalize-space()='Iniciar sesión']"
    btn_registrarse = "//a[normalize-space()='Registrarse']"


    def __init__(self, driver):
        self.driver = driver

    
    def click_aceptar_cookies(self):
        if self.driver.find_element(By.XPATH, self.btn_aceptar_cookies).is_displayed():
            self.driver.find_element(By.XPATH, self.btn_aceptar_cookies).click()
            print("Aceptamos las cookies")
        else:
            print("Ya se aceptaron las cookies")
    
    def buscar(self, texto):
        if self.driver.find_element(By.XPATH, self.buscador).is_displayed():
            print("La caja de búsqueda está visible")
            self.driver.find_element(By.XPATH, self.buscador).clear()
            print("Limpiamos la caja de búsqueda")
            self.driver.find_element(By.XPATH, self.buscador).send_keys(texto)
            print(f"Ingresamos el valor {texto} en la caja de búsqueda")
            self.driver.find_element(By.XPATH, self.buscador).send_keys(Keys.ENTER)
            print("Presionamos ENTER")

    
    



