i,p=map(int,input().split())
for j in range(i,p+1):
	e=0
	n=len(str(j))
	a=j
	while(a>0):
		e=e+(a%10)**n
		a=a//10
	if e==j:
		print(j)
