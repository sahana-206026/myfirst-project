arr = list(map(int, input("Enter numbers: ").split()))
n = len(arr)
total_subsets = (1 << n)  # 2^n
ans = []

for num in range(total_subsets):  # loop through all bitmasks
    curr_subset = []
    for i in range(n):
        if (num & (1 << i)) != 0:   # check if i-th bit is set
            curr_subset.append(arr[i])
    ans.append(curr_subset)

print(ans)

