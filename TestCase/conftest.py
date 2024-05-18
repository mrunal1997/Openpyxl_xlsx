from selenium import webdriver
import pytest, configparser

parser = configparser.ConfigParser()
parser.read(filenames="Utilities/input.properties")


@pytest.fixture
def page(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get(parser.get("Url", "page_url"))
    request.cls.driver.maximize_window()
    yield
    request.cls.driver.quit()


def pytest_html_report_title(report):
    report.title = "My Selenium web application testing!"
