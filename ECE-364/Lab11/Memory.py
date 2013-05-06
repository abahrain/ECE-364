#!/usr/bin/env python2.6
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

import re
import sys
import bitWorker

class Memory:
    def __init__(self, size):
        self.list=[]
        for i in range(0,size):
            self.list.append(0)


    def loadValue(self, location):
        if re.match(r"[0-9a-f]{4}", str(location)):
            hex = "0x" + str(location)
            index = int(hex, 16)
            return self.list[index]

        return self.list[location]


    def storeValue(self, location, value):
        if re.match(r"[0-9a-f]{4}", str(location)):
            hex = "0x" + str(location)
            index = int(hex, 16)
            self.list[index] = value
        else:
            self.list[location] = value


    def dumpMemory(self):
        for i,elem in enumerate(self.list):
            index_str=hex(i)
            index_str=index_str[2:]
            while (len(index_str) < 4):
                index_str = '0' + index_str

            print "%s -> " % (index_str,),
            mask = 0x80000000
            while mask:
                bit = elem & mask != 0
                sys.stdout.write("%d" % (bit))
                mask >>= 1

            print ""


class DataMemory(Memory):
    def dumpMemory(self):
        for i,elem in enumerate(self.list):
            index_str=hex(i)
            index_str=index_str[2:]
            while (len(index_str) < 4):
                index_str = '0' + index_str

            print "%s -> %d" % (index_str, self.list[i])



class InstructionMemory(Memory):
    def loadValue(self, location):
        self.list[location][1] += 1
        return self.list[location]


    def storeValue(self, location, value):
        self.list[location] = [value, 0]


    def dumpMemory(self):
        i = 0
        for elem in self.list:
            try:
                print "%d -> " % (i,),
                mask = 0x80000000
                while mask:
                    bit = elem[0] & mask != 0
                    sys.stdout.write("%d" % (bit))
                    mask >>= 1

                print " <%d>" % (elem[1])

            except TypeError:
                mask = 0x80000000
                while mask:
                    bit = self.list[i] & mask != 0
                    sys.stdout.write("%d" % (bit))
                    mask >>= 1

                print " <%d>" % (self.list[i])
            i += 1

class RegisterArray(Memory):
    def loadValue(self, location):
        #num_reg = re.match(r"\$t(?P<num>[0-7])", str(location))
        #if num_reg:
        #    i = int(num_reg.group('num'))
        #    return self.list[i]
        #else:
            return self.list[location]


    def storeValue(self, location, value):
        num_reg = re.match(r"\$t(?P<num>[0-7])", str(location))
        if num_reg:
            i = int(num_reg.group('num'))
            self.list[i] = value
        else:
            self.list[location] = value

    def dumpMemory(self):
        i = 0
        for elem in self.list:
            print "$t%d -> %d" % (i, self.list[i])
            i+=1




