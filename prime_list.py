i,j=map(int,input().split())
for a in range (i,j+1):
    e=0
    if a>1:
        for c in range(2,a):
            if (a%c==0):
                e=1
                break
        if e==0:
            print(a,end=" ")
