import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.AddCustomerPage import AddCustomer
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()  #Logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("**************** Test_003_AddCustomer *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)  #create object,this time constructor gets called
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** Login successful *******************")

        self.logger.info("**************** Starting Add Customer Test *******************")
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMainMenu()
        time.sleep(2)
        self.addcust.clickOnCustomerSubMenuItem()
        time.sleep(2)
        self.addcust.clickOnAddNewButton()
        time.sleep(2)

        self.logger.info("**************** Providing Customer Info *******************")
        self.email = random_generator() + "@gmail.com"
        self.addcust.enterEmail(self.email)
        self.addcust.eneterPassWord("test123")
        self.addcust.selectCustomerRoles("Forum Moderators")

        #clicking on SAVE button
        self.addcust.clickSave()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))



