import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common import keys

class mouseactions():

    def mouseactiosnimplementation(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.ebay.com/")
        mainamenu = self.driver.find_element(by=By.LINK_TEXT,value="Electronics")
        mouseactions=ActionChains(self.driver)
        mouseactions.move_to_element(mainamenu).perform()
        mouseactions.move_to_element(self.driver.find_element(by=By.LINK_TEXT,value="Cameras and photos")).click().perform()
        """WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='gh-ac-box2']//input[@id='gh-ac']")))
        self.driver.find_element(by=By.XPATH,value="//*[@id='gh-ac-box2']//input[@id='gh-ac']").send_keys("shoes")
        mouseactions.move_to_element(self.driver.find_element(by=By.XPATH,value="//*[@id='gh-ac-box2']//input[@id='gh-ac']")).double_click().context_click().perform()"""

    def facebook(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        mouseactions = ActionChains(self.driver)
        mouseactions.move_to_element(
            self.driver.find_element(by=By.ID, value="email")).send_keys(
            "sathish").key_down(Keys.TAB).key_up(Keys.TAB).perform()

    def draganddrop(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.leafground.com/drag.xhtml")
        mouseactions = ActionChains(self.driver)
        mouseactions.move_to_element(self.driver.find_element(by=By.ID,value="form:drag_content")).drag_and_drop(self.driver.find_element(by=By.ID,value="form:drag_content"),self.driver.find_element(by=By.ID,value="form:drop_content")).perform()


    def mouseotheractions(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        mouseactions = ActionChains(self.driver)
        mouseactions.move_to_element(
            self.driver.find_element(by=By.ID, value="email")).send_keys(
            "sathish").double_click().context_click().perform()
        time.sleep(3)

    def facebookkeyboard(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        mouseactions = ActionChains(self.driver)
        mouseactions.move_to_element(
            self.driver.find_element(by=By.ID, value="email")).send_keys(
            "sathish").double_click().context_click().perform()
        time.sleep(1)
        pyautogui.press(['down','down','down','down'])

        """pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')"""

        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.press("tab")
        pyautogui.hotkey('ctrl','v')

    def facebookkeyboardwithinapp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        mouseactions = ActionChains(self.driver)

        self.driver.find_element(by=By.ID, value="email").send_keys("sathish")
        mouseactions.key_down(keys.Keys.TAB).key_up(keys.Keys.TAB).key_down(keys.Keys.TAB).key_up(keys.Keys.TAB).key_down(keys.Keys.TAB).key_up(keys.Keys.TAB).perform()
        time.sleep(2)




obj=mouseactions()
obj.facebookkeyboardwithinapp()