#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-03-07 10:22:08 -0500 (Thu, 07 Mar 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab09/replace_regex.py $
#$Revision: 54058 $

import sys
import re
import os

n=sys.argv[1:]
l=len(n)

if len(sys.argv) <= 1:
    print "usage: replace_regex.py <input_file> <bad_expr_1><replace_expr_1><bad_expr_2><replace_expr_2>"
    sys.exit(1)
if not os.access(n[0],os.R_OK):
    print "error: %s is not readable" % (n[0],)
    sys.exit(2)

try:
    fp=open(sys.argv[1])
except:
    sys.exit(3)

l=(l-1)/2

for line in fp:
    for i in range(l):
        j=i+1
        j=j*2
        line=re.sub(re.escape(sys.argv[j]), sys.argv[j+1], line)
    print line

sys.exit(0)
