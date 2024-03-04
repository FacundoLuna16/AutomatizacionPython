# conftest.py
import pytest
from config.browser import BrowserConfig
import os


def pytest_addoption(parser):
    """
    Agregar opciones de línea de comandos para seleccionar el navegador
    """
    parser.addoption("--browser", action="store", default="chrome",
                     help="Escoger navegador: chrome o edge")
    parser.addoption("--ambiente", action="store", default="qa",
                     help="Escoger el ambiente de ejecución: qa o prod")


def pytest_configure(config):
    os.environ["ambiente"] = config.getoption("ambiente")
    os.environ["browser"] = config.getoption("browser")


@pytest.fixture(autouse=True)
def driver(request):
    """
    Fixture para inicializar el driver del navegador
    """
    driver = BrowserConfig(os.getenv("browser")).select_browser()
    driver.maximize_window()

    yield driver  # Retorna el objeto driver para que esté disponible en las pruebas

    print("Cerrar Browser")
    driver.quit()
