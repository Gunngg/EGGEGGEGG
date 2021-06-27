import time

# EGGEGGEGG

# at the start of the program you have 1 egg (variable) available, and every n (5?) commands turtle lays an egg (eggs stored in a list, their index is used to refer to them)

# pseudo truth machine
'''
set $0 n
is $0 0
out 0
is $0 1
🐢 5
while $0 1
out 1
'''
# value - if its a number then its a number,
# if it starts with $ then 1) if its followed by a number its $egg; 2) 'c' without quotes will return total amount of available eggs; 3) 'n' will return amount of nonzero variables; 4) 'z' will return amount of zeros (int only)
# if starts with " then everything until the end of the line is saved as a string (\n = newline, \s = space), 
# if its 'n' without quotes then it asks for input (int), if its 'i' without quotes it asks for input (str)
# -----
# set $egg value - sets value of $egg to value
# is value1 value2 - executes next line only if value1 is equal to value2
# isnot value1 value2 - executes next line only if value1 is NOT equal to value2
# while value1 value2 - while value1 is equal to value2 do the next line
# whilenot value1 value2 - while value1 is NOT equal to value2 execute the next line
# out value - output value
# turtle value - goto line number value (count from 0)
# add value1 value2 $egg - adds value1 to value2 and saves into $egg
# sub value1 value2 $egg - subtracts value2 from value1 and saves into $egg
# mult value1 value2 $egg - multiplies value1 by value2 and saves into $egg
# div value1 value2 $egg - divides value1 by value2 (integer division) and saves into $egg
# conc value1 value2 $egg - concatenate value1 and value2 and save into $egg
# toint value $egg - convert value to int if possible and save into $egg
# tostr value $egg - convert value to str and save into $egg
# free - you free the turtle

#TODO:


eggs = [0]
turtle = 0
eggcount = 1

def reset():
	global eggs,turtle,eggcount
	eggs = [0]
	turtle = 0
	eggcount = 1


def toval(xx): #xxv = xx value
	if xx[0] == '"':
		xxv = xx[1:].replace('\\n','\n').replace('\s',' ')
	elif xx[0] == '$':
		if xx[1] in ['0','1','2','3','4','5','6','7','8','9']:
			xxv = eggs[int(xx[1:])]
		elif xx[1:3] in ['-0','-1','-2','-3','-4','-5','-6','-7','-8','-9']:
			xxv = eggs[abs(int(xx[1:]))]
		elif xx[1] == 'c': #c = count
			xxv = len(eggs)
		elif xx[1] == 'n':
			xxv = 0
			for n in eggs:
				if n != 0:
					xxv += 1
		elif xx[1] == 'z':
			xxv = 0
			for n in eggs:
				if n == 0:
					xxv += 1
	elif xx.rstrip() == 'n':
		xxv = int(input('n>'))
	elif xx.rstrip() == 'i':
		xxv = input('i>')
	elif xx[0] in ['0','1','2','3','4','5','6','7','8','9']:
		xxv = int(xx)
	elif xx[0:2] in ['-0','-1','-2','-3','-4','-5','-6','-7','-8','-9']:
		xxv = int(xx)
	else:
		xxv = 0
	return xxv


