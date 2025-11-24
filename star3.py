num=int(input())
for row in range(num):
    for col in range(row):
        print("*", end=" ") 
    for col in range(2*num-2*row-1):
        print("*", end=" ")
    print()