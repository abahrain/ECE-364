#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-27 19:51:43 -0500 (Wed, 27 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab08/listmod.py $
#$Revision: 53509 $

import sys

sys.argv

listone=raw_input('Enter the first list of numbers: ')
listone=[int(i) for i in listone.split(' ')]
listtwo=raw_input('Enter the second list of numbers: ')
listtwo=[int(i) for i in listtwo.split(' ')]
print "First list: ",listone
print "Second list: ", listtwo

def find_median(a,b):
    mergelist=a+b
    mergelist.sort()
    N=len(mergelist)
    med=mergelist[(N-1)/2]
    print "Merged list: ",mergelist
    print "Median: ",med

find_median(listone,listtwo)

sys.exit(0)
