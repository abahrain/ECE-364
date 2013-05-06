#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-27 22:29:54 -0500 (Wed, 27 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab08/parse.py $
#$Revision: 53537 $

import sys

n=sys.argv[1:]
sum=0
avg=0

if len(sys.argv) != 2:
    print "Usage: parse.py <filename>"
    sys.exit(1)

try:
    fp = open(sys.argv[1], "r")
except IOError as e:
    print "%s is not a readable file" % (sys.argv[1],)

for line in fp:
    list=[]
    outstring=[]
    line=line.split(' ')

    for i in line:
        try:
            list.append(int(i))
        except ValueError:
            outstring.append(i),

    for i in list:
        sum=float(sum+i)
        avg=sum/len(list)
    
    if avg > 0:
        print("%.3f ") % (avg,),
        for t in outstring:
            print("%s") % (t,),
        print("")
    else:
        for t in outstring:
            print("%s") % (t,),

sys.exit(0)
