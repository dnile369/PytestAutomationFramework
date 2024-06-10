import pandas as pd
from selenium.webdriver.common.by import By


class nse_website:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        print(self.driver.title)

    def get_each_stock_details(self):
        pass

