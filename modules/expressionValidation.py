#This modules provides solution to the problem of validating the string arithmatic expression for evaluation
#Module uses RegEx to try on some tests on the input string to declare it to be valid or other wise
import re
def validate(s):
	match=re.search(r'[^0-9+-/\*()]',s)
	if match:
		return 0
	match=re.search(r'\)\(',s)
	if match:
		return 0
	match=re.search(r'\(/',s)
	if match:
		return 0
	match=re.search(r'\(*',s)
	if match:
		return 0
	match=re.search(r'\.[0-9]*\.',s)
	if match:
		return 0
	match=re.search(r'\+\)',s)
	if match:
		return 0
	match=re.search(r'\-\)',s)
	if match:
		return 0
	match=re.search(r'/\)',s)
	if match:
		return 0
	match=re.search(r'\*\)',s)
	if match:
		return 0
	match=re.search(r'/\*',s)
	if match:
		return 0
	match=re.search(r'\*/',s)
	if match:
		return 0
	match=re.search(r'\+/',s)
	if match:
		return 0
	match=re.search(r'//',s)
	if match:
		return 0
	match=re.search(r'\*\*',s)
	if match:
		return 0
	match=re.search(r'\+\*',s)
	if match:
		return 0
	match=re.search(r'\-/',s)
	if match:
		return 0
	match=re.search(r'\-\*',s)
	if match:
		return 0
	match=re.search(r'(/\+/)|(/\+\*)|(/\+\+)|(/\+\-)|(/\-/)|(/\-\*)|(/\-\+)|(/\-\-)',s)
	if match:
		return 0
	match=re.search(r'(\*\+/)|(\*\+\*)|(\*\+\+)|(\*\+\-)|(\*\-/)|(\*\-\*)|(\*\-\+)|(\*\-\-)',s)
	if match:
		return 0
	match=re.search(r'(\+\+/)|(\+\+\*)|(\+\+\+)|(\+\+\-)|(\+\-/)|(\+\-\*)|(\+\-\+)|(\+\-\-)',s)
	if match:
		return 0
	match=re.search(r'(\-\+/)|(\-\+\*)|(\-\+\+)|(\-\+\-)|(\-\-/)|(\-\-\*)|(\-\-\+)|(\-\-\-)',s)
	if match:
		return 0
	
	return 1