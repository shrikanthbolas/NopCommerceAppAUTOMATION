import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/TestData.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_Login_ddt(self,setup):
        self.logger.info("**************** Test_002_DDT_Login *******************")
        self.logger.info("**************** Verifying Login DDT test *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)  #create object,this time constructor gets called

        #Get row cpunt from xlutils
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in a Excel:", self.rows)

        #Create empty list variable
        list_status=[]

        for r in range(2,self.rows+1):     #2 means starting from second row and +1 means including last row
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)
            self.driver.maximize_window()
            time.sleep(5)
            act_title = self.driver.title
            print('print shrikanth ------->>>>',act_title)
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("**************** Login test is passed *******************")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("**************** Login test is failed *******************")
                    self.lp.clickLogout()
                    list_status.append("Pass")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("**************** Login test is failed *******************")
                    list_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("**************** Login test is passed *******************")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("**************** Login DDT test is passed *******************")
            self.driver.close()
            assert True
        else:
            self.logger.info("**************** Login DDT test is failed *******************")
            self.driver.close()
            assert False

        self.logger.info("**************** End of Login DDT test  *******************")
        self.logger.info("**************** Completed Test_002_DDT_Login *******************")






















