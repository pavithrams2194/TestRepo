import time

import pyautogui
from selenium.webdriver.common.by import By

from Utility_files import Driverwait
from Utility_files.Utilities import Utilities


class AddEmployeePage:

    def __init__(self,driver):
        self.firstname_locator = "firstName"
        self.lastname_locator = "lastName"
        self.middlename_locator = "middleName"
        self.plus_sign_locator = "//button[@class = 'oxd-icon-button oxd-icon-button--solid-main employee-image-action']"
        self.save_button_locator = "//button[text() = ' Save ']"
        self.successmsg_locator="//*[text()='Successfully Saved']"
        self.addemployee_driver = driver
        self.emp_data = Utilities.get_emp_data()

    def enter_firstname(self):
        self.addemployee_driver.find_element(By.NAME, self.firstname_locator).send_keys(self.emp_data.get("firstname"))

    def enter_middlename(self):
        self.addemployee_driver.find_element(By.NAME, self.middlename_locator).send_keys(self.emp_data.get("middlename"))

    def enter_lastname(self):
        self.addemployee_driver.find_element(By.NAME, self.lastname_locator).send_keys(self.emp_data.get("lastname"))

    def add_photo(self):
        Driverwait.driver_wait_until_clickable(self.addemployee_driver,10,self.plus_sign_locator)
        self.addemployee_driver.find_element(By.XPATH,self.plus_sign_locator).click()
        time.sleep(3)
        pyautogui.write(Utilities.get_root_directory()+"\Employeedata\photo.jpeg")
        pyautogui.press('enter')
        time.sleep(3)

    def click_save_button(self):
        self.addemployee_driver.find_element(By.XPATH,self.save_button_locator).click()

    def check_successmsg_display(self):
        self.addemployee_driver.find_element(By.XPATH,self.successmsg_locator)
        return True