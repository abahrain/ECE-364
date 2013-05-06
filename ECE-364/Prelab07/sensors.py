#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-21 02:30:14 -0500 (Thu, 21 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab07/sensors.py $
#$Revision: 52917 $

import sys
import os
import math

mi=0
ma=0
s=0
a=0
dev=0
d={}
n=sys.argv[1:]

if len(sys.argv) != 2:
    print "Usage: sensors.py <inputfile>"
    sys.exit(1)
if not os.access(n[0],os.R_OK):
    print "%s is not readable" % (n[0],)
    sys.exit(1)

InFile = open(n[0], "r")

for line in InFile:
    line=line.split(":,")
    
    for i in range(1,len(line)):
         s=s+float(line[i])
         a=s/i
         if line[i] < mi:
             mi=line[i]
         if line[i] > ma:
             ma=line[i]

    if d.has_key(line[0]):
        d[line[0]]=[s,a,mi,ma,s]
    else:
        b={line[0]:[s,a,mi,ma,s]}
        d.update(b)
    


InFile.close()

for keys in d:
    print "%s: min=%.3f, max=%.3f, sum=%.3f, avg=%.3f, stdev=%.3f" % (keys,d.get(keys)[2],d.get(keys)[3], d.get(keys)[0], d.get(keys)[1], d.get(keys)[4],)
sys.exit(0)
