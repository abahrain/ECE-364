#! /usr/bin/env python2.6
#
#$Author: ee364e12 $
#$Date: 2013-03-27 22:46:55 -0400 (Wed, 27 Mar 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364e12/Prelab11/bitWorker.py $
#$Revision: 54909 $

def displayBinary(num):
  bits = ""
  mask = 0x8000
  for i in range(15,-1,-1): # Descend to remove subtraction in bit shift
    bits = bits + str((mask & num) >> i)
    mask >>= 1
  print bits

def getBit(index, num):
  if (index < 0 or index > 31): # Check if index is in bounds
    raise ValueError(index);
  mask = 1 << index
  return (num & mask) >> index

def getPartialValue(index1, index2, num):
  mask = 0;
  for i in range(index1, index2 + 1):
    mask |= 1 << i
  return (num & mask) >> index1
