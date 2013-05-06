#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-02-17 20:49:37 -0500 (Sun, 17 Feb 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab07/FunctionFun.py $
#$Revision: 52020 $

import sys

x=1
o=0
f=1

print "fact_iter(0) = 1"
for i in [1, 2, 3, 4, 5]:
    x=i*x
    print "fact_iter(%d) = %d" % (i,x,)

def fact(numb):
    if numb < 1:
        return 1
    else:
        return numb * fact(numb-1)
for i in [0, 1, 2, 3, 4, 5]:
    print "fact(%d)= %d" % (i,fact(i),)

print "fib_iter(0) = 0"
print "fib_iter(1) = 1"
for i in [2, 3, 4, 5, 6]:
    m= f+o
    print "fib_iter(%d) = %d" % (i,m,)
    o=f
    f=m

def fib(num):
    if num ==0 or num ==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)
print "fib(0) = 0"
for w in [0, 1, 2, 3, 4, 5]:
    print "fib(%d) = %d" % (w+1,fib(w),)
sys.exit(0)
