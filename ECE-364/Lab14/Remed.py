#! /usr/bin/env python2.6
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$

import sys
import re


input=r"+086(10)-69445464"
if re.match(r"(\+)(?P<CC>\d{3}).*(?P<AC>\d{2}).*\-(?P<NUM>\d{8})",input):
    #m=re.match(r"(\+)(?P<CC>\d{3}).*(?P<AC>\d{2}).*\-(?P<NUM>\d{8})",input)
    print "%s is a valid Chinese international phone number with Country Code %s and Area Code %s." % (input,input.group('CC'),input.group('AC'))
else:
    print "Wrong number!"

sys.exit(0)
