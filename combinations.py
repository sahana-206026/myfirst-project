def combinationSum(candidates, target):
    def generate(int, curr_subset, ans, target):
        # base case: target reached
        if target == 0:
            ans.append(curr_subset.copy())
            return
        # base case: end of list or target < 0
        if int == len(candidates) or target < 0:
            return

        # include candidates[ind]
        curr_subset.append(candidates[int])
        generate(int, curr_subset, ans, target - candidates[int])
        curr_subset.pop()

        # exclude candidates[ind]
        generate(int + 1, curr_subset, ans, target)

    ans = []
    generate(0, [], ans, target)
    return ans
# input
candidates = list(map(int, input("Enter candidates: ").split()))
target = int(input("Enter target: "))
print(combinationSum(candidates, target))
