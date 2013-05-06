#! /usr/bin/env python2.6
#
# $Author: ee364e11 $
# $Date: 2013-03-28 11:28:08 -0400 (Thu, 28 Mar 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364e11/Lab11/testExecute.py $
# $Revision: 54934 $
from ExecuteUnit import *
from IFAD import *
from Memory import *


dataMem = DataMemory(10)
registers = RegisterArray(8)
instructMem = DataMemory(3) 
fetchUnit = InstructionFetchAndDecode(instructMem)
dataMem.dumpMemory()
registers.dumpMemory()
instructMem.dumpMemory()
print "\n"
#The changes are listed to the right of the instruction. Compare results
#with what we have here. They should be the same!
execUnit = ExecuteUnit(fetchUnit, dataMem, registers)
lwInstruct1 = Instruction("lw",1,("imm",5),()) #Reg 1 = 5
lwInstruct2 = Instruction("lw",0,("reg",1),()) #Reg 0 = 5
swInstruct1 = Instruction("sw",0,("mem",2),()) #Mem 2 = 5
lwInstruct3 = Instruction("lw",4,("mem",2),()) #Reg 4 = 5
swInstruct2 = Instruction("sw",4,("reg",3),()) #Reg 3 = 5
addInstruct = Instruction("add",2,("imm",54),("reg",1)) #Reg 2 = 59
subInstruct = Instruction("sub",3,("mem",2),("imm",2)) #Reg 3 = 3 
mulInstruct = Instruction("mul",4,("imm",3),("imm",4)) #Reg 4 = 12
divInstruct = Instruction("div",5,("imm",18),("imm",3)) #Reg 5 = 6
beqInstruct1 = Instruction("beq",7,("mem",2),()) #Branch to 5
beqInstruct2 = Instruction("beq",1,("reg",2),()) #No branch
jmpInstruct1 = Instruction("jmp",5,("imm",4),()) #Jump to 4
def memDump(): #Displays all relevant parts of memory
    dataMem.dumpMemory()
    registers.dumpMemory()
    instructMem.dumpMemory()
    print fetchUnit.pc
    print "\n"
execUnit.executeInstruction(lwInstruct1)
memDump()
execUnit.executeInstruction(lwInstruct2)
memDump()
execUnit.executeInstruction(swInstruct1)
memDump()
execUnit.executeInstruction(lwInstruct3)
memDump()
execUnit.executeInstruction(swInstruct2)
memDump()
execUnit.executeInstruction(addInstruct)
memDump()
execUnit.executeInstruction(subInstruct)
memDump()
execUnit.executeInstruction(mulInstruct)
memDump()
execUnit.executeInstruction(divInstruct)
memDump()
execUnit.executeInstruction(beqInstruct1)
memDump()
execUnit.executeInstruction(beqInstruct2)
memDump()
execUnit.executeInstruction(jmpInstruct1)
memDump()

