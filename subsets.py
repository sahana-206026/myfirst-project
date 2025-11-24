def subsets(nums):
    def generate(ind, ans, curr_subset):
        
        if ind == len(nums):
            ans.append(curr_subset.copy())
            return
        
        curr_subset.append(nums[ind])
        generate(ind + 1, ans, curr_subset)
        curr_subset.pop()   # backtrack

        
        generate(ind + 1, ans, curr_subset)

    ans = []
    generate(0, ans, [])
    return ans


# input
nums = list(map(int, input("Enter numbers: ").split()))
print(subsets(nums))
