#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-03 02:46:58 -0500 (Sun, 03 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab05/test_rfor1.py $
#$Revision: 49805 $

import sys

sum=0
n=sys.argv[1]
i=int(n[0])
x=range(1,i+1)

for arg in x:
    sum = sum + int(arg)

print "The sum is: %d" % (sum,)

sys.exit(0)
