import datetime
import unittest

from endofday.utils import eod


class TestEod(unittest.TestCase):

    def test_eod(self):
        """Test eod for end of the day on a couple of dates"""
        self.assertEqual(
            eod(datetime.datetime(2017, 12, 1, 17, 30)),
            '0'
        )
        self.assertEqual(
            eod(datetime.datetime(2001, 6, 4, 17, 30)),
            '0'
        )

    def test_eod_start(self):
        """Test eod for start of the day on a couple of dates"""
        self.assertEqual(
            eod(datetime.datetime(2017, 12, 1, 9, 0)),
            '510'
        )
        self.assertEqual(
            eod(datetime.datetime(2001, 6, 4, 9, 0)),
            '510'
        )



if __name__ == '__main__':
    unittest.main()
