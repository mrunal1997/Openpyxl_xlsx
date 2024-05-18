class Dashboard:
    def __init__(self, driver):
        self.driver = driver

        self.xpath_logged_in = "//h1[normalize-space()='Logged In Successfully']"
        self.xpath_practicePage = "//a[normalize-space()='Practice']"
        self.xpath_exception_test = "//a[normalize-space()='Test Exceptions']"
        self.xpath_editBtn = "//button[@id='edit_btn']"
        # self.xpath_enterText = "//input[@value='Pizza']"
        self.xpath_saveBtn = "//button[@id='save_btn']"
        self.xpath_addBtn = "//button[@id='add_btn']"
        self.xpath_message = "//div[@id='confirmation']"
        self.xpath_removeBtn = "//button[@id='remove_btn']"

    def login_msg(self):
        return self.driver.find_element("xpath", self.xpath_logged_in).text

    def practicePage(self):
        self.driver.find_element("xpath", self.xpath_practicePage).click()

    def exceptionTest(self):
        self.driver.find_element("xpath", self.xpath_exception_test).click()

    def edit_text_btn(self):
        self.driver.find_element("xpath", self.xpath_editBtn).click()
    #
    # def enterTextBox(self, entertext):
    #     self.driver.find_element("xpath", self.xpath_enterText).send_keys(entertext)

    def save_btn(self):
        self.driver.find_element("xpath", self.xpath_saveBtn).click()

    def add_btn(self):
        self.driver.find_element("xpath", self.xpath_addBtn).click()

    def status(self):
        return self.driver.find_element("xpath", self.xpath_message).text

    def remove_btn(self):
        self.driver.find_element("xpath", self.xpath_removeBtn).click()
