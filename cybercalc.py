from Tkinter import *
import re
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

def sub(a,b):
	try:
		a=int(a)
	except ValueError:
		a=float(a)
	try:
		b=int(b)
	except ValueError:
		b=float(b)
	ans=a-b
	ans=repr(ans)
	try:
		ans=int(ans)
	except ValueError:
		ans=float(ans)
	return repr(ans)

def mul(a,b):
	try:
		a=int(a)
	except ValueError:
		a=float(a)
	try:
		b=int(b)
	except ValueError:
		b=float(b)
	ans=a*b
	ans=repr(ans)
	try:
		ans=int(ans)
	except ValueError:
		ans=float(ans)
	return repr(ans)

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

#Performs specific operations on elementary expression	
def operation(oper1,oper2,oper):
	if oper==0:
		return divide(oper1,oper2)
	if oper==1:
		return mul(oper1,oper2)
	if oper==2:
		return add(oper1,oper2)
	if oper==3:
		return sub(oper1,oper2)
	return -1


#Performs parsing for input operator and resolves expression
def operator_parser(s,op,oper):
	mid=s.find(op)
	while mid!=-1:
		i=mid-1;opn=-1;cls=-1
		while i>-1 and s[i] not in {'+','-','*','/'}:
			i=i-1
		opn=i;i=mid+1
		if opn==mid-1 and op=='-':
			break
		while i<len(s) and s[i] not in {'+','-','*','/'}:
			i=i+1
		if i==mid+1:
			i=i+1
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

def earth(s):
	
	#parsing to simplify the expression by removing brackets
	#if validate(s)==0:
	#	s="Invalid Expression"
	#	return s
		
	op=-1;cls=-1
	for i in range(0,len(s)):
		if s[i] == '(':
			op=i
		if s[i] == ')':
			cls=i
			if op==-1:
				s="Invalid Expression"
				break
			simplify=solve(s[op+1:cls])
			s=s[0:op]+simplify+s[cls+1:]
			i=0;op=-1;cls=-1
	if op!=-1 or cls!=-1:
		s="Invalid Expression"
		return s
	if s!="Invalid Expression":
		s=solve(s)
	return s
	
action_text_control=0
def action_append(expr_inp,s):
	global action_text_control
	if action_text_control==1:
		expr_inp.delete(0,END)
		action_text_control=0
	expr_inp.insert(END,s)
def action_trimLast(expr_inp):
	expr_inp.delete(len(expr_inp.get())-1)	
def action_clear(expr_inp):
	expr_inp.delete(0,END)
def action_solve(expr_inp):
	global action_text_control
	try:
		s=expr_inp.get()
		s='('+s+')'
		s=earth(s)
	except:
		s="Invalid Expression"
	expr_inp.delete(0,END)
	expr_inp.insert(0,s)
	action_text_control=1
root = Tk()
root.wm_title("CyberCalc")
root.resizable(0,0)
f1=Frame(root)
f1.pack(fill=BOTH,expand=1)
f2=Frame(root,background="#FFFFFF")
f2.pack(fill=BOTH,expand=1,ipadx=0,ipady=0)
f3=Frame(root,background="#434343")
f3.pack(fill=BOTH,expand=1)
expr_inp = Entry(f2,highlightthickness=0,font=("Helvetica", 12),borderwidth=0,justify=RIGHT,width=34)
expr_inp.grid(row=1,columnspan=6,padx=(0,0),pady=(0,0),ipadx=10,ipady=5,sticky=E+W)
b_7 = Button(f3, text="7",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'7'))
b_7.grid(row=1, column=1,columnspan=1,padx=(10,5),pady=(10,5),sticky=E+W)
b_8 = Button(f3, text="8",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'8'))
b_8.grid(row=1, column=2,columnspan=1,padx=(5,5),pady=(10,5),sticky=E+W)
b_9 = Button(f3, text="9",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'9'))
b_9.grid(row=1, column=3,columnspan=1,padx=(5,5),pady=(10,5),sticky=E+W)
b_div = Button(f3, text="/",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'/'))
b_div.grid(row=1, column=4,columnspan=1,padx=(5,5),pady=(10,5),sticky=E+W)
b_revert = Button(f3, text="area's",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_clear(expr_inp))
b_revert.grid(row=1, column=5,columnspan=1,padx=(5,5),pady=(10,5),sticky=E+W)
b_back = Button(f3, text="C",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_trimLast(expr_inp))
b_back.grid(row=1, column=6,columnspan=1,padx=(5,10),pady=(10,5),sticky=E+W)

b_4 = Button(f3, text="4",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'4'))
b_4.grid(row=2, column=1,columnspan=1,padx=(10,5),pady=(5,5),sticky=E+W)
b_5 = Button(f3, text="5",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'5'))
b_5.grid(row=2, column=2,columnspan=1,padx=(5,5),pady=(5,5),sticky=E+W)
b_6 = Button(f3, text="6",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'6'))
b_6.grid(row=2, column=3,columnspan=1,padx=(5,5),pady=(5,5),sticky=E+W)
b_mul = Button(f3, text="*",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'*'))
b_mul.grid(row=2, column=4,columnspan=1,padx=(5,5),pady=(5,5),sticky=E+W)
b_oc = Button(f3, text="(",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'('))
b_oc.grid(row=2, column=5,columnspan=1,padx=(5,5),pady=(5,5),sticky=E+W)
b_cb = Button(f3, text=")",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,')'))
b_cb.grid(row=2, column=6,columnspan=1,padx=(5,10),pady=(5,5),sticky=E+W)

b_1 = Button(f3, text="1",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'1'))
b_1.grid(row=3, column=1,columnspan=1,padx=(10,5),pady=(5,5),sticky=E+W)
b_2 = Button(f3, text="2",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'2'))
b_2.grid(row=3, column=2,columnspan=1,padx=(5,5),pady=(5,5),sticky=E+W)
b_3 = Button(f3, text="3",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'3'))
b_3.grid(row=3, column=3,columnspan=1,padx=(5,5),pady=(5,5),sticky=E+W)
b_sub = Button(f3, text="-",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'-'))
b_sub.grid(row=3, column=4,columnspan=1,padx=(5,5),pady=(5,5),sticky=E+W)
b_sq = Button(f3, text="P&SP",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12))
b_sq.grid(row=3, column=5,columnspan=1,padx=(5,5),pady=(5,5),sticky=E+W)
b_sqrt = Button(f3, text="%sqrt",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12))
b_sqrt.grid(row=3, column=6,columnspan=1,padx=(5,10),pady=(5,5),sticky=E+W)

b_0 = Button(f3, text="0",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'0'))
b_0.grid(row=4, column=1,columnspan=1,padx=(10,5),pady=(5,10),sticky=E+W)
b_deci = Button(f3, text=".",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'.'))
b_deci.grid(row=4, column=2,columnspan=1,padx=(5,5),pady=(5,10),sticky=E+W)
b_per = Button(f3, text="AC",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_clear(expr_inp))
b_per.grid(row=4, column=3,columnspan=1,padx=(5,5),pady=(5,10),sticky=E+W)
b_add = Button(f3, text="+",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica", 12),command= lambda: action_append(expr_inp,'+'))
b_add.grid(row=4, column=4,columnspan=1,padx=(5,5),pady=(5,10),sticky=E+W)
b_eq = Button(f3, text="=",bg="#434343",fg="#FFFFFF",highlightthickness=0,font=("Helvetica",12),command= lambda: action_solve(expr_inp))
b_eq.grid(row=4, column=5,columnspan=2,padx=(5,10),pady=(5,10),sticky=E+W)

root.mainloop()

