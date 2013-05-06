#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-03 02:59:55 -0500 (Sun, 03 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab05/test_rwhile.py $
#$Revision: 49807 $

import sys

sum=0
n=sys.argv[1]
i=int(n[0])
a=0

while a<i+1:
    sum = sum + int(a)
    a += 1 
print "The sum is: %d" % (sum,)

sys.exit(0)
