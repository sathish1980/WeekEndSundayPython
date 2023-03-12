import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common import keys
class scroll():

    def scrollimplementation(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.leafground.com/drag.xhtml")
        self.driver.maximize_window()
        # scroll down
        self.driver.execute_script("window.scrollTo(0, 100)", "")
        time.sleep(1)
        # scroll up
        self.driver.execute_script("window.scrollTo(0, -100)", "")
        time.sleep(1)

        # scroll right
        self.driver.execute_script("window.scrollTo(100, 0)", "")
        time.sleep(1)
        # scroll left
        self.driver.execute_script("window.scrollTo(-100, 0)", "")
        time.sleep(1)
        # scroll bottom
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        #scroll up
        self.driver.execute_script("window.scrollTo(0, 0)", "")
        time.sleep(1)
        # screenshot
        startbutton=self.driver.find_element(by=By.ID,value="form:j_idt119")
        self.driver.execute_script("arguments[0].scrollIntoView();", startbutton)



obj= scroll()
obj.scrollimplementation()

