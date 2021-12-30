n = int(input())
ones = True
for n in range(n,-1,-1):
    out = ["1"]*n if ones else ["0"]*n
    ones = not ones
    print("".join(out))
            
