import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class webtab:

    def table(self,actualtext):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://leafground.com/table.xhtml")
        pagination ="//*[@class='ui-paginator-pages']//a";
        totalpagevalue = self.driver.find_elements(by=By.XPATH, value=pagination)
        sizeofpagelist = len(totalpagevalue)
        print(sizeofpagelist)
        for j in range(1, sizeofpagelist + 1):
            time.sleep(2)
            self.driver.find_element(by=By.XPATH, value=pagination + "[" + str(j) + "]").click()
            time.sleep(2)
            basepath = "//*[@id='form:j_idt89']//div[@class='ui-datatable-scrollable-body']//table//tbody//tr"

            totalrowvalue = self.driver.find_elements(by=By.XPATH,value=basepath)
            sizeofrowlist = len(totalrowvalue)
            for x in range(1, sizeofrowlist+1):
                totalcolumnvalue = self.driver.find_elements(by=By.XPATH,value=basepath+"[" + str(x) + "]//td")
                sizeofcolumnlist = len(totalcolumnvalue)
                text_Value = self.driver.find_element(by=By.XPATH,value=basepath+"[" + str(x) + "]//td[2]//span[3]").text
                #print(text_Value)
                if text_Value == actualtext:
                    print(self.driver.find_element(by=By.XPATH,value=basepath+"[" + str(x) + "]//td[1]").text)
                    print(self.driver.find_element(by=By.XPATH, value=basepath + "[" + str(x) + "]//td[3]//span[2]").text)
                    print(self.driver.find_element(by=By.XPATH, value=basepath + "[" + str(x) + "]//td[4]").text)
                    print(self.driver.find_element(by=By.XPATH, value=basepath + "[" + str(x) + "]//td[5]//span[2]").text)
                    #break
        time.sleep(2)
W= webtab()
W.table("Spain")