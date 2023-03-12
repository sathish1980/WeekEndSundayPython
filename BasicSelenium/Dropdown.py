import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class dropdown:

    def singleselectdropdown(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://www.facebook.com")
        # self.driver.find_element_by_xpath("//a[text()='Create New Account']").click()
        self.driver.find_element(by=By.XPATH, value="//*[text()='Create new account']").click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "firstname")))
        # time.sleep(2)
        self.driver.find_element(by=By.NAME, value="firstname").send_keys("sathish")

        daydropwn = Select(self.driver.find_element(by=By.ID,value="day"))
        daydropwn.select_by_index(4)

        mothdropwn = Select(self.driver.find_element(by=By.ID, value="month"))
        mothdropwn.select_by_value("6")

        yrdropwn = Select(self.driver.find_element(by=By.ID, value="year"))
        yrdropwn.select_by_visible_text("2000")

        time.sleep(3)

    def multiselectdropdown(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
        multiselect = Select(self.driver.find_element(by=By.XPATH, value="//select[@id='second']"))
        if multiselect.is_multiple ==True:
            multiselect.select_by_index(2)
            time.sleep(2)
            multiselect.select_by_visible_text("Pizza")
            time.sleep(2)
            multiselect.deselect_by_index(2)
            time.sleep(2)
            multiselect.select_by_index(3)
            time.sleep(2)
            multiselect.deselect_all()
            time.sleep(2)


obj= dropdown()
obj.multiselectdropdown()
