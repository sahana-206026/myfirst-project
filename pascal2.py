row=int(input())
col=int(input())
ans=1
n=row-1
r=col-1
for i in range(r):
    ans=ans*(n-i)
    ans=ans//(i+1)
print(ans)