class Solution:
    def smallestDivisor(self,arr,k):
        for div in range(1,max(arr)+1):
            sum=0
            for num in arr:
                sum+=ceil(num/div)