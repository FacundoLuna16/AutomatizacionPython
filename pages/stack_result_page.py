

class StackResultPage:

    def __init__(self, driver):
        self.driver = driver

    def validar_contenido_URL(self, texto):
        assert texto in self.driver.current_url, f"El valor {texto} no se encuentra en la URL"
