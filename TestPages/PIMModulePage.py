from selenium.webdriver.common.by import By


class PIMModulePage:

    def __init__(self,driver):
        self.PIMModule_driver = driver
        self.PIMModule_locator = "//*[@class = 'oxd-text oxd-text--span oxd-main-menu-item--name' and text()='PIM']"
        self.add_button_locator = "//button[text()=' Add ']"
        self.emp_list_locator = "//*[@class='oxd-table-body']//div"
        self.emp_delete_locator = "//div[@class='oxd-table-cell-actions']//button//i[@class='oxd-icon bi-trash']"
        self.delete_successfull_locator = "//*[text()='Successfully Deleted']"
        self.yes_button_locator = "//button[contains(.,'Delete')]"

    def click_pim_module(self):
        self.PIMModule_driver.find_element(By.XPATH,self.PIMModule_locator).click()

    def click_add_button(self):
        self.PIMModule_driver.find_element(By.XPATH,self.add_button_locator).click()

    def select_employee(self):
        self.PIMModule_driver.find_element(By.XPATH,self.emp_list_locator).click()

    def delete_employee(self):
        self.PIMModule_driver.find_element(By.XPATH,self.emp_delete_locator).click()
        self.PIMModule_driver.find_element(By.XPATH,self.yes_button_locator).click()

    def check_successfull_deletionmsg(self):
        self.PIMModule_driver.find_element(By.XPATH,self.delete_successfull_locator)
        return True
