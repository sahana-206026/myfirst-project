from collections import Counter
def majorityElements(nums):
    d=Counter(nums)
    n=len(nums)
    result=[]
    for key,value in d.items():
        if(value>n/3):
            result.append(key)
            return result
num=list(map(int,input("enter a num:").split()))
print(majorityElements(num))