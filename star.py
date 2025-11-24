n=int(input("enter a number:"))
for i in range(2* n+1):
    for j in range(2*n+1):
        dist=((i-n)**2+(j-n)**2)**0.5
        if abs(dist-n)<0.5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()