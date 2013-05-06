#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-21 11:32:51 -0500 (Thu, 21 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab07/baseball_stats.py $
#$Revision: 52980 $

import sys
import os

n=sys.argv[1:]
hit=0
bat=0
ave=0
base=0
A={"single":1,"double":2,"triple":3,"HR":4}

if len(sys.argv) != 3:
    print "Usage: baseball_stats.py <infile> <outfile>"
    sys.exit(1)
if not os.access(n[0],os.R_OK):
    print "%s is not readable" % (n[0],)
    sys.exit(2)
if os.path.exists(n[1]):
    print "Error: %s already exists" % (n[1],)
    sys.exit(2)

InFile = open(n[0], "r")
OutFile = open(n[1], "w+")

for line in InFile:
    base=0
    line=line.split()

    for res in line:
        if res in A:
            base=base+A[res]
            hit=hit+1
            bat=bat+1


    print "%s: Hits: %d At-bats: %d Avg: %.3f Total Bases: %d" % (line[0],hit,bat,ave,base,)

InFile.close()
OutFile.close()
sys.exit(0)
