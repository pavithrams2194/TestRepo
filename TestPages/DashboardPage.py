from selenium.webdriver.common.by import By

from Utility_files import Driverwait


class DashboardPage:
    def __init__(self,driver):
        self.dashboard_locator = "//h6[text()='Dashboard']"
        self.dashboard_driver = driver

    def check_is_dashboard_page(self):
        Driverwait.driver_wait_until_visible(self.dashboard_driver,5,self.dashboard_locator)
        self.dashboard_driver.find_element(By.XPATH,self.dashboard_locator)
        return True
