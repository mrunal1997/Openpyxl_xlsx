class Contact:
    def __init__(self, driver):
        self.driver = driver
        # super().__init__()

        self.xpath_contactPage = "//a[normalize-space()='Contact']"
        self.xpath_first_name = "//input[@id='wpforms-161-field_0']"
        self.xpath_last_name = "//input[@id='wpforms-161-field_0-last']"
        self.xpath_emailID = "//input[@id='wpforms-161-field_1']"
        self.xpath_comment = "//textarea[@id='wpforms-161-field_2']"
        self.xpath_botCheckbox = "//div[@style='width: 304px; height: 78px;']"
        self.xpath_submitBtn = "//button[@id='wpforms-submit-161']"
        self.xpath_thankyou_msg = "//p[contains(text(),'Thanks for contacting us! We will be in touch with')]"

    def contactPage(self):
        self.driver.find_element("xpath", self.xpath_contactPage).click()

    def first_name(self, firstName):
        self.driver.find_element("xpath", self.xpath_first_name).send_keys(firstName)

    def last_name(self, lastName):
        self.driver.find_element("xpath", self.xpath_last_name).send_keys(lastName)

    def enter_email(self, emailId):
        self.driver.find_element("xpath", self.xpath_emailID).send_keys(emailId)

    def enter_comment(self, comment):
        self.driver.find_element("xpath", self.xpath_comment).send_keys(comment)

    def click_botCheckBox(self):
        self.driver.find_element("xpath", self.xpath_botCheckbox).click()

    def click_submit(self):
        self.driver.find_element("xpath", self.xpath_submitBtn).click()

    def thanks_msg(self):
        return self.driver.find_element("xpath", self.xpath_thankyou_msg).text