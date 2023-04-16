import time



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class download:
    option = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "C:\\Users\\sathishkumar\\PycharmProjects\\weekendproject\\WeekEndSundayPython\\Downloadfile\\"}
    option.add_experimental_option("prefs", prefs)
    option.add_argument("--start-maximized")
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=option)


    def downdefaultlocation(self):
        #driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe')
        self.driver.get("https://www.leafground.com/grid.xhtml")
        self.driver.maximize_window()
        self.driver.find_element(By.ID,value="form:j_idt93").click()
        time.sleep(5)

    def downspecificlocation(self):
        self.driver.get("http://www.leafground.com/pages/download.html")
        #self.driver.maximize_window()
        self.driver.find_element_by_link_text("Download Excel").click()




D = download()
D.downspecificlocation()
