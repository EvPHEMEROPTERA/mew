def max_check(a,m):
	if a > m:
		m = a
	return m

def div_check(a,b):
	bo = False
	if a % b == 0:
		bo = True
	return bo

def last_sort(b):
	if b[3] != None and b[4] != None: 
			if b[3] > b[4]:
				dub = b[4]
				b[4] = b[3]
				b[3] = dub
	return b

b = [None for i in range(0,5)]

n = int(input())
for i in range(0,n):
	a = int(input())
	if div_check(a,14):
		if b[3] != None and b[4] != None: 
			if a > b[3] and a <= b[4]:
				b[3] = a
			elif a > b[4]:
				b[3] = b[4]
				b[4] = a
		elif b[4] == None:
			b[4] = a
		else:
			b[3] = a
	else:
		if div_check(a,7):
			if a > b[2] or b[2] == None:
				b[2] = a
			elif a > b[0] or b[0] == None:
				b[0] = a
		elif div_check(a,2):
			if a > b[1] or b[1] == None:
				b[1] = a
		elif a > b[0] or b[0] == None:
				b[0] = a
	b = last_sort(b)

ma = None
if b[1] != None and b[2] != None:
	ma = b[1] * b[2]
for i in range(0,4):
	if b[i] != None and b[4] != None:
		ma = max_check(b[i] * b[4],ma)
print(ma)