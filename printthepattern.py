N=int(input())
for i in range(1,N+1,2):
    for j in range(1,N+1,1):
        print(N*(i-1)+j,end=" ")
    print()
for i in range((N//2)*2,0,-2):
    for j in range(1,N+1,1):
        print(N*(i-1)+j,end=" ")
    print()
