import pytest
from utilities.nse import nse_website
from utilities.YahooFinance import Yahoo_Finance
import time


@pytest.mark.usefixtures('setup')
class Test_001_info:

    @pytest.mark.nse
    def test_nse(self):
        self.driver.maximize_window()
        self.driver.get("https://www.nseindia.com/")
        self.driver.implicitly_wait(5)
        web = nse_website(self.driver)
        web.get_title()

        web.get_each_stock_details()
        time.sleep(60)

    @pytest.mark.yahoo
    def test_yahoo_finance(self):
        self.driver.maximize_window()
        self.driver.get("https://finance.yahoo.com/")
        self.driver.implicitly_wait(5)
        web = Yahoo_Finance(self.driver)
        web.get_title()

        web.get_each_stock_details()

