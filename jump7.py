a=0
while a<100:
	a=a+1
	if a%7==0:
		pass
	elif a//10==7:
		pass
	elif a%10==7:
		continue
	else:
		print(a)


