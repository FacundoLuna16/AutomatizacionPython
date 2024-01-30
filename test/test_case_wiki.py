import pytest
import allure
from pages.wiki_home_page import WikiHomePage


class Tests:

    @allure.title("Validar Busqueda desde la caja de texto en ingles")
    @allure.description("Validar que la caja de texto funcione correctamente realizando una busqueda y validando el resultado en ingles")
    def test_buscar_en_ingles(self, driver):
        """
        Test para validar la funcionalidad de la caja de búsqueda.
        """
        with allure.step("Nos dirigimos a la pagina de Wikipedia"):
            driver.get("http://wikipedia.org")

        home_page = WikiHomePage(driver)
        with allure.step("Seleccionamos el idioma ingles"):
            home_page.seleccionar_idioma("English")

        with allure.step("Buscamos pytest"):
            home_page.ingresar_dato_caja_busqueda("pytest")

        with allure.step("Validamos que el titulo de la pagina sea el correcto"):
            assert "pytest" in driver.title, f"El título de la página no es el correcto. Debería ser pytest"


if __name__ == "__main__":
    pytest.main()
