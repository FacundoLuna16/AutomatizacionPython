from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StackHomePage:
    """
    Clase que representa la Page Object de la página principal de Stack Overflow en español.
    """

    buscador = (By.XPATH, "//input[@placeholder='Buscar…']")
    btn_aceptar_cookies = (
        By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    btn_iniciar_sesion = (By.XPATH, "//a[normalize-space()='Iniciar sesión']")
    btn_registrarse = (By.XPATH, "//a[normalize-space()='Registrarse']")
    btn_usuario = (By.CSS_SELECTOR, "#nav-users")

    def __init__(self, driver):
        self.driver = driver

    def click_aceptar_cookies(self):
        """
        Método para hacer clic en el botón de aceptar cookies.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_aceptar_cookies)
        )

        if self.driver.find_element(*self.btn_aceptar_cookies).is_displayed():
            self.driver.find_element(*self.btn_aceptar_cookies).click()
            print("Aceptamos las cookies")
        else:
            print("Ya se aceptaron las cookies")

    def buscar(self, texto):
        """
        Método para realizar una búsqueda en la caja de búsqueda.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.buscador)
        )
        print("Validamos que se cargue el campo de búsqueda")
        if self.driver.find_element(*self.buscador).is_displayed():
            print("La caja de búsqueda está visible")
            self.driver.find_element(*self.buscador).clear()
            print("Limpiamos la caja de búsqueda")
            self.driver.find_element(*self.buscador).send_keys(texto)
            print(f"Ingresamos el valor {texto} en la caja de búsqueda")
            self.driver.find_element(*self.buscador).send_keys(Keys.ENTER)
            print("Presionamos ENTER")

    def click_usuarios(self):
        """
        Método para dirigirse a la sección de usuarios.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_usuario)
        )
        if self.driver.find_element(*self.btn_usuario).is_displayed():
            self.driver.find_element(*self.btn_usuario).click()
            print("Hacemos clic en el botón de usuarios")
        else:
            print("El botón de usuarios no está visible")

    def verificar_contenido_URL(self, texto):
        """
        Método para verificar que la URL contenga el texto esperado.
        """
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(texto)
        )
        print("Validamos que la URL contenga el texto esperado")
        assert texto in self.driver.current_url, f"La URL no contiene el texto {
            texto}"
