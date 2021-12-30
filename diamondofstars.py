n = int(input())
n1=(n+1)//2
n2=(n//2)
for i in range(1,n1+1):
    print(" "*(n1-i)+"*"*(2*i-1))
for i in range(n2,-1,-1):
    print(" "*(n2-i+1)+"*"*(2*i-1))
