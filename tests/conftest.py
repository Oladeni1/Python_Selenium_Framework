

import pytest

# Initialisation (Before & after class):
from selenium import webdriver
# start
# Passing different browser at the runtime from command line: ===>
# Resources location :"https://docs.pytest.org/en/latest/example/simple.html"
# command to run from cmd: ===>  py.test --browser_name chrome or firefox


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
# end


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")  # to use from cmd line
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\chromedriver.exe")
        driver.maximize_window()
        #driver.get("https://rahulshettyacademy.com/angularpractice/")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\olatu\\PycharmProjects1\\PythonProject1\\Browsers\\geckodriver.exe")
        driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver     # use to connect with other driver(s)
    yield
    driver.close()
