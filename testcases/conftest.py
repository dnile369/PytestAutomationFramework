import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# from selenium.webdriver.firefox.service import Service


# This code is for Browser Invocation.
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service())
    request.cls.driver = driver
