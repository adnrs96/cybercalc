#This module accepts a raw string expression composed of operands and operators between +,-,/,* and returns the mathematical evaluation
import add
import subtract
import multiply
import division

#Performs specific operations on elementary expression	
def operation(oper1,oper2,oper):
	if oper==0:
		return division.divide(oper1,oper2)
	if oper==1:
		return multiply.mul(oper1,oper2)
	if oper==2:
		return add.add(oper1,oper2)
	if oper==3:
		return subtract.sub(oper1,oper2)
	return -1


#Performs parsing for input operator and resolves expression
def operator_parser(s,op,oper):
	mid=s.find(op)
	while mid!=-1:
		i=mid-1;opn=-1;cls=-1
		while i>-1 and s[i] not in {'+','-','*','/'}:
			i=i-1
		opn=i;i=mid+1
		if opn==mid-1:
			break
		while i<len(s) and s[i] not in {'+','-','*','/'}:
			i=i+1
		cls=i
		oper1=s[opn+1:mid];oper2=s[mid+1:cls]
		s=s[0:opn+1]+operation(oper1,oper2,oper)+s[cls:]
		mid=s.find(op)
	return s
		
#Calls for different parsing operations
def solve(s):
	#Parse for division operation
	s=operator_parser(s,'/',0)
	#Parse for multiplication operation
	s=operator_parser(s,'*',1)
	#Parse for Addition operation
	s=operator_parser(s,'+',2)
	#Parse for Subtraction operation
	s=operator_parser(s,'-',3)
	return s

