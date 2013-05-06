#!/usr/bin/env python2.6

import os, sys, math, random
import libalg

if len(sys.argv) != 3:
	sys.stderr.write("usage: algorithm.py <algorithm_name> <N>\n")
	sys.exit(1)
	
try:
	N=int(sys.argv[2])
except:
	sys.stderr.write("error: %s is not a valid integer.\n" % (sys.argv[2],))
	sys.exit(1)
	
if N <= 0:
	sys.stderr.write("error: N must be a number larger than 0.\n")
	sys.exit(1)
	
try:
	algo=libalg.get_algorithm(sys.argv[1])
	print "%s runtime: %.3f" % (sys.argv[1], algo(N))
	sys.exit(0)
except Exception as e:
	sys.stderr.write("Unknown algorithm: %s\n" % (sys.argv[1]))
	sys.exit(1)

