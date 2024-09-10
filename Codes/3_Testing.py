import unittest
from datetime import datetime

class TestStockData(unittest.TestCase):

    def test_data_valid(self):
        # Define test inputs
        open_price = 100.5
        high_price = 105.0
        low_price = 98.5
        close_price = 102.0
        volume = 10000
        instrument = "AAPL"
        date_time = datetime(2024, 9, 8)

        # Assert that all fields meet the data type requirements
        self.assertIsInstance(open_price, float)
        self.assertIsInstance(high_price, float)
        self.assertIsInstance(low_price, float)
        self.assertIsInstance(close_price, float)
        self.assertIsInstance(volume, int)
        self.assertIsInstance(instrument, str)
        self.assertIsInstance(date_time, datetime)

if __name__ == '__main__':
    unittest.main()
