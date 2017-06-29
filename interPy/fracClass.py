#! /usr/bin/env python3

class Fraction:
	def __init__(self,top,bottom):
		if bottom == 0:
			raise RuntimeError("Denominator cannot be zero")
		if top % 1 != 0 or bottom %1 != 0:
			raise RuntimeError("Both numerator and denominator must be integers")
		if bottom<0:
			bottom = -bottom
			top = -top
		fac = gcd(top,bottom)
		self.num = top//fac
		self.den = bottom//fac
	def __str__(self):
		return str(self.num)+"/"+str(self.den)
	def __add__(self,otherFrac):
		newNum = (self.num*otherFrac.den) + (otherFrac.num*self.den)
		newDen = self.den*otherFrac.den
		return Fraction(newNum,newDen)
	def __sub__(self,otherFrac):
		newNum = (self.num*otherFrac.den)-(self.den*otherFrac.num)
		newDen = self.den*otherFrac.den
		return Fraction(newNum,newDen)
	def __mul__(self,otherFrac):
		newNum = self.num*otherFrac.num
		newDen = self.den*otherFrac.den
		return Fraction(newNum,newDen)
	def __truediv__(self,otherFrac):
		newNum = self.num*otherFrac.den
		newDen = self.den*otherFrac.num
		return Fraction(newNum,newDen)	
	def __eq__(self,otherFrac):
		return self.num*otherFrac.den == otherFrac.num*self.den
	def __ne__(self,otherFrac):
		return self.num*otherFrac.den != otherFrac.num*self.den
	def __gt__(self,otherFrac):
		return self.num*otherFrac.den > otherFrac.num*self.den
	def __ge__(self,otherFrac):
		return self.num*otherFrac.den >= otherFrac.num*self.den
	def __lt__(self,otherFrac):
		return self.num*otherFrac.den < otherFrac.num*self.den
	def __le__(self,otherFrac):
		return self.num*otherFrac.den <= otherFrac.num*self.den
	def show(self):
		print(self.num,"/",self.den)
	def getNum(self):
		return self.num
	def getDen(self):
		return self.den

def gcd(m,n):
	num = 0
	if n<0:
		n = -n
	if m<0:
		m = -m
	if m%n == 0:
		num = n
	else:
		num = gcd(n,m%n)
	return num

def main():	
	myF = Fraction(3,5)
	otherF = Fraction(4,5)
	thirdF = Fraction(30,50)
	print(Fraction(1,10)+Fraction(1,-15))
	print(Fraction(5,3)/Fraction(3,10))


main()

