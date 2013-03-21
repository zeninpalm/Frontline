__author__ = 'yiwei'

import unittest

from connections.httpconnection import VersionNumber, IllegalVersionNumber
from mock import MagicMock

class testVersionNumber(unittest.TestCase):
    def test_VersionNumberShouldBeAvailable(self):
        version_num = VersionNumber(1, 1)
        self.assertIsNotNone(version_num,
                             "A VersionNumber instance should be created.")

    def test_VersionNumberShouldBeLegal(self):
        majorVer1 = 1
        majorVer2 = 2

        minorVer1 = 1
        minorVer2 = 2
        minorVer3 = 3

        version_num = VersionNumber(majorVer1, minorVer1)
        self.assertIsNotNone(version_num, "Version 1.1 should be legal.")

        version_num = VersionNumber(majorVer1, minorVer2)
        self.assertIsNotNone(version_num, "Version 1.2 should be legal.")

        self.assertRaises(IllegalVersionNumber, VersionNumber, majorVer1, minorVer3)
        self.assertRaises(IllegalVersionNumber, VersionNumber, majorVer2, minorVer1)
        self.assertRaises(IllegalVersionNumber, VersionNumber, majorVer2, minorVer2)
        self.assertRaises(IllegalVersionNumber, VersionNumber, majorVer2, minorVer3)

    def test_VersionNumberShouldBeIntegerOrder(self):
        version_num1 = VersionNumber(1, 2)
        version_num2 = VersionNumber(1, 1)

        self.assertGreater(version_num1, version_num2,
                           "Version 1.2 should be greater than 1.1")

if __name__ == '__main__':
    unittest.main()
