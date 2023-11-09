import unittest
from TestPages.DashboardPage import DashboardPage
from TestPages.LoginPage import LoginPage
from Utility_files.Utilities import Utilities


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.utility_obj = Utilities()
        self.driver = self.utility_obj.initialize_driver()
        self.loginpage_obj = LoginPage(self.driver)
        self.dashboardpage_obj = DashboardPage(self.driver)

    #Testcase Id:Tc_Login_1
    #Test Successfull employee login to orangeHRM portal
    def test_successfull_login(self):

        self.loginpage_obj.enter_username("Admin")
        self.loginpage_obj.enter_password("admin123")
        self.loginpage_obj.click_login_button()
        self.assertEqual(True, self.dashboardpage_obj.check_is_dashboard_page())
        self.utility_obj.take_screenshot()

    # Testcase Id:Tc_Login_2
    # Test Invalid employee login to orangeHRM portal
    def test_invalid_password(self):

        self.loginpage_obj.enter_username("Admin")
        self.loginpage_obj.enter_password("Invalid Password")
        self.loginpage_obj.click_login_button()
        self.assertEqual(True,self.loginpage_obj.check_invalid_credentials_display())
        self.utility_obj.take_screenshot()

    def test_invalid_username(self):
        self.loginpage_obj.enter_username("Admin123")
        self.loginpage_obj.enter_password("admin123")
        self.loginpage_obj.click_login_button()
        self.assertEqual(True, self.loginpage_obj.check_invalid_credentials_display())
        self.utility_obj.take_screenshot()
    #
    def test_invalid_credentials(self):
        self.loginpage_obj.enter_username("Admin123")
        self.loginpage_obj.enter_password("Invalid Password")
        self.loginpage_obj.click_login_button()
        self.assertEqual(True, self.loginpage_obj.check_invalid_credentials_display())
        self.utility_obj.take_screenshot()

    def test_username_required(self):
        self.loginpage_obj.enter_password("admin123")
        self.loginpage_obj.click_login_button()
        self.assertEqual(True, self.loginpage_obj.check_username_required_display())
        self.utility_obj.take_screenshot()

    def test_password_required(self):
        self.loginpage_obj.enter_username("Admin")
        self.loginpage_obj.click_login_button()
        self.assertEqual(True, self.loginpage_obj.check_password_required_display())
        self.utility_obj.take_screenshot()

    def test_both_required(self):
        self.loginpage_obj.click_login_button()
        self.assertEqual(True, self.loginpage_obj.check_password_required_display())
        self.assertEqual(True,self.loginpage_obj.check_username_required_display())
        self.utility_obj.take_screenshot()


if __name__ == '__main__':
    unittest.main()
        


