import json
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from TestPages.LoginPage import LoginPage
from selenium import webdriver
from pathlib import Path
from datetime import datetime


class Utilities:
    file_open = None

    def __init__(self):
        self.utilities_driver = None
        self.loginpage_obj =None

    @classmethod
    def get_root_directory(cls):
        return str(Path(os.getcwd()).parent)

    @classmethod
    def get_emp_data(cls):
        cls.file_open = open(cls.get_root_directory() + "/Employeedata/Employee_details.json")
        emp_data = json.load(cls.file_open)
        cls.file_open.close()
        return emp_data

    def initialize_driver(self):
        self.utilities_driver = webdriver.Chrome()
        self.utilities_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.utilities_driver.maximize_window()
        return self.utilities_driver

    def login_into_orangehrm(self):
        self.loginpage_obj = LoginPage(self.utilities_driver)
        self.utilities_driver.implicitly_wait(5)
        self.loginpage_obj.enter_username("Admin")
        self.loginpage_obj.enter_password("admin123")
        self.loginpage_obj.click_login_button()

    def take_screenshot(self):
        filename = (datetime.now()).strftime("%d%m%Y %H%M%S")+".png"
        screenshot_folder = "/TestResult/Screenshots/"
        self.utilities_driver.get_screenshot_as_file(self.get_root_directory()+screenshot_folder+filename)

    def take_failed_screenshot(self):
        filename = (datetime.now()).strftime("%d%m%Y %H%M%S") + ".png"
        screenshot_folder = "/TestResult/FailedScreenshots/"
        self.utilities_driver.get_screenshot_as_file(self.get_root_directory() + screenshot_folder + filename)

