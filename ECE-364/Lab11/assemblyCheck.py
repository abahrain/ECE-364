#!/usr/bin/env python2.6
#
# $Author: ee364e02 $
# $Date: 2013-03-24 15:04:16 -0400 (Sun, 24 Mar 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364e02/Prelab11/assemblyCheck.py $
# $Revision: 54697 $

from sys import argv,exit
import re

def valid_args(args, cmd):
    reg = r"\$t[0-7]"
    imd = r"!\d+"
    mem = r"(\d\d?\d?|10[0-1]\d|102[0-4])"
    loc = r"(%s|%s|%s)" % (reg,imd,mem)
    arg_reg = re.compile("")
    if   cmd == 'lw':  arg_reg = re.compile('%s,%s' % (reg, loc))
    elif cmd == 'sw':  arg_reg = re.compile('%s,%s' % (reg, loc))
    elif cmd == 'add': arg_reg = re.compile('%s,%s,%s' % (reg, loc, loc))
    elif cmd == 'sub': arg_reg = re.compile('%s,%s,%s' % (reg, loc, loc))
    elif cmd == 'mul': arg_reg = re.compile('%s,%s,%s' % (reg, loc, loc))
    elif cmd == 'div': arg_reg = re.compile('%s,%s,%s' % (reg, loc, loc))
    elif cmd == 'beq': arg_reg = re.compile('%s,%s' % (reg, loc))
    elif cmd == 'jmp': arg_reg = re.compile('%s' % (loc))
    return arg_reg.match(args)


# Error checking
if len(argv) != 2:
    print "Usage: assemblyCheck.py <file>"
    exit(1)

try:
    file = open(argv[1])
except:
    print "Error: %s is not readable" % (argv[1])
    exit(2)

for i,line in enumerate(file):
    # ignore newlines
    if line.endswith('\n'):
        line = line[:-1]

    # split into cmd,args
    words = line.split()

    try:
        if words[0] != 'lw' and words[0] != 'sw' and words[0] != 'add' and \
           words[0] != 'sub' and words[0] != 'mul' and words[0] != 'div' and \
           words[0] != 'beq' and words[0] != 'jmp':
            print "Error: invalid line %d" % (i+1)
        elif not valid_args(words[1], words[0]):
            print "Error: invalid line %d" % (i+1)
    except IndexError as e: # this means the cmd has no arguments
        print "Error: invalid line %d" % (i+1)

exit(0)
