from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from utils import Utiles


class DriverFactory:

    @staticmethod
    def levantar_browser(driver, context):
        Utiles.separador()
        browser_name = context.current_xml_test.get("NombreNavegador")
        url = context.current_xml_test.get("Url")

        if browser_name == "CHROME":
            # Usando WebDriver para Chrome
            print("Abro browser")
            driver = webdriver.Chrome(executable_path="C:\\chrome/chromedriver.exe")
        elif browser_name == "FIREFOX":
            # Usando WebDriver para Firefox
            # TODO: Ejecutar con Firefox
            print("Abro browser")
            driver = webdriver.Firefox(executable_path="driverBrowsers\\firefox\\geckodriver.exe")
        else:
            print("No se seleccionó ningún navegador correcto, se asignará Chrome por defecto")
            print("Abro browser")
            driver = webdriver.Chrome(executable_path="Recursos/chromedriver.exe")

        driver.maximize_window()
        driver.get(url)
        return driver

    @staticmethod
    def finalizar_browser(driver):
        print("Cerrando el browser")
        Utiles.separador()
        driver.quit()
        driver = None
