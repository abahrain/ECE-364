#! /usr/bin/env python

import sys
import os

class Expression:
	def __init__(self):
		pass
        	
	def evaluate(self, variables):
                self.variables = variables
                return self.variables
	def __str__(self):
		variables=str(self.variables)
		return variables
		
class RealValuedExpression(Expression):
	def __init__(self, value):
		self.value = value
                
		
	def evaluate(self, variables):
		return self.value

	def __str__(self):
		value = str(self.value)
                return value

class BinaryExpression(Expression):
	def __init__(self, lhs, rhs, op):
		self.lhs = lhs
                self.rhs = rhs
                self.op = op

	def evaluate(self, variables):
            if self.op == '+':
                value = self.lhs.evaluate({})+self.rhs.evaluate({})
            if self.op == '-':
                value = self.lhs.evaluate({})-self.rhs.evaluate({})
            if self.op == '*':
                value = self.lhs.evaluate({})*self.rhs.evaluate({})
            if self.op == '/':
                value = self.lhs.evaluate({})/self.rhs.evaluate({})

            return value


	def __str__(self):
		value=str(self.lhs)+str(self.op)+str(self.rhs)
                return value

class VariableExpression(Expression):
	def __init__(self, variable_name):
		self.variable_name = variable_name
	
	def evaluate(self, variables):
                return variables[self.variable_name]

	def __str__(self):
		name = str(self.variable_name)
		return name
