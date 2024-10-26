import pytest
from selenium import webdriver
import os


@pytest.fixture()
def init_driver(request):
    pass
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    driver = webdriver.Remote(command_executor='http://chrome_selenium:4444/wd/hub', options=options)
    driver.get(os.getenv('URL'))
    request.cls.driver = driver

    yield 
    driver.quit()
