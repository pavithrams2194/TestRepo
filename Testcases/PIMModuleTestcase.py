import unittest

from selenium.common import NoSuchElementException

from TestPages.AddEmployeePage import AddEmployeePage
from TestPages.PIMModulePage import PIMModulePage
from TestPages.PersonalDetailsPage import PersonalDetailsPage
from Utility_files.Utilities import Utilities


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.utility_obj = Utilities()
        self.driver = self.utility_obj.initialize_driver()
        self.utility_obj.login_into_orangehrm()
        self.pim_module_obj = PIMModulePage(self.driver)
        self.add_emp_obj = AddEmployeePage(self.driver)
        self.personal_det_obj=PersonalDetailsPage(self.driver)

    #Testcase ID:TC_PIM_01
    #Add a new employee in PIM Module
    def test_add_new_employee(self):
        self.pim_module_obj.click_pim_module()
        self.pim_module_obj.click_add_button()
        self.add_emp_obj.enter_firstname()
        self.add_emp_obj.enter_middlename()
        self.add_emp_obj.enter_lastname()
        self.add_emp_obj.add_photo()
        self.add_emp_obj.click_save_button()
        self.assertEqual(True, self.add_emp_obj.check_successmsg_display())  # add assertion here
        self.assertEqual(True, self.personal_det_obj.check_personaldetails_display())
        self.personal_det_obj.enter_nickname()
        self.personal_det_obj.enter_driverlicense()
        self.personal_det_obj.enter_driverlicense_expdate()
        self.personal_det_obj.select_nationality()
        self.personal_det_obj.select_maritalstatus()
        self.personal_det_obj.enter_date_of_Birth()
        self.personal_det_obj.select_male()
        self.personal_det_obj.select_smoker()
        self.personal_det_obj.click_save()
        self.assertEqual(True, self.personal_det_obj.check_successmsg_display())
        self.utility_obj.take_screenshot()

    # Testcase ID:TC_PIM_02
    #Modify employee detail in PIM module
    def test_modify_emp_detail(self):
        self.pim_module_obj.click_pim_module()
        self.pim_module_obj.select_employee()
        self.assertEqual(True, self.personal_det_obj.check_personaldetails_display())
        self.personal_det_obj.enter_nickname()
        self.personal_det_obj.click_save()
        self.assertEqual(True,self.personal_det_obj.check_successmsg_display())
        self.personal_det_obj.select_bloodtype()
        self.personal_det_obj.click_save_cus_fields()
        self.assertEqual(True,self.personal_det_obj.check_successmsg_display())
        self.utility_obj.take_screenshot()

    # Testcase ID:TC_PIM_03
    # Delete employee in PIM module
    def test_delete_emp_detail(self):
        try:
            self.pim_module_obj.click_pim_module()
            self.pim_module_obj.delete_employee()
            self.assertEqual(True, self.pim_module_obj.check_successfull_deletionmsg())
            self.utility_obj.take_screenshot()
        except NoSuchElementException:
            self.utility_obj.take_failed_screenshot()
            self.assertEqual(True,False)




