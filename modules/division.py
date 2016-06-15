# This module provides Division support for two strings and returns a string in suitable format
def divide(a,b):
	a=float(a)
	b=float(b)
	ans=a/b
	ans=repr(ans)
	try:
		ans=int(ans)
	except ValueError:
		ans=float(ans)
	return repr(ans)
