#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-03-27 22:42:05 -0400 (Wed, 27 Mar 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Prelab11/bitWorker.py $
#$Revision: 54907 $

import sys

def displayBinary(num):
    Bin = bin(num)[2:].zfill(16)
    return Bin
def getBit(index,num):
    if 0 > index > 31:
        raise ValueError("invalid index")
    num = bin(num)[2:].zfill(32)
    return num[31-index]
def getPartialValue(index1,index2,num):
    tmp=''
    if 0 > index1 > 32:
        raise ValueError("invalid index")
    if 0 > index2 > 31:
        raise ValueError("invalid index")
    num = bin(num)[2:].zfill(16)
    for i in range(index1,index2+1):
        tmp=num[15-i]+tmp
    
    return int(tmp,2)
