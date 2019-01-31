i=int(input())
e=1
if i>1 :
	for a in range(2,i):
		if (i%a==0):
			e=0
		break
	if e==1:
		print("yes")
	else :
		print("no")
else :
	print("enter a valid number")
	
