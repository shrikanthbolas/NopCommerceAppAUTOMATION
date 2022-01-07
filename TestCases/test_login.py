import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("**************** Test_001_Login *******************")
        self.logger.info("**************** Verifying Home Page Title *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************** Home Page Title test is passed *******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**************** Home Page Title test is failed *******************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self,setup):
        self.logger.info("**************** Verifying Login test *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)  #create object,this time constructor gets called
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("**************** Login test is passed *******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.logger.error("**************** Login test is failed *******************")
            assert False

