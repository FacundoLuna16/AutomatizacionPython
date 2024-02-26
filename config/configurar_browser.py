from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager as EdgeDriverManager
from selenium.webdriver.chrome.service import Service


class BrowserConfig:
    """
    Clase para configurar el navegador que se usará en las pruebas.
    """

    def __init__(self, browser):
        self.BROWSER = browser

    def select_browser(self):
        """
        Método para seleccionar el navegador que se usará en las pruebas.
        """
        browser = self.BROWSER
        driver = None
        if browser == 'firefox':
            driver = webdriver.Firefox(
                service=Service(GeckoDriverManager().install()))
        elif browser == 'chrome':
            driver = webdriver.Chrome(service=Service(
                ChromeDriverManager().install()))
        elif browser == 'chrome-headless':
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                      options=self.chrome_headless_options())
        elif browser == 'edge':
            driver = webdriver.Edge(service=Service(
                EdgeDriverManager().install()))
        else:
            raise ValueError(f'--browser="{browser}" no esta definido')

        return driver
