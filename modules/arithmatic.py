#This module will provide one stop solution to and string expression composed of operands and operators between +,-,/,* and curved braces ()
import evaluate

def earth(s):
	
	#parsing to simplify the expression by removing brackets
	op = -1,cls=-1
	for i in range(0,len(s)):
		if s[i] == '(':
			op=i
		if s[i] == ')':
			cls=i
			if op==-1:
				#Raise Exception
			simplify=evaluate.solve(s[op+1:cls])
			if simplify==-1:
				#Raise Exception
			s=s[0:op]+simplify+s[cls+1:]
			i=0,op=-1,cls=-1
	
	s=evaluate.solve(s)
	if s==-1:
		#Raise Exception
	return s
	

