class ElementDriver():

    def EnterTextInToTextBox(self,TextboxWebElement,TextToBeEneter):
        if(TextboxWebElement.is_displayed()):
            TextboxWebElement.send_keys(TextToBeEneter)

    def CLickOnButton(self,TextboxWebElement):
        if(TextboxWebElement.is_displayed()):
            TextboxWebElement.click()