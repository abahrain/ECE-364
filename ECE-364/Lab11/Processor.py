#! /usr/bin/env python2.6
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

import sys
from Assembler import *
from ExecuteUnit import *
from Memory import *
from InstructionFetchAndDecode import *

class Processor:
    def __init__(self):
        self.dataMemory = DataMemory(1024)
        self.instructionMemory = InstructionMemory(32)
        self.registerArray = RegisterArray(8)
        self.fetchDecode = InstructionFetchAndDecode(self.instructionMemory)

        self.execute = ExecuteUnit(self.fetchDecode, self.dataMemory, self.registerArray)

    def simulate(self):
        while(True):
            machineCode = self.fetchDecode.fetchInstruction()
            instruction = self.fetchDecode.processInstruction(machineCode)
            if(not instruction):
                break
            self.execute.executeInstruction(instruction)

    def outputState(self):
        self.registerArray.dumpMemory()
        self.instructionMemory.dumpMemory()
        self.dataMemory.dumpMemory()

    def loadAssemblyFile(self, assembler):
        assembler.loadMemory(self.instructionMemory)

if len(sys.argv) - 1 != 1:
    print "usage: Processor.py <filename>"
    sys.exit(1)

assembler = Assembler(sys.argv[1])
processor = Processor()
processor.loadAssemblyFile(assembler)
processor.simulate()
processor.outputState()



sys.exit(0)
