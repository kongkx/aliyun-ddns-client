#!/usr/bin/env python
# coding=utf-8
"""
 Copyright (C) 2010-2013, Ryan Fan <reg_info@126.com>

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Library General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
"""
import socket
import sys
from urllib2 import Request, urlopen, URLError
from datetime import datetime

class DDNSUtils:
    def __init__(self, debug):
        self.debug = debug

    @staticmethod
    def err(str):
        sys.stderr.write("{0}\t[ERROR]\t{1}\n".format(DDNSUtils.getCurrentTime(), str))

    @staticmethod
    def info(str):
        sys.stdout.write("{0}\t[INFO]\t{1}\n".format(DDNSUtils.getCurrentTime(), str))

    @staticmethod
    def err_and_exit(str):
        sys.stderr.write("{0}\t[ERROR]\t{1}\n".format(DDNSUtils.getCurrentTime(), str))
        sys.exit(1)

    def getCurrentPublicIP(self):
        """
        Get current public IP

        @return None or ip string
        """
        ip = None
        try:
            r = urlopen("http://members.3322.org/dyndns/getip")
            ip = r.read().rstrip("\n")
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
                print e.read()
        # return '192.168.1.1'
        return ip

    def getCurrenDNSResolvedIP(self, domainName, subDomainName):
        """
        Get current ip resolved by DNS server,
        Due for local DNS cache, it may be not synced to the one recorded in DNS service provider
        """
        ip = None
        try:
            ip = socket.gethostbyname("{0}.{1}".format(subDomainName,domainName))
        except Exception,e:
            self.err("network problem:{0}".format(e))

        return ip

    @staticmethod
    def getCurrentTime():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
