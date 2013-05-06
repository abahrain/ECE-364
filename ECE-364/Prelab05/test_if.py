#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-03 02:20:01 -0500 (Sun, 03 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab05/test_if.py $
#$Revision: 49798 $

import sys

i=sys.stdin.readline()
num= int(i)
if num <7:
    print "Low value"
elif num >7:
    print "High value"
else:
    print "Neither"

sys.exit(0)

