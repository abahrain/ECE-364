#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-21 11:10:05 -0500 (Thu, 21 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab07/summarize_expr.py $
#$Revision: 52966 $

import sys
import os

n=sys.argv[1:]
A={}

if len(sys.argv) != 3:
    print "Usage: summarize_expr.py <filename> <course number>"
    sys.exit(1)
if not os.access(n[0],os.R_OK):
    print "%s is not readable" % (n[0],)
    sys.exit(2)
InFile = open(n[0], "r")
l=len(n[1])
for line in InFile:

    line=line.split()
    value=float(line[2])
    if line[0][:l] == n[1]:
        if line[1] in A:
            A[line[1]].append(value)
        else:
            B={line[1]:[value]}
            A.update(B)
for keys in A:
    L=sorted(A[keys])
    mi=min(A[keys])
    ma=max(A[keys])
    s=sum(A[keys])
    le=len(A[keys])
    me=L[(le/2)]
    av=s/le

    print "%s: min= %.3f, max=%.3f, median=%.3f, avg=%.3f" % (keys,mi,ma,me,av,)

InFile.close()
sys.exit(0)
