import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class listconcepts:

    def listimplmentation(self,expectedcountry):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.leafground.com/dashboard.xhtml")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[@id='menuform:j_idt40']//a)[1]")))

        self.driver.find_element(by=By.XPATH,value="(//*[@id='menuform:j_idt40']//a)[1]").click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//*[@id='menuform:m_dropdown']//a)[1]")))
        self.driver.find_element(by=By.XPATH, value="(//*[@id='menuform:m_dropdown']//a)[1]").click()
        self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt87:country']//div[3]").click()
        countryvalue = self.driver.find_elements(by=By.XPATH,value="//*[@id='j_idt87:country_items']//li")
        for eachcountryval in countryvalue:
            actualcountry=eachcountryval.text
            print(actualcountry)
            if actualcountry == expectedcountry:
                eachcountryval.click()
                break
        time.sleep(2)

obj = listconcepts()
obj.listimplmentation("Germany")

