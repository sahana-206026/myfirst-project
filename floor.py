

class Solution:
    def floorSqrt(self, n):
        ans = 0
        for i in range(1, n + 1):
            if i * i > n:
                break
            else:
                ans = i
        return ans

obj = Solution()
n = int(input("Enter a number: "))
print("The floor square root is:", obj.floorSqrt(n))
