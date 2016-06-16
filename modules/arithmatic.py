#This module will provide one stop solution to and string expression composed of operands and operators between +,-,/,* and curved braces ()
import evaluate
import expressionValidation
def earth(s):
	
	#parsing to simplify the expression by removing brackets
	if expressionValidation.validate(s)==0:
		s="Invalid Expression"
		return s
		
	op=-1;cls=-1
	for i in range(0,len(s)):
		if s[i] == '(':
			op=i
		if s[i] == ')':
			cls=i
			if op==-1:
				s="Invalid Expression"
				break
			simplify=evaluate.solve(s[op+1:cls])
			s=s[0:op]+simplify+s[cls+1:]
			i=0;op=-1;cls=-1
	if op!=-1 or cls!=-1:
		s="Invalid Expression"
		return s
	if s!="Invalid Expression":
		s=evaluate.solve(s)
	return s
	

