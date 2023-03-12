import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class firstclass:

    def launc(self):
        #self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        """self.driver.set_window_size(300,500)
        self.driver.quit()
        self.driver.minimize_window()"""
        self.driver.get("https://www.facebook.com/")
        """self.driver.get("https://www.gmail.com/")
        self.driver.back()
        self.driver.forward()
        self.driver.refresh()"""
        #username=self.driver.find_element(by=By.ID,value="email")
        #username = self.driver.find_element(by=By.CSS_SELECTOR, value="input#email")
        username = self.driver.find_element(by=By.CSS_SELECTOR, value="input[data-testid=royal_email]")
        username=self.driver.find_element(by=By.XPATH,value="//input[@type='text']")
        username.send_keys("sathish")
        username.clear()
        self.driver.find_element(by=By.NAME, value="email").send_keys("kumar")
        #self.driver.find_element(by=By.CLASS_NAME,value="inputtext _55r1 _6luy").send_keys("sara")
       # self.driver.find_element(by=By.LINK_TEXT,value="Forgotten password?").click()
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="word?").click()


        time.sleep(2)


obj = firstclass()
obj.launc()