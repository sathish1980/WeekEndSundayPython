import time

import pytest
from selenium.webdriver.common.by import By

from CommonClass.ElementDriver import ElementDriver
from Pages.FacebookLoginPage import FacebookLoginPAge
from PytestConcepts.Testdata import Testdata


@pytest.mark.usefixtures("BrowserLaunch")
class Test_FacebookloginandLogout(ElementDriver):

    def test_Launc(self):
        self.driver.get("http://www.facebook.com")
        print(self.driver.title)

    def test_FacebookValidLoginandLogout(self,fbloginvaliddataFromExecl):
        #self.driver.find_element(by=By.ID, value="email").send_keys("kumar.sathish189@gmail.com")

        #self.driver.find_element(by=By.ID, value="pass").send_keys("Admin@123")

        # self.driver.find_element(by=By.ID, value="email").send_keys("kumar.sathish189@gmail.com")
        # self.driver.find_element(by=By.ID, value="pass").send_keys("Admin@123")
        #self.driver.find_element(by=By.NAME, value="login").click()
        #TextboxWebElement = self.driver.find_element(by=By.ID, value="email")
        size = len(Testdata.credential_excel_dic[0])
        print(size)
        value = size / 5
        print(value)
        for i in range(1, int(value) + 1):
            LoginPage = FacebookLoginPAge(self.driver)
            #LoginPage.EnterUseName(FBUsername[0])
            #LoginPage.EnterPassword(FBUsername[1])
            LoginPage.EnterUseName(fbloginvaliddataFromExecl["username"+str(i)])
            LoginPage.EnterPassword(fbloginvaliddataFromExecl["password"+str(i)])
            LoginPage.ClickLoginButton()
           # passwordElement = self.driver.find_element(by=By.ID, value="pass")
            #self.EnterTextInToTextBox(self.driver.find_element(by=By.ID, value="pass"), "Admin@123")
            #loginButton = self.driver.find_element(by=By.NAME, value="login")
            #self.CLickOnButton(self.driver.find_element(by=By.NAME, value="login"))
            time.sleep(5)
            #self.explictiwaitbyxpathforclickable("(//div[@aria-label='Your profile'])[1]")
            self.driver.find_element(by=By.XPATH, value="//*[local-name()='svg' and @aria-label='Your profile']").click()
            time.sleep(3)
            #self.explictiwaitbyxpathforclickable("(//span[text()='Log Out']//parent::div//parent::div)[1]")
            self.driver.find_element(by=By.XPATH, value="(//span[text()='Log Out']//parent::div//parent::div)[1]").click()
            time.sleep(5)

    def test_FacebookinValidLogin(self):
        self.driver.find_element(by=By.ID, value="email").send_keys("23342312323")
        #self.driver.find_element(by=By.ID, value="pass").send_keys("Admin@123")
        # self.driver.find_element(by=By.ID, value="email").send_keys("kumar.sathish189@gmail.com")
        # self.driver.find_element(by=By.ID, value="pass").send_keys("Admin@123")
        self.driver.find_element(by=By.NAME, value="login").click()
        time.sleep(5)
        errorMessage = self.driver.find_element(by=By.XPATH,value="//*[@id='email_container']//div[2]").text
        print(errorMessage)

