# This module provides addition support for two strings and returns a string in suitable format
def add(a,b):
	if a=='':
		a='0'
	try:
		a=int(a)
	except ValueError:
		a=float(a)
	try:
		b=int(b)
	except ValueError:
		b=float(b)
	ans=a+b
	ans=repr(ans)
	try:
		ans=int(ans)
	except ValueError:
		ans=float(ans)
	return repr(ans)
