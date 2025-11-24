total_rows = int(input()) #6
for row in range(1,total_rows+1):
    ans = 1
    print(ans,end=" ")
    #row generation
    for col in range(1,row):
        ans = ans*(row-col)
        ans = ans//col                                        
        print(ans,end=" ") # T.C:-0(N)
    print()     #  4
#1 
#1 1  
#1 2 1 >>1+1
#1 3 3 1>> 2+1,2+1