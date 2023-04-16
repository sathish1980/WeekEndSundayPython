import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class winhandle:
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    def winhandle(self):
        self.driver.get("https://leafground.com/window.xhtml")
        self.driver.maximize_window()
        parent_window = self.driver.current_window_handle
        self.driver.find_element(by=By.ID,value="j_idt88:new").click()

        ALL_window = self.driver.window_handles

        for child in ALL_window :

            if child!=parent_window :
                self.driver.switch_to.window(child) # switch in to particular window
                elementpreset = self.driver.find_elements(by=By.XPATH,value="//*[@id='menuform:j_idt41']") # eleent identification in the window
                elementpresent_count = len(elementpreset)
                if elementpresent_count >0 :
                    self.driver.find_element(by=By.XPATH,value="//*[@id='menuform:j_idt41']").click()
                    time.sleep(1)
                    self.driver.find_element(by=By.XPATH,value="//*[@id='menuform:m_table']").click()
                    print(self.driver.title)
                    self.driver.switch_to.window(parent_window)
                    break
        time.sleep(3)
    def OpenMultiplewinhandle(self):
        self.driver.get("https://leafground.com/window.xhtml")
        self.driver.maximize_window()
        parent_window = self.driver.current_window_handle
        self.driver.find_element(by=By.ID,value="j_idt88:j_idt91").click()

        ALL_window = self.driver.window_handles

        for child in ALL_window :

            if child!=parent_window :
                self.driver.switch_to.window(child) # switch in to particular window
                self.driver.maximize_window()
                elementpreset = self.driver.find_elements(by=By.XPATH,value="//*[@id='menuform:j_idt41']") # eleent identification in the window
                elementpresent_count = len(elementpreset)
                if elementpresent_count >0 :
                    self.driver.find_element(by=By.XPATH,value="//*[@id='menuform:j_idt41']").click()
                    time.sleep(1)
                    self.driver.find_element(by=By.XPATH,value="//*[@id='menuform:m_table']").click()
                    print(self.driver.title)
                    self.driver.switch_to.window(parent_window)
                    break
        time.sleep(10)
    def morethantwowinhandle(self):
        self.driver.get("http://www.leafground.com/pages/Window.html")
        self.driver.maximize_window()
        parent_window = self.driver.current_window_handle
        self.driver.find_element_by_xpath("//button[text()='Open Multiple Windows']").click()

        ALL_window = self.driver.window_handles

        for child in ALL_window :

            if child!=parent_window :
                self.driver.switch_to.window(child)
                self.driver.maximize_window()
                elementpreset = self.driver.find_elements_by_id("home")
                elementpresent_count = len(elementpreset)
                if elementpresent_count >0 :
                    self.driver.find_element_by_id("home").click()
                    self.driver.find_element_by_xpath("//h5[text()='Edit']//parent::a").click()
                    self.driver.find_element_by_id("email").send_keys("kumar.sathish189")
                    #self.driver.switch_to.window(parent_window)
                    #self.driver.quit()
                    break

                else  :
                    print()
                     #self.driver.switch_to.window(parent_window)

W= winhandle()
W.OpenMultiplewinhandle()