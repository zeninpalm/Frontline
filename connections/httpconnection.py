"""
    httpconnection moudle encapsulates details about establishment and management of http connections
"""
__author__ = 'yiwei'

import  httplib

class IllegalVersionNumber(BaseException):
    pass

#@class_invariant
#always_legal: isLegal(majorVersion, minorVersion)
#@@end
class VersionNumber(object):

    #@requires
    #not_none: majorVersion is not None and minorVersion is not None
    #be_positive: majorVersion > 0 and minorVersion > 0
    #@end
    #
    #@ensures
    #correct_init: majorVersion == majorVersion and minorVersion == minorVersion
    #@end
    def __init__(self, majorVersion, minorVersion):
        if self.isLegal(majorVersion, minorVersion) is False:
            raise IllegalVersionNumber()

        self._majorVersion = majorVersion
        self._minorVersion = minorVersion

    @property
    def majorVersion(self):
        return self._majorVersion
    #

    @property
    def minorVersion(self):
        return  self._minorVersion

    #@requires
    #not_none: majorVersion is not None and minorVersion is not None
    #positive_integers: majorVersion > 0 and minorVersion > 0
    #@end
    #@requires
    #
    def isLegal(self, majorVersion, minorVersion):
        if majorVersion >= 2 or minorVersion >= 3:
            return False
        else:
            return True

    def __cmp__(self, other):
        if self.majorVersion != other.majorVersion:
            return self.majorVersion - other.majorVersion
        else:
            return self.minorVersion - other.minorVersion

class HttpConnection(object):
    """
        Encapsulation of httplib's HttpRequest
    """
    def __init__(self, destIP = None, destPort = None, versionNumber = None):
        if destIP is not None:
            self.__destIPAddress = destIP

        if destPort is not None:
            self.__destPortNumber = destPort

        if versionNumber is not None:
            self.__versionNumber = versionNumber
        else:
            self.__versionNumber = VersionNumber(1, 1)



    @property
    def destIp(self):
        return self.__destIPAddress

    @property
    def destPort(self):
        return self.__destPortNumber

    @property
    def versionNumber(self):
        return self.__versionNumber

    @destIp.setter
    def destIP(self, ip_addr):
        self.__destIPAddress = ip_addr

    @destPort.setter
    def destPort(self, port_num):
        self.__destPortNumber = port_num

    @versionNumber.setter
    def versionNumber(self, newVersion):
        self.__versionNumber = newVersion

