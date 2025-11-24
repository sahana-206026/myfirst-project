row=int(input())
for col in range(1,row+1):
    ans=1
    n=row-1
    r=col-1
for i in range(r):
    ans=ans*(n-i)#numerator
    ans=ans//(i+1)#denominator
print(ans,end=" ")