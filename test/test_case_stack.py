import pytest
import allure
from pages.stack_home_page import StackHomePage
from pages.stack_result_page import StackResultPage

parametros_busqueda = [
    ("pytest", "pytest"),
]


class Tests:

    @pytest.mark.parametrize("var_buscar, resultado", parametros_busqueda)
    @allure.title("Validar Busqueda desde la caja de texto")
    @allure.description(
        "Validar que la caja de texto funcione correctamente realizando una busqueda y validando el resultado"
    )
    def test_validar_caja_texto_nuevo(
        self, var_buscar, resultado, driver
    ):  # driver viene de conftest.py los demas parametros vienen del parametrize
        """
        Test para validar la funcionalidad de la caja de búsqueda.
        """
        steps = allure.step
        steps("Nos dirigimos a la pagina Stack Overflow en español")

        driver.get("https://es.stackoverflow.com/")
        home_page = StackHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.buscar(var_buscar)
        result_page = StackResultPage(driver)
        result_page.validar_contenido_URL(resultado)

    @allure.title("Validar redireccion a la página de usuarios")
    @allure.description("Validar que se redireccione a la página de usuarios")
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
