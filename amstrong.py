i=int(input())
n=len(str(i))
e=0
j=i
while(j>0):
	e=e+(j%10)**n
	j=j//10
if (i==e):
	print("yes")
else:
	print("no")
