from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import openpyxl


class Yahoo_Finance:
    def __init__(self, driver):
        self.driver = driver
        self.stock_name = None
        self.StockName = []
        self.c_price = []
        self.day_range = []
        self.week_52_range = []
        self.peRatio = []
        self.eps = []

    def get_title(self):
        print(self.driver.title)

    def get_each_stock_details(self):
        stock_list_df = pd.read_csv("TestData/stock_list.csv")
        for stock_index in range(len(stock_list_df)):
            self.stock_name = stock_list_df.loc[stock_index, "StockNames"]
            self.sending_values()
            try:
                self.fetch_values()

            except NoSuchElementException:
                print(f"Details of {self.stock_name} is not present")
                continue

            self.driver.back()
        self.create_df()

    def sending_values(self):
        self.driver.find_element(By.CSS_SELECTOR, "#ybar-sbq").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#ybar-sbq").send_keys(self.stock_name)
        self.driver.find_element(By.XPATH, "//button[@id='ybar-search']").click()

    def fetch_values(self):
        self.StockName.append(self.driver.find_element(By.CSS_SELECTOR, ".container.svelte-3a2v0c.paddingRight").text)
        self.c_price.append(self.driver.find_element(By.CSS_SELECTOR, ".livePrice.svelte-mgkamr").text)
        self.day_range.append(self.driver.find_element(By.XPATH,
                                                       """//span[@class='label svelte-tx3nkj']
                                                       [text()="Day's Range"]/following::span[1]""").text)
        self.week_52_range.append(self.driver.find_element(By.XPATH,
                                                           """//span[@class='label svelte-tx3nkj']
                                                       [text()="52 Week Range"]/following::span[1]""").text)
        self.peRatio.append(self.driver.find_element(By.XPATH,
                                                     """//span[@class='label svelte-tx3nkj']
                                                       [text()="PE Ratio (TTM)"]/following::span[1]""").text)
        self.eps.append(self.driver.find_element(By.XPATH,
                                                 """//span[@class='label svelte-tx3nkj']
                                                       [text()="EPS (TTM)"]/following::span[1]""").text)

    def create_df(self):
        req_dict = {
            "Stock Name": self.StockName,
            "Current Price": self.c_price,
            "Day's Range": self.day_range,
            "52 Week Range": self.week_52_range,
            "PE Ratio": self.peRatio,
            "EPS": self.eps
        }

        req_df = pd.DataFrame(req_dict)
        req_df.to_excel("C:\\Users\\niles\\PycharmProjects\\Stock_Information\\Reports\\info.xlsx", index=False)
        req_df.to_csv("C:\\Users\\niles\\PycharmProjects\\Stock_Information\\Reports\\info.csv", index=False)
