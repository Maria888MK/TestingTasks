import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def selenium_browser(request):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()

