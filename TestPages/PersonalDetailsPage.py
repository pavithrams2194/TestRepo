import time

from selenium.webdriver.common.by import By

from Utility_files import Driverwait
from Utility_files.Utilities import Utilities


class PersonalDetailsPage:

    def __init__(self,driver):
        self.personaldetails_driver = driver
        self.personal_details_locator = "//*[@class='oxd-text oxd-text--h6 orangehrm-main-title' and text()='Personal Details']"
        self.nickname_locator = "//label[text()='Nickname']//following::div//child::input"
        self.driverlicense_locator = "//label[contains(.,'License Number')]//following::div//child::input"
        self.driverlicense_ExpDate_locator = "//label[text()='License Expiry Date']//following::div//child::input"
        self.nationality_locator = "//label[text()='Nationality']//following::div//child::div"
        self.select_Indian_locator = "//div[@role='option']//child::span[text()='Indian']"
        self.maritial_status_locator = "//label[text()='Marital Status']//following::div//child::div"
        self.select_single_locator = "//div[@role='option']//child::span[text()='Single']"
        self.DOB_locator = "//label[text()='Date of Birth']//following::div//div//div//input"
        self.male_locator = "//*[text()='Male']"
        self.smoker_locator = "//input[@type='checkbox']//following-sibling::span"
        self.save_locator = "//*[@class='oxd-form-actions']//p//following-sibling::button[text()=' Save ']"
        self.blood_type_locator = "//label[text()='Blood Type']//following::div//div"
        self.blood_type_select_locator = "//div[@role='option']//span[text()='O+']"
        self.save_custom_fields_locator = "//div[@class='orangehrm-custom-fields']//button[@type='submit' and text()=' Save ']"
        self.successmsg_locator = "//*[text()='Successfully Updated']"
        self.emp_data = Utilities.get_emp_data()


    def enter_nickname(self):
        time.sleep(5)
        self.personaldetails_driver.find_element(By.XPATH, self.nickname_locator).send_keys(self.emp_data.get("nickname"))

    def enter_driverlicense(self):
        self.personaldetails_driver.find_element(By.XPATH, self.driverlicense_locator).send_keys(self.emp_data.get("driverLicense"))

    def enter_driverlicense_expdate(self):
        self.personaldetails_driver.find_element(By.XPATH, self.driverlicense_ExpDate_locator).send_keys(self.emp_data.get("Dlexpirydate"))

    def select_nationality(self):
        self.personaldetails_driver.find_element(By.XPATH,self.nationality_locator).click()
        self.personaldetails_driver.find_element(By.XPATH,self.select_Indian_locator).click()

    def select_maritalstatus(self):
        self.personaldetails_driver.find_element(By.XPATH,self.maritial_status_locator).click()
        self.personaldetails_driver.find_element(By.XPATH,self.select_single_locator).click()

    def enter_date_of_Birth(self):
        self.personaldetails_driver.find_element(By.XPATH,self.DOB_locator).send_keys(self.emp_data.get("DOB"))

    def select_male(self):
        self.personaldetails_driver.find_element(By.XPATH,self.male_locator).click()

    def select_smoker(self):
        self.personaldetails_driver.find_element(By.XPATH,self.smoker_locator).click()

    def click_save(self):
        Driverwait.driver_wait_until_clickable(self.personaldetails_driver,10,self.save_locator)
        self.personaldetails_driver.find_element(By.XPATH,self.save_locator).click()

    def select_bloodtype(self):
        self.personaldetails_driver.find_element(By.XPATH,self.blood_type_locator).click()
        self.personaldetails_driver.find_element(By.XPATH,self.blood_type_select_locator).click()

    def click_save_cus_fields(self):
        self.personaldetails_driver.find_element(By.XPATH,self.save_custom_fields_locator).click()

    def check_successmsg_display(self):
        self.personaldetails_driver.find_element(By.XPATH,self.successmsg_locator)
        return True

    def check_personaldetails_display(self):
        Driverwait.driver_wait_until_visible(self.personaldetails_driver,10,self.personal_details_locator)
        return True

