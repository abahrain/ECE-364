#!/usr/bin/env python2.6
#
# $Author: ee364e02 $
# $Date: 2013-03-24 15:04:16 -0400 (Sun, 24 Mar 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364e02/Prelab11/bitWorker.py $
# $Revision: 54697 $

import sys

def displayBinary(num):
    if num < 0:
        print "error: does not support negative values"
        return

    # display lsb to 16 bits
    mask = 0x80000000
    while mask:
        bit = num & mask != 0
        sys.stdout.write("%d" % (bit))
        mask >>= 1

    print ""


def getBit(index, num):
    if num < 0:
        print "error: does not support negative values"
        return
    if index > 31:
        print "error: support only to 32 bit"
        return

    mask = 0x00000001
    for i in range(0, index):
        mask <<= 1

    bit = int(num & mask != 0)
    print bit


def getPartialValue(index1, index2, num):
    if num < 0:
        print "error: does not support negative values"
        return
    elif index1 > index2:
        print "error: invalid bounds"
        return
    elif index1 > 31 or index2 > 31:
        print "error: support only to 32 bit"
        return

    mask1 = 0x00000001
    for i in range(0, index1):
        mask1 <<= 1

    mask2 = 0x00000001
    for i in range(0, index2):
        mask2 <<= 1

    val = num & mask2
    while mask1 != mask2:
        val += num & mask1
        mask1 <<= 1

    # adjust val for index1 offset
    while index1:
        val >>= 1
        index1 -= 1

    print val

