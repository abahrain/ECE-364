#! /usr/bin/env python2.6
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$
import sys,os

class Assembler:
    def __init__(self,filename):
        try :
            self.f=open(filename,"r")
        except IOError as e:
            print "Error: Unable to open assembly file: %s" %(e)
            sys.exit(2)

        #know that we can open and read the file
        
    def parseInstruction(self, instructionString):
        machinecode=""
        insdict={"lw":"000","sw":"001","add":"010","sub":"011","mul":"100","div":"101","beq":"110","jmp":"111"}
        if instructionString == "halt":
            haltidentifier="11"
            while len(haltidentifier)!=32:
                haltidentifier+="0"
            return int(haltidentifier,2)

        machinecode="00"
        instructionList=instructionString.split();
        opcode=insdict[instructionList[0]];
        machinecode+=opcode
        
    
        memoryList=instructionList[1].split(',');
        if instructionList[0]!="jmp":
            register=memoryList[0][2]
            binregister=bin(int(register))[2:]

            while len(binregister) != 3:
                binregister="0"+binregister

            machinecode+=binregister
            memoryList=memoryList[1:];
        else:
            machinecode += "000"
            
        for i in memoryList:
            if i[0]=='$':
                binregister=bin(int(i[2]))[2:]
                while len(binregister) != 10:
                    binregister="0"+binregister
                
                machinecode+="00"+binregister

            else:
                if i[0]=='!':
                    machinecode+="01"#for immediate
                    add=i[1:]
                else:
                    machinecode+="10"#for direct
                    add=i
                binaddress=bin(int(add))[2:]
                while len(binaddress) !=10:
                    binaddress="0"+binaddress

                machinecode+=binaddress

        
                
        while len(machinecode)!=32:
            machinecode+="0"#pads machine code with zeros to extend length to 32
        
        return int(machinecode,2)#returns machine code as an int 
         
    def loadMemory(self,memory):
        index=0
        for line in self.f:
            memory.storeValue(index,self.parseInstruction(line.strip()))
            index+=1


        




