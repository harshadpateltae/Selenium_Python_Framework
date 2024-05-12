import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from utilities import common
from utilities.common import Common
from utilities.json_parser import JsonParser
from utilities.readProperties import ReadConfig


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        test_name = request.node.name
        # driver.save_screenshot(".\\Screenshots\\" + test_name + ".png")  # Screenshot
        screenshot_path = f"./Screenshots/{test_name}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def setup(request):
    global driver
    if (ReadConfig.getCommonInfo("browser") == "chrome"):
        # service_obj = Service("C://drivers//chromedriver.exe")
        options = Options()
        # Add specific arguments to the ChromeOptions object
        options.add_argument("--disable-extensions")
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")  # Disable sandbox mode.
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")  # Disable browser notifications.
        options.add_argument("--disable-popup-blocking")  # Disable popup blocking.
        options.add_argument('--start-maximized')  # Maximize the window when the browser starts.
        driver = webdriver.Chrome(options=options)
        request.cls.driver = driver

        yield
        driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# # Hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config.metadata['Project Name'] = 'Amazon'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester'] = 'Harshad'
#
# # Hook for deleting/Modifying Environment info in HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
