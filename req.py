from collections import Counter
arr=list(map(int,input("enter a arr:").split()))
d= Counter(arr)
u_d= sorted(d.items(),key=lambda x: (x[1], -x[0]))
result=[]
for key,value in u_d:
    for i in range(value):
        result.append(key)
print(result)
