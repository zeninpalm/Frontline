"""
    Unit test for Http connection establishment ability.
"""

__author__ = 'yiwei'

import unittest
import connections.httpconnection as httpconnection

from connections.httpconnection import VersionNumber
from data_transport.ip_address import IPAddress
from mock import MagicMock

class HttpConnectionTestCase(unittest.TestCase):

    def test_HttpConnectionShouldBeAvailable(self):
        httpConnection = httpconnection.HttpConnection()
        self.assertIsNotNone(httpConnection, "A HttpConnection instance should have been established.")

    def test_HttpConnectionCanSpecifyIPandPort(self):
        destIP = IPAddress()
        destIP.getIpAsString = MagicMock(return_value = '119.75.217.109')
        destPort = 80

        httpConnection = httpconnection.HttpConnection(destIP, destPort)
        self.assertIsNotNone(httpConnection,
                             "A HttpConnection instance should be able to specify destination IP and port.")

    def test_HttpConnectionMaySpecifyIpAndPortLater(self):
        destIP = IPAddress()
        destIP.getIpAsString = MagicMock(return_value = "119.75.217.109")
        destPort = 80

        httpConn = httpconnection.HttpConnection()
        httpConn.destIP = destIP
        httpConn.destPort = destPort

        httpConn1 = httpconnection.HttpConnection(destIP, destPort)
        self.assertEqual(httpConn.destIP.getIpAsString(), httpConn1.destIp.getIpAsString(),
                         "Two instances should contain the same destination IP.")
        self.assertEqual(httpConn.destPort, httpConn.destPort,
                         "Two instances should contain the same destination port.")

    def test_HttpConnectionMaySpecifyVersion(self):
        version = VersionNumber(1, 1)
        httpConn = httpconnection.HttpConnection(versionNumber=version)
        self.assertEqual(httpConn.versionNumber.majorVersion, 1,
                         "Major version number should be 1")
        self.assertEqual(httpConn.versionNumber.minorVersion, 1,
                         "Major version number should be 1")

    def test_HttpConnectionDefaultToBe1point1(self):
        httpConn = httpconnection.HttpConnection()
        self.assertEqual(httpConn.versionNumber.majorVersion, 1, "MajorVersion should default to be 1.")

        minor = httpConn.versionNumber.minorVersion
        #self.assertEuqals(minor, 1, "MinorVersion should default to be 1.")
        self.assertIs(minor, 1, "MinorVersion should be 1.")

if __name__ == '__main__':
    unittest.main()
