from Utilities.test_logs import LogClass

logger = LogClass().get_logger()
class Login(LogClass):

    def __init__(self, driver):

        # super().__init__()
        self.driver = driver
        self.xpath_username = "username"
        self.xpath_password = "password"
        self.xpath_submitBtn = "submit"
        self.xpath_invalidMsg = "//div[@id='error']"
        # self.logger = LogClass().get_logger()

    def username(self, username):
        # logger = self.getLogs()
        self.driver.find_element("name", self.xpath_username).send_keys(username)
        logger.info("Login with username: %s", username)

    def password(self, password):
        self.driver.find_element("name", self.xpath_password).send_keys(password)
        logger.info("Login with username: %s", password)

    def click_submit(self):
        self.driver.find_element("id", self.xpath_submitBtn).click()

    def invalid_msg(self):
        logger.error("Error: Invalid credentials")
        return self.driver.find_element("xpath", self.xpath_invalidMsg).text
