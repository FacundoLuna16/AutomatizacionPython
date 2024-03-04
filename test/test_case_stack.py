import pytest
import allure
from pages.stack_home_page import StackHomePage
from pages.stack_result_page import StackResultPage
from utils.data_driven import DatosConfig
import os
from config.browser import BrowserConfig


def datos_ambiente():
    ambiente = os.getenv("ambiente")
    datos = DatosConfig(ambiente)
    return datos.obtener_datos_xlsx("Sheet1")


class Test:
    """
    Clase para realizar las pruebas de la página de Stack Overflow en español.
    """

    @pytest.mark.skip
    @allure.title("Validar Busqueda desde la caja de texto")
    @allure.description(
        "Validar que la caja de texto funcione correctamente realizando una busqueda y validando el resultado"
    )
    @pytest.mark.noprod
    @pytest.mark.parametrize("busqueda, resultado, navegador, url", datos_ambiente())
    def test_validar_caja_texto_nuevo(self, driver, busqueda, resultado, navegador, url):
        """
        Test para validar la funcionalidad de la caja de búsqueda.
        """

        # driver = BrowserConfig(navegador).select_browser()
        # driver.maximize_window()

        with allure.step("Nos dirigimos a la pagina Stack Overflow en español"):
            driver.get(url)

        home_page = StackHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.limpiar_caja_busqueda()
        home_page.buscar(busqueda)
        result_page = StackResultPage(driver)
        result_page.validar_contenido_URL(resultado)

    # @pytest.mark.skip
    @allure.title("Validar redireccion a la página de usuarios")
    @allure.description("Validar que se redireccione a la página de usuarios")
    @pytest.mark.smoke
    def test_ir_usuarios(self, driver):
        """
        Test para verificar la navegación a la página de usuarios.
        """
        with allure.step("Nos dirigimos a la pagina Stack Overflow en español"):
            driver.get("https://es.stackoverflow.com/")
        home_page = StackHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.click_usuarios()
        result_page = StackResultPage(driver)
        result_page.validar_contenido_URL("users")


if __name__ == "__main__":
    pytest.main()
