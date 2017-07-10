#!/usr/bin/env python3

class bankAcct:
	def __init__(self,name):
		self.name = name
		self.balance = 0
	def getName(self):
		return self.name
	def getBalance(self):
		return self.balance
	def deposit(self,number):
		if number < 0:
			raise RuntimeError("Cannot deposit negative dollars")
		self.balance += number
		return self.balance
	def withdraw(self,number):
		if number > 0:
			raise RuntimeError("Cannot deposit negative dollars")
		self.balance -= number
		return self.balance

class minBalanceAcct(bankAcct):
	def __init__(self,minBalance):
		bankAcct.__init__(self)
		self.minBalance = minBalance
	def withdraw(self,number):
		if self.balance-number < self.minBalance:
			raise RuntimeError("You cannot withdraw beyond minimum balance")
		else:
			bankAcct.withdraw(self,number)




def main():
	a = minBalanceAcct("Jack")
	b = bankAcct("Luke")
main()
