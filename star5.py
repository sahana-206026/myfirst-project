n=int(input())
for row in range(n):
    for col in range(row+1):
        if((row+col)%2==0):
            print(1,end="")
        else:
            print(0,end="")
    print()