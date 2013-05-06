#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-04-02 21:27:06 -0400 (Tue, 02 Apr 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab11/testDecoder.py $
#$Revision: 55182 $

import sys
import os
import re
import InstructionFetchAndDecode

F = InstructionFetchAndDecode.InstructionFetchAndDecode(None)

print "processInstruction(125730816)"
I = F.processInstruction(125730816)
print "op   => %s" % I.getOp()
print "reg  => %d" % I.getReg()
print "mem1 => " + str(I.getMem1())
print "mem2 => " + str(I.getMem2())

print ""

print "processInstruction(469776385)"
I = F.processInstruction(469776385)
print "op   => %s" % I.getOp()
print "reg  => %d" % I.getReg()
print "mem1 => " + str(I.getMem1())
print "mem2 => " + str(I.getMem2())

while(1):
  print ""
  input = raw_input("Enter a process value (or \"exit\" to exit): ")
  if (input == "exit"):
    break
  try:
    input = int(input)
  except:
    print "Invalid machine code"
    continue
  I = F.processInstruction(input)
  if (I == None):
    print "Invalid machine code"
    continue
  print "op   => %s" % I.getOp()
  print "reg  => %d" % I.getReg()
  print "mem1 => " + str(I.getMem1())
  print "mem2 => " + str(I.getMem2())

sys.exit(0)
