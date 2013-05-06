#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-03-27 22:42:31 -0400 (Wed, 27 Mar 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab11/testBinary.py $
#$Revision: 54908 $

import sys
import bitWorker

dBin=bitWorker.displayBinary(22)
gBin1=bitWorker.getBit(0, 99)
gBin2=bitWorker.getBit(3, 17)
gPV1=bitWorker.getPartialValue(1,4,67)
gPV2=bitWorker.getPartialValue(3,6,117)
gPV3=bitWorker.getPartialValue(1,3,22)

print '\ndisplayBinary'
print dBin
print '\ngetBit'
print gBin1
print gBin2
print '\ngetPartialValue'
print gPV1
print gPV2
print gPV3
