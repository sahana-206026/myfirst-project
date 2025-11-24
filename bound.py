def subsets(nums):
    def generate(ind, curr_subset):
        # base case: when we reached the end of nums
        if ind == len(nums):
            ans.append(curr_subset.copy())
            return
        
        # include nums[ind]
        curr_subset.append(nums[ind])
        generate(ind + 1, curr_subset)
        curr_subset.pop()   # backtrack

        # exclude nums[ind]
        generate(ind + 1, curr_subset)

    ans = []
    generate(0, [])
    return ans


# input
nums = list(map(int, input("Enter numbers: ").split()))
print(subsets(nums))
