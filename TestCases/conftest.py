import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
        print("Launching chrome browser")
    elif browser=='firefox':
        driver=webdriver.Firefox()
    else:
        driver = webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
    return driver

def pytest_addoption(parser):       #This method will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   #This method will return the browser value to setup method
    return request.config.getoption("--browser")

##############PyTest HTML Reports
#It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Shrikanth K R'

#It is hook for Delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)

