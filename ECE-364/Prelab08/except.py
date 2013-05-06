#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-27 21:06:54 -0500 (Wed, 27 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab08/except.py $
#$Revision: 53517 $

import sys

sys.argv
list=[]
sum=0

input=raw_input("Please enter some values: ")

for i in input.split(' '):
    try:
        list.append(int(i))
    except ValueError:
        try:
            list.append(float(i))
        except ValueError:
            pass

for i in list:
    sum=sum+i

print "The sum is: %.1f" % (sum,)
sys.exit(0)
