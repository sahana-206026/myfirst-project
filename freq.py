from collections import Counter   
s = input("enter a string:") #tree
d = Counter(s) #{t:1,r:1,e:2}
# value_sort=[(e,2),(r,1)(t,1)]
u_d= sorted(d.items(),key=lambda x: -x[1])
result=""
for key,value in u_d:
    result+=key*value
print(result)    