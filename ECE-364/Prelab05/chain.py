#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-06 15:26:28 -0500 (Wed, 06 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab05/chain.py $
#$Revision: 51225 $

import sys
x=0
p=-1
h=-1
a=[1, 2, 3]
n=sys.argv[1:]
s=sys.stdin.readline()

if len(sys.argv) != 3:
    print "usage: chain <region> <animal>"
    sys.exit(0)

while s:
    t=s.split()
    a[x]=[t[0],[tuple(t[1:3]), tuple(t[2:4]), tuple(t[3:5]), tuple(t[4:6])]]
    x=x+1
    s=sys.stdin.readline()
print a
print "\n"

if n[0] == a[0][0]:
    for i in range (0,len(a[0][1])):
        for w in range (0,len(a[0][1][i])):
                if n[1]==a[0][1][i][w]:
                    p=i
                    h=w+1
    if p>=0 and h>=0:
        print "In the ", n[0], "the", n[1], "is eaten by the ", a[0][1][p][h]
    else:
        print "No chain entry for ", n[1]
elif n[0] == a[1][0]:
    for i in range (0,len(a[1][1])):
        for w in range (0,len(a[1][1][i])):
            if n[1]==a[1][1][i][w]:
                p=i
                h=w+1
    if p>=0 and h>=0:
        print "In the ", n[0], "the", n[1], "is eaten by the ", a[1][1][p][w]
    else:
        print "No chain entry for ", n[1]
elif n[0] == a [2][0]:
    for i in range (0,len(a[2][1])):
        for w in range (0,len(a[2][1][i])):
            if n[1]==a[2][1][i][w]:
                p=i
                h=w+1
    if p>=0 and h>=0:
        print "In the ", n[0], "the", n[1], "is eaten by the ", a[2][1][p][h]
    else:
        print "No chain entry for ", n[1]
else:
    print "Unknown region: ", n[0]

sys.exit(0)
