import pytest
from time import sleep
from Test_xlsx_param.PageObject.LoginPage import Login
from Test_xlsx_param.PageObject.DashBoard_Practice import Dashboard
from Test_xlsx_param.Utilities.test_logs import LogClass
from Utilities_script import ExcelMethods
sheet_names = "Sheet"

@pytest.mark.usefixtures("page")
class Test_login:

    @pytest.mark.parametrize("t_c_no, username, password, condition", ExcelMethods(sheet_names).get_parametrize_list())
    def test_login1(self, t_c_no, username, password, condition):
        self.logger = LogClass().get_logger()

        login = Login(self.driver)
        dashboard_p = Dashboard(self.driver)

        login.username(username)
        login.password(password)
        login.click_submit()
        sleep(2)
        if condition == "+ve":
            if "Logged In Successfully" in dashboard_p.login_msg():
                status = True
            else:
                status = False
        if condition == "-ve":
            if "Your username  invalid!" in login.invalid_msg():
                status = True

            elif "Your password is invalid!" in login.invalid_msg():
                status = True
            else:
                status = False, "Text not found"
        ExcelMethods(sheet_names).update_result_in_excel(t_c_no, status)
        assert status