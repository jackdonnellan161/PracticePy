#! /usr/bin/env python3

class Fraction:
	def __init__(self,top,bottom):
		if bottom == 0:
			raise RuntimeError("Denominator cannot be zero")
		self.num = top
		self.den = bottom
	def __str__(self):
		return str(self.num)+"/"+str(self.den)
	def __add__(self,otherFrac):
		newNum = (self.num*otherFrac.den) + (otherFrac.num*self.den)
		newDen = self.den*otherFrac.den
		fac = gcd(newNum,newDen)
		return Fraction(newNum//fac,newDen//fac)
	def __sub__(self,otherFrac):
		newNum = (self.num*otherFrac.den)-(self.den*otherFrac.num)
		newDen = self.den*otherFrac.den
		fac = gcd(newNum,newDen)
		return Fraction(newNum//fac,newDen//fac)
	def __mul__(self,otherFrac):
		newNum = self.num*otherFrac.num
		newDen = self.den*otherFrac.den
		fac = gcd(newNum,newDen)
		return Fraction(newNum//fac,newDen//fac)
	def __truediv__(self,otherFrac):
		newNum = self.num*otherFrac.den
		newDen = self.den*otherFrac.num
		fac = gcd(newNum,newDen)
		return Fraction(newNum//fac,newDen//fac)	
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
def gcd(m,n):
	num = 0
	if n<0:
		n = -n
	if m%n == 0:
		num = n
	else:
		num = gcd(n,m%n)
	return num

myF = Fraction(3,5)
otherF = Fraction(4,5)
thirdF = Fraction(30,50)
#myF.show()
#print(myF,"works")
#print(myF==otherF)
#print(gcd(20,10))
#print(myF==thirdF)
#print(Fraction(1,2)-Fraction(1,3))
#print(Fraction(1,2)-Fraction(8,5))
print(Fraction(1,10)/Fraction(1,15))
print(Fraction(5,3)/Fraction(3,10))

