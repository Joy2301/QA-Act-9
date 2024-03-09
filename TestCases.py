"""Module providing a function printing python version."""

import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestSuite(unittest.TestCase):
    """Clase que representa los casos de prueba"""
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        """Caso de prueba de Inicio de Sesion"""

        # Navega a la página de inicio de sesión
        self.driver.get("https://the-internet.herokuapp.com/login")

        # Encuentra los campos de entrada para el nombre de usuario y la contraseña
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")

        # Ingresa las credenciales
        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")

        # Envía el formulario
        password_field.send_keys(Keys.RETURN)

        # Espera hasta que el mensaje de éxito aparezca
        success_message = self.driver.find_element(By.CSS_SELECTOR, ".flash.success")
        assert "You logged into a secure area!" in success_message.text

        time.sleep(10)

    def test_navigation(self):
        """Caso de prueba de Navegacion en las secciones"""
        
        # Navega a diferentes secciones del sitio
        sections = ["hovers", "dropdown", "typos"]
        for section in sections:
            self.driver.get(f"https://the-internet.herokuapp.com/{section}")
            title = self.driver.find_element(By.TAG_NAME, "h3")
            self.assertIn(section.capitalize(), title.text)

    def test_form_submission(self):
        """Caso de prueba de envio de formulario"""

        # Navega a la página del formulario
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")

        # Encuentra los elementos de checkbox y los marca
        checkboxes = self.driver.find_elements(By.XPATH, "input[@id='checkboxes']")
        for checkbox in checkboxes:
            checkbox.click()

        # Verifica que todos los checkboxes estén seleccionados
        for checkbox in checkboxes:
            #assert checkbox.is_selected()
            assert all([c.is_selected() for c in checkboxes])

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports', report_title='Reporte de Pruebas', descriptions=True, combine_reports=True))