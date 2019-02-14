N,A,D=map(int,input().split())
E=0
C=0
for i in range(A,N+A):
    E=(A+(C*D))+E
    C=C+1
print(E)
