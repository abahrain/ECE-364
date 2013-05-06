#! /usr/bin/env python2.6
#
#$Author: ee364f04 $
#$Date: 2013-04-04 10:37:55 -0400 (Thu, 04 Apr 2013) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-lnx/home/ecegrid/a/ece364sv/svn/S13/students/ee364f04/Lab12/poly.py $
#$Revision: 55342 $

import sys
import math
import re

class Polynomial:

    def __int__(self,coefficients,exponents):
        self.coefficients = int(coefficients)
        self.exponents = int(exponents)

        if len(coefficients) <= 0:
            raise ValueError
        if len(exponents) <= 0:
            raise ValueError
        if len(coefficients) != len(exponents):
            raise ValueError


    def evaluate(self,at):
        x=self.at
        math=float(0)

        for i in range(len(self.coefficients)):
            math = math + float(self.coefficients[i] * x ** self.exponents[i])
        return math
    
    def differentiate(self):
        polyc=[]
        polye=[]
        poly=""
        
        for i in range(len(self.coefficients)):
            polyc[i] = self.coefficients[i] * self.exponents[i]
            polye[i] = self.exponents[i] - 1
        for i in range(len(self.exponents)-1):
            poly=poly+polyc[i]+"x^"+polye[i]
        return Polynomial(poly)

    def __str__(self):
        pol=""

        for i in range(len(self.coefficients)):
            if self.coefficients[i] > 0:
                pol= pol + "+" + str(self.coefficients[i]) + "x^" + str(self.coefficients[i])
            if self.coefficients[i] < 0:
                pol= pol + "" + str(self.coefficients[i]) + "x^" + str(self.coefficients[i])
            if self.coefficient[i] == 0:
                pol= pol + "+" + "x^" + str(self.coefficients[i])
                
        return pol

    def isValidPolynomialString(self,polyno):
        validin = r"(\d+)x^(\d+)(((+|-)(\d+)x^(\d+))+)|(\d+)"

        if re.match(validin,self.polyno):
            return True
        else:
            return False
sys.exit(0)
