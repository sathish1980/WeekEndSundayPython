import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from PytestConcepts.Testdata import Testdata


@pytest.fixture(scope="class")
def add():
    # return 2+3
    print("Before")
    yield
    print("end of mehtod")

@pytest.fixture()
def dataload():
	return["sathish","kumar","1990"]

@pytest.fixture(params=["chrome","firefox","IE"])
def browserName(request):
	return request.param

@pytest.fixture(params=[("chrome","sathishkumar","password"),("firefox","sathish","kumar"),("IE","thirdvalue")])
def mutidata(request):
	return request.param

@pytest.fixture(scope="class")
def BrowserLaunch(request):
    web = webdriver.ChromeOptions()
    web.add_argument("--start-maximized")
    web.add_argument("--incognito")
    web.add_argument("--disable-notifications")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def FBUsername():
	return["kumar.sathish189@gmail.com","Admin@123"]

@pytest.fixture(params=[("kumar.sathish189@gmail.com","Admin@123"),("kumar.sathish189@gmail.com","Admin@123"),("kumar.sathish189@gmail.com","Admin@123")])
def mutidataFbLogin(request):
	return request.param

@pytest.fixture(params=Testdata.credential_excel_dic)
def fbloginvaliddataFromExecl(request):
    return request.param


