#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-07 11:09:56 -0500 (Thu, 07 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab05/transpose.py $
#$Revision: 51288 $

import sys

x=0
a=[]
n=sys.argv[1:]
s=sys.stdin.readline()

if len(sys.argv) != 3:
    print "usage: transpose.py <nrows> <ncols>"
    sys.exit(1)
if n[0] <0 or n[1] <0:
    print "error: invalid dimensions"
    sys.exit(1)

while s:
    t=s.split()
    a.append(t)
    s=sys.stdin.readline()

if int(n[0]) != len(a):
    print "Invalid number of rows."
    sys.exit(2)
elif int(n[1]) != len(a[0]):
    print "Invalid number of columns."
    sys.exit(2)
for t in range(0,len(a[0])):
    for i in range(0,len(a)):
        print "%.2f" % (float(a[i][t]),),
    print ""

sys.exit(0)
