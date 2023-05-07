import pytest
from selenium.webdriver.common.by import By

from CommonClass.ElementDriver import ElementDriver

class FacebookLoginPAge(ElementDriver):

    def __init__(self,driver):
        self.driver=driver

    def EnterUseName(self,userName):
        self.EnterTextInToTextBox(self.driver.find_element(by=By.ID, value="email"), userName)

    def EnterPassword(self,passWord):
        self.EnterTextInToTextBox(self.driver.find_element(by=By.ID, value="pass"), passWord)

    def ClickLoginButton(self):
        self.CLickOnButton(self.driver.find_element(by=By.NAME, value="login"))