import pytest
from pages.stack_home_page import StackHomePage
from pages.stack_result_page import StackResultPage

parametros_busqueda = [
    ("pytest", "pytest"),
]

class Tests:

    @pytest.mark.parametrize("var_buscar, resultado", parametros_busqueda)
    def test_validar_caja_texto_nuevo(self,var_buscar, resultado,driver):#driver viene de conftest.py los demas parametros vienen del parametrize
        """
        Test para validar la funcionalidad de la caja de búsqueda.
        """
        driver.get("https://es.stackoverflow.com/")
        print("Validamos que se cargue la página")
        home_page = StackHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.buscar(var_buscar)

        result_page = StackResultPage(driver)
        result_page.validar_contenido_URL(resultado)



    def test_ir_usuarios(self,driver):
        """
        Test para verificar la navegación a la página de usuarios.
        """
        driver.get("https://es.stackoverflow.com/")
        home_page = StackHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.click_usuarios()

        result_page = StackResultPage(driver)
        result_page.validar_contenido_URL("users")

if __name__ == "__main__":
    pytest.main()
