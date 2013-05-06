#! /usr/bin/env python
#
#$Author: ee364e05 $
#$Date: 2013-03-28 11:02:33 -0400 (Thu, 28 Mar 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364e05/Lab11/testAssembler.py $
#$Revision: 54927 $
#
#
##         Modules         ##
import sys
import os

#checking if module exists, is executable and can be imported
if not os.path.exists("./Assembler.py"): print "Error: Assembler does not exist"; sys.exit(1)
elif not os.access("./Assembler.py", os.X_OK): print "Error: Assembler is not executable"; sys.exit(1)

try: from Assembler import *
except: print "Error: Unable to import Assembler.py"; sys.exit(1)

if not os.path.exists("./code_1.txt"): print "Error: code_1.txt does not exist, must add a readable sample assembly file named code_1.txt for this program to function"; sys.exit(6)

#Testing Assembler Class Creation
try: test = Assembler("code_1.txt")
except: print "Error: Unable to create Assembler object"; sys.exit(2)

#Testing parseInstruction Function

try: integer = test.parseInstruction('lw $t7,!1000')
except: print "Error: Unable to execute parseInstruction function"; sys.exit(3)

if(integer != 125730816): print "Error: parseInstruction function has incorrect output with test lw $t7,!1000. Function output was %d, should be 125730816" % (integer); sys.exit(4)

try: integer = test.parseInstruction('sub $t4,$t3,1')
except: print "Error: Unable to execute parseInstruction function"; sys.exit(3)

if(integer != 469776385): print "Error: parseInstruction function has incorrect output with test sub $t4,$t3,1. Function output was %d, should be 469776385" % (integer); sys.exit(5)



#test_strings_lw = ["lw $t0,!1000","lw $t0,1020","lw $t1,!1000","lw $t1,1020", "lw $t2,!1000","lw $t2,1020","lw $t3,!1000","lw $t3,1020", "halt", "jmp 10", "add $t1,!100,$t5"]
#                                   h op rg t1num1      t2num2
#                                   /\/-\/-\/\/--------\/\/--------\   
test_strings_lw = {"lw $t0,!1000":0b00000000011111101000000000000000,
             "lw $t0,1020":       0b00000000101111111100000000000000,
             "lw $t1,!1000":      0b00000001011111101000000000000000,
             "lw $t1,1020":       0b00000001101111111100000000000000,
             "lw $t2,!1000":      0b00000010011111101000000000000000,
             "lw $t2,1020":       0b00000010101111111100000000000000,
             "lw $t3,!1000":      0b00000011011111101000000000000000,
             "lw $t3,1020":       0b00000011101111111100000000000000,
             "halt":              0b11000000000000000000000000000000,
             "jmp 10":            0b00111000100000001010000000000000,
             "add $t1,!100,$t5":  0b00010001010001100100000000000101,
             "sub $t4,$t3,1":     0b00011100000000000011100000000001,
             'lw $t7,!1000':      0b00000111011111101000000000000000,
                   }

for key in test_strings_lw.keys():
	skip_bool = False 
	try: integer = test.parseInstruction(key)
	except: print "Error: Unable to execute parseInstruction with input %s" % (key); skip_bool = True
		
	if(not skip_bool):
		if(integer != test_strings_lw[key]): print "Testing: %s. The ouput is: %d, should be %d"%(key, integer, test_strings_lw[key])

print "No errors found"

sys.exit(0)

