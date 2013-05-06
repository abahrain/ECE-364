#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-03-06 21:11:32 -0500 (Wed, 06 Mar 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab09/function_finder.py $
#$Revision: 54013 $

import sys
import re
import os

n=sys.argv[1:]

if len(sys.argv) != 2:
    print "Usage: function_finder.py <infile>"
    sys.exit(1)
if not os.access(n[0],os.R_OK):
    print "%s is not readable" % (n[0],)
    sys.exit(2)

fp=open(sys.argv[1])

for line in fp:
    if re.search("def [a-zA-Z0-9]+",line):
        line=line.split("(")
        print line[0]
        line[1]=line[1].replace("):","")
        line=line[1].split(",")
        for i in range(len(line)):
            print "Arg%d: %s" % (i+1,line[i])


sys.exit(0)
