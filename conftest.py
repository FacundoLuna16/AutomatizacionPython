# conftest.py
import pytest
from config.configurar_browser import BrowserConfig


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Escoger navegador: chrome o edge")
    #TODO agregar otra opción para el ambiente de pruebas
    #TODO agregar una opcion para pasar la url por parametro


@pytest.fixture(autouse=True)
def driver(request):

    browser = request.config.getoption("--browser")
    print(f"Se ejecutará las pruebas en el navegador {browser}")
    if browser is None:
        raise ValueError("No se ha seleccionado un navegador")
    driver = BrowserConfig(browser).select_browser()
    driver.maximize_window()

    yield driver  # Retorna el objeto driver para que esté disponible en las pruebas

    print("Cerrar Browser")
    driver.quit()
