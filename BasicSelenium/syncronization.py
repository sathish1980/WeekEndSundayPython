import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class syncronisation:

    def syncimplementaion(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        #self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH,value="//*[text()='Create new account']").click()
        WebDriverWait(self.driver, 10).until(
           EC.visibility_of_element_located((By.NAME, "firstname")))
        #time.sleep(2)
        self.driver.find_element(by=By.NAME,value="firstname").send_keys("sathish")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "lastname")))
        self.driver.find_element(by=By.NAME, value="lastname").send_keys("sathish")
        time.sleep(3)

obj=syncronisation()
obj.syncimplementaion()