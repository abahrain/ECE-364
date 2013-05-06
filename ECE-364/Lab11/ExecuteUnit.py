#! /usr/bin/env python2.6
#
# $Author: ee364e11 $
# $Date: 2013-03-28 11:28:08 -0400 (Thu, 28 Mar 2013) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364e11/Lab11/ExecuteUnit.py $
# $Revision: 54934 $


class ExecuteUnit:
    def __init__(self, fetchUnit, dataMem, registers):
        self.fetchUnit = fetchUnit
        self.dataMem = dataMem
        self.registers = registers

    def executeInstruction(self, instruct):
        instructName = instruct.getOp()
        if instructName == "lw":
            reg = instruct.getReg()
            mem1 = instruct.getMem1()
            if mem1[0] == "imm":
                self.registers.storeValue(reg, mem1[1])
            elif mem1[0] == "reg":
                self.registers.storeValue(reg, self.registers.loadValue(mem1[1]))
            else:
                self.registers.storeValue(reg, self.dataMem.loadValue(mem1[1]))
        elif instructName == "sw":
            reg = instruct.getReg()
            mem1 = instruct.getMem1()
            if mem1[0] == "imm":
                pass
            elif mem1[0] == "reg":
                self.registers.storeValue(mem1[1],self.registers.loadValue(reg))
            else:
                self.dataMem.storeValue(mem1[1],self.registers.loadValue(reg))
        elif instructName in ["add","sub","mul","div"]:
            reg = instruct.getReg()
            mem1 = instruct.getMem1()
            mem2 = instruct.getMem2()
            if mem1[0] == "imm":
                mem1val = mem1[1]
            elif mem1[0] == "reg":
                mem1val = self.registers.loadValue(mem1[1])
            else:
                mem1val = self.dataMem.loadValue(mem1[1])
            if mem2[0] == "imm":
                mem2val = mem2[1]
            elif mem2[0] == "reg":
                mem2val = self.registers.loadValue(mem2[1])
            else:
                mem2val = self.dataMem.loadValue(mem2[1])
            if instructName == "add":
                self.registers.storeValue(reg,mem1val+mem2val)
            elif instructName == "sub":
                self.registers.storeValue(reg,mem1val-mem2val)
            elif instructName == "mul":
                self.registers.storeValue(reg,mem1val*mem2val)
            else:
                self.registers.storeValue(reg,mem1val/mem2val)
        elif instructName == "beq":
            reg = instruct.getReg()
            mem1 = instruct.getMem1()
            
            if self.registers.loadValue(reg) == 0:
                if mem1[0] == "imm":
                    mem1val = mem1[1]
                elif mem1[1] == "reg":
                    mem1val = self.registers.loadValue(mem1[1])
                else:
                    mem1val = self.dataMem.loadValue(mem1[1])
                self.fetchUnit.updatePC(mem1val)
                return
        else: #if equals "jmp"
            mem1 = instruct.getMem1()
            if mem1[0] == "imm":
                mem1val = mem1[1]
            elif mem1[1] == "reg":
                mem1val = self.registers.loadvalue(mem1[1])
            else:
                mem1val = self.dataMem.loadvalue(mem1[1])
            self.fetchUnit.updatePC(mem1val)
            return
        self.fetchUnit.incrementPC()
