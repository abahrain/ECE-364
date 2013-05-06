#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-03-03 16:05:55 -0500 (Sun, 03 Mar 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab09/email.py $
#$Revision: 53784 $

import sys
import re

n=sys.argv[1:]

fp=open(sys.argv[1], "r")
for line in fp:
    line=line.split()
    if re.search(r"([\w.-])@purdue([\w.-]+)",line[0]):
        id=re.split(r"@",line[0],maxsplit=1)
        print "%s@ecn.purdue.edu %2s/100" % (id[0],line[1])

sys.exit(0)
