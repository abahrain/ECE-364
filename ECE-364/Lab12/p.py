#! /usr/bin/env python2.6
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$

import sys
import poly

p=0
e = (3,2,1)
c = (4,5,6)

j = poly.Polynomial(c,e)
p= j.evaluate(2)
print p
sys.exit(0)
