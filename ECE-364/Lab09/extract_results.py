#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-03-07 11:32:25 -0500 (Thu, 07 Mar 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab09/extract_results.py $
#$Revision: 54105 $

import sys
import re
import os

n=sys.argv[1:]

if len(sys.argv) != 2:
    print "usage: extract_results.py <input_file>"
    sys.exit(1)
if not os.access(n[0],os.R_OK):
    print "error: %s is not readable" % (n[0],)
    sys.exit(2)

fp=open(sys.argv[1])
t=""
c=""
l=""

for line in fp:

    title = re.search("<TITLE>(.*?)</TITLE>",line)
    if title:
        t=title.group(1)
    
    course = re.search("<COURSE>(.*?)</COURSE>",line)
    if course:
        c=course.group(1)
    
    lang = re.search("<OPTIONS>-l( .*?) -m \d </OPTIONS>",line)
    if lang:
        l=lang.group(1)

    match=r"<PATH(\d)>/students/%s(s\d+)/%s(\-)(\d)(\.)%s (\d+)</PATH(\d)>"

    user = re.match(match%(c,t,l),line)
    if user:
        u=user

print "Lab Title: %s" % (t)
print "Course: %s" % (c)
print "Language: %s" % (l)
print "User1: %s User2: %s Lines Matched %d" % (u1,u2,m)

sys.exit(0)
