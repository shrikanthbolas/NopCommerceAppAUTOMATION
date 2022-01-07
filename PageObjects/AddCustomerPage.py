import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    #locator elements of the add customer page
    lnkCustomers_manin_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomers_sub_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    addNewButton="/html/body/div[3]/div[1]/form[1]/div/div/a"

    #Add Customer Page
    txtEmail_xpath="//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"

    #*****************************************************************************************
    txtcustomerRoles_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    listitemAdministrators_xpath="//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    listitemForumModerators_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    listitemRegistered_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    listitemGuests_xpath = ""
    listitemVendors_xpath = ""

    #click save
    saveButton="//button[@name='save']"





    def __init__(self,driver):
        self.driver = driver

    #Action methods
    def clickOnCustomerMainMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_manin_menu_xpath).click()

    def clickOnCustomerSubMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_sub_menu_xpath).click()

    def clickOnAddNewButton(self):
        self.driver.find_element_by_xpath(self.addNewButton).click()

    def enterEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def eneterPassWord(self,pwd):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(pwd)

    def selectCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role=='Registered':
            self.listitem = self.driver.find_element_by_xpath(self.listitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.listitemAdministrators_xpath)
        elif role=='Forum Moderators':
            self.listitem = self.driver.find_element_by_xpath(self.listitemForumModerators_xpath)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def clickSave(self):
        self.driver.find_element_by_xpath(self.saveButton).click()




