#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-03-03 19:10:52 -0500 (Sun, 03 Mar 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab09/ipfun.py $
#$Revision: 53793 $

import sys
import re

n=sys.argv[1:]

fp=open(sys.argv[1])

for test in fp:
    line=test.split(":")
    test=test.split("\n")

    if re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",line[0]):
        
        if re.match("(0-1)0(0-2)(0-4)|(0-1)(\d)(\d)(\d)|(\d)(\d)|(\d)",line[1]):
            print "%s - Valid (root privileges required)" % (test[0])
        else:
            print "%s - Valid" % (test[0])
    else:
        print "%s - Invalid IP Address" % (test[0])

sys.exit(0)
