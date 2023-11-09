import time

from selenium.webdriver.common.by import By

from Utility_files import Driverwait


class LoginPage:

    def __init__(self,driver):
        self.username_locator = "//*[@name='username']"
        self.password_locator = "//*[@name='password']"
        self.login_button_locator = "//button[text()=' Login ']"
        self.invalid_credentials_locator = "//*[text()='Invalid credentials']"
        self.username_required_locator = "//input[@name='username']//following::span[text()='Required']"
        self.password_required_locator = "//input[@name='password']//following::span[text()='Required']"
        self.loginpage_driver = driver

    def enter_username(self,username_text):
        Driverwait.driver_wait_until_visible(self.loginpage_driver,5,self.username_locator)
        self.loginpage_driver.find_element(By.XPATH,self.username_locator).send_keys(username_text)

    def enter_password(self,password_text):
        Driverwait.driver_wait_until_visible(self.loginpage_driver,5,self.password_locator)
        self.loginpage_driver.find_element(By.XPATH, self.password_locator).send_keys(password_text)

    def click_login_button(self):
        Driverwait.driver_wait_until_visible(self.loginpage_driver,5,self.login_button_locator)
        self.loginpage_driver.find_element(By.XPATH,self.login_button_locator).click()

    def check_invalid_credentials_display(self):
        Driverwait.driver_wait_until_visible(self.loginpage_driver,5,self.invalid_credentials_locator)
        self.loginpage_driver.find_element(By.XPATH,self.invalid_credentials_locator)
        return True

    def check_username_required_display(self):
        self.loginpage_driver.find_element(By.XPATH,self.username_required_locator)
        return True

    def check_password_required_display(self):
        self.loginpage_driver.find_element(By.XPATH,self.password_required_locator)
        return True


