#! /usr/bin/env python2.6
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$

import sys

count=0
sum=0
avg=0
min=0
max=0
a=[1]
n=sys.argv[1:]
m=n[0].lower()
s=sys.stdin.readline()
s=s.rstrip()

if len(sys.argv) != 2:
    print "usage: expr_stats.py <username>"
    sys.exit(1)

while s:
    t=s.split("/")
    a.append(t)
    s=sys.stdin.readline()
    s=s.rstrip()

for i in range(1,len(a)):
    if m == a[i][0]:
        for o in range(1,len(a[i])-1):
            count=count+1
            sum=sum+float(a[i][o])
            if float(a[i][o]) > max:
                max=float(a[i][o])
            if float(a[i][o]) < min:
                min=float(a[i][o])
avg=sum/count

print "%s: sum= %.2f, count= %d, avg= %.2f, min= %.2f, max= %.2f" % (n[0],sum,count,avg,min,max,)

sys.exit(0)