def eee(abc,ln=0):
	global eggs,turtle,eggcount
	abcl = abc.split('\n')
	#comments
	win = 0
	for w in abcl:
		w2in = 0
		for w2 in w:
			if w2 == '`':
				abcl[win]=abcl[win][:w2in]
			w2in += 1
		win += 1
	#print(abcl)
	line = ln
	while line < len(abcl):
		if abcl[line].strip(' ') == '':
			line += 1
			continue
		time.sleep(turtle)
		#print(eggcount,eggs,line,abcl[line])
		i = abcl[line]
		isp = i.lstrip(' ').split(' ')
		if eggcount == 5:
			eggs.append(0)
			eggcount = 0

		# set
		if isp[0] == 'set':
			if isp[1][0] == '$':
				eggs[abs(int(isp[1][1:]))] = toval(' '.join(isp[2:]))
		# out
		elif isp[0] == 'out':
			print(toval(' '.join(isp[1:])),end='',flush=True)
		# funny goto
		elif isp[0] == 'turtle':
			if line > abs(int(isp[1])):
				while line > abs(int(isp[1]))-1:
					line -= 1
			elif line < abs(int(isp[1]))-1:
				while line < abs(int(isp[1]))-1:
					line += 1
			elif line == abs(int(isp[1])):
				line -= 1
		# if ==
		elif isp[0] == 'is':
			add = 1
			if toval(isp[1]) != toval(' '.join(isp[2:])):
				while abcl[line+add].lstrip(' ').split(' ')[0] in ['is','while']:
					add += 1
				line += add
		# if !=
		elif isp[0] == 'isnot':
			add = 1
			if toval(isp[1]) == toval(' '.join(isp[2:])):
				while abcl[line+add].lstrip(' ').split(' ')[0] in ['is','while']:
					add += 1
				line += add
		# while ==
		elif isp[0] == 'while':
			add = 1
			op1 = toval(isp[1])
			op2 = toval(' '.join(isp[2:]))
			if op1 != op2:
				while abcl[line+add].lstrip(' ').split(' ')[0] in ['is','while']:
					add += 1
				line += add
			else:
				while abcl[line+add].lstrip(' ').split(' ')[0] in ['is','while']:
					add += 1
				end = line+add
				while op1 == op2:
					if isp[1] not in ['n','i']:
						op1 = toval(isp[1])
					if isp[2] not in ['n','i']:
						op2 = toval(' '.join(isp[2:]))
					if op1 == op2:
						break
					#eee('\n'.join(abcl[line+1:end+1]))
					if abcl[end].split(' ')[0] == 'turtle':
						eee(abc,end)
					else:
						eee('\n'.join(abcl[line+1:end+1]))
				line += 1
		# while !=
		elif isp[0] == 'whilenot':
			add = 1
			op1 = toval(isp[1])
			op2 = toval(' '.join(isp[2:]))
			if op1 == op2:
				while abcl[line+add].lstrip(' ').split(' ')[0] in ['is','while']:
					add += 1
				line += add
			else:
				while abcl[line+add].lstrip(' ').split(' ')[0] in ['is','while']:
					add += 1
				end = line+add
				while op1 != op2:
					if isp[1] not in ['n','i']:
						op1 = toval(isp[1])
					if isp[2] not in ['n','i']:
						op2 = toval(' '.join(isp[2:]))
					if op1 == op2:
						break
					#eee('\n'.join(abcl[line+1:end+1]))
					if abcl[end].split(' ')[0] == 'turtle':
						eee(abc,end)
					else:
						eee('\n'.join(abcl[line+1:end+1]))
				line += 1
		# ---- MATH ----
		# add
		elif isp[0] == 'add':
			op1 = toval(isp[1]) #op1 = operation1
			op2 = toval(isp[2])

			if type(op1) == int and type(op2) == int:
				if isp[3][0] == '$':
					eggs[abs(int(isp[3][1:]))] = op1+op2
			else:
				print('\nerror (line {0}): cant add strs'.format(line),flush=True)
				break
		# sub
		elif isp[0] == 'sub':
			op1 = toval(isp[1])
			op2 = toval(isp[2])

			if type(op1) == int and type(op2) == int:
				if isp[3][0] == '$':
					eggs[abs(int(isp[3][1:]))] = op1-op2
			else:
				print('\nerror (line {0}): cant subtract strs'.format(line),flush=True)
				break
		# mult
		elif isp[0] == 'mult':
			op1 = toval(isp[1])
			op2 = toval(isp[2])

			if type(op1) == int and type(op2) == int:
				if isp[3][0] == '$':
					eggs[abs(int(isp[3][1:]))] = op1*op2
			else:
				print('\nerror (line {0}): cant multiply strs'.format(line),flush=True)
				break
		# div
		elif isp[0] == 'div':
			op1 = toval(isp[1])
			op2 = toval(isp[2])

			if type(op1) == int and type(op2) == int:
				if isp[3][0] == '$':
					eggs[abs(int(isp[3][1:]))] = op1//op2
			else:
				print('\nerror (line {0}): cant divide strs'.format(line),flush=True)
				break
		
		# conc
		elif isp[0] == 'conc':
			op1 = toval(isp[1])
			op2 = toval(isp[2])

			if type(op1) == str and type(op2) == str:
				if isp[3][0] == '$':
					eggs[abs(int(isp[3][1:]))] = op1+op2
			else:
				print('\nerror (line {0}): cant concatenate ints'.format(line),flush=True)
				break
		# toint
		elif isp[0] == 'toint':
			if isp[2][0] == '$':
				eggs[abs(int(isp[2][1:]))] = int(toval(isp[1]))
			else:
				print('\nerror (line {0}): cant save result of toint'.format(line),flush=True)
				break
		# tostr
		elif isp[0] == 'tostr':
			if isp[2][0] == '$':
				eggs[abs(int(isp[2][1:]))] = str(toval(isp[1]))
			else:
				print('\nerror (line {0}): cant save result of tostr'.format(line),flush=True)
				break
		# get
		elif isp[0] == 'get':
			if isp[2][0] == '$':
				eggs[abs(int(isp[2][1:]))] = eggs[abs(toval(isp[1]))]
			else:
				print('\nerror (line {0}): cant save result of get'.format(line),flush=True)
				break
		# free
		elif isp[0] == 'free':
			break

		line += 1
		eggcount += 1
		turtle += 0.1

	#print('end',eggs,line)


print('Welcome to the EGGEGGEGG interpreter')
while 1:
	print('Type "c" to code - use ; for newlines (then type c again to exit); "o" to open a file')
	og = input()
	if og == 'c':
		cinp = input()
		while cinp != 'c':
			eee(cinp.replace(';','\n'))
			print('/---\\')
			reset()
			cinp = input()
	elif og == 'o':
		print('Enter file path')
		oinp = input()
		oopen = open(oinp,'r')
		oread = oopen.read()
		oopen.close()
		eee(oread)
		#eee(open(input(),'r').read())
		print('/---\\')
		reset()
