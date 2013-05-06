#!/usr/bin/env python2.6

from Memory import *


mem=Memory(5)
mem.storeValue(0001, 5)
mem.loadValue(0001)
mem.dumpMemory()

mem=DataMemory(5)
mem.storeValue(0001, 5)
mem.loadValue(0001)
mem.dumpMemory()

mem=InstructionMemory(5)
mem.storeValue(0001, 5)
mem.loadValue(0001)
mem.loadValue(0001)
mem.loadValue(0001)
mem.loadValue(0001)
mem.loadValue(0001)
mem.loadValue(0001)
mem.loadValue(0001)
mem.loadValue(0001)
mem.dumpMemory()

mem=RegisterArray(8)
mem.storeValue('$t0', 5)
mem.dumpMemory()

