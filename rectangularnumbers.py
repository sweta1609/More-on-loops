n=int(input())
for i in range(-n+1,n):
    for j in range(-n+1,n):
        print(1+max(abs(i),abs(j)),end="")
    print()    
