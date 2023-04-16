import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class dpwon:
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    def radiobutton(self,actaultext):
        self.driver.get("https://www.leafground.com/radio.xhtml")
        eachval=self.driver.find_elements(by=By.XPATH,value="//*[@id='j_idt87:console1']//td[2]//label")
        for val in eachval :
            eachradiobutton = val.text
            print(eachradiobutton)
            if(eachradiobutton==actaultext):
                print(actaultext)
                self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt87:console1']//td[2]//*[@class='ui-radiobutton ui-widget']//div[2]").click()
                break
        time.sleep(2)

    def Alert(self):
        self.driver.get("https://www.leafground.com/alert.xhtml")
        self.driver.find_element(by=By.ID,value="j_idt88:j_idt91").click()
        self.driver.switch_to.alert.accept()
        time.sleep(1)
        self.driver.find_element(by=By.ID,value="j_idt88:j_idt93").click()
        self.driver.switch_to.alert.dismiss()
        time.sleep(1)
        self.driver.find_element(by=By.ID,value="j_idt88:j_idt104").click()
        obj = self.driver.switch_to.alert
        obj.send_keys("Besant technilogies")
        time.sleep(1)
        print(obj.text)
        obj.accept()
        self.driver.find_element(by=By.ID,value="j_idt88:j_idt95").click()
        time.sleep(2)
        self.driver.find_element(by=By.ID,value="j_idt88:j_idt98").click()
        time.sleep(2)
    def verification(self):
        self.driver.get("https://www.leafground.com/checkbox.xhtml")
        #Get Title
        print(self.driver.title)
        # Get currenturl
        print(self.driver.current_url)
        # Get attribute
        classattributename = self.driver.find_element(by=By.XPATH, value="//*[@id='j_idt87:j_idt89']//div[2]").get_attribute("class")
        print(classattributename)
        # Get text
        textoftheelement = self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt87:j_idt89']//span[@class='ui-chkbox-label']").text
        print(textoftheelement)

        # currentwindowname
        classattributename = self.driver.current_window_handle
        print(classattributename)
        classattributenames = self.driver.window_handles
        print(classattributenames)
    def validation(self):
        self.driver.get("https://www.leafground.com/checkbox.xhtml")
        time.sleep(2)
        print(self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt87:j_idt89']//div[2]").is_displayed())
        print(self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt87:j_idt89']//div[2]").is_enabled())
        valu= self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt87:j_idt89']//div[2]").is_selected()
        print(valu)
        if valu == False :
            self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt87:j_idt89']//div[2]").click()
            time.sleep(2)
        print(self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt87:j_idt89']//div[2]").is_selected())
        afterclick =self.driver.find_element(by=By.XPATH, value="//*[@id='j_idt87:j_idt89']//div[2]").get_attribute("class")
        print(afterclick)
        if afterclick.__contains__("active"):
            print("Its selected")



d= dpwon()
d.verification()