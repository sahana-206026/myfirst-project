def generateParenthesis(n):
    def generate(curr_str, open_count, close_count, ans, n):
        # if length reached and balanced
        if open_count == n and close_count == n:
            ans.append(curr_str)
            return
        # try to add "("
        if open_count < n:
            generate(curr_str + "(", open_count + 1, close_count, ans, n)
        # try to add ")"
        if close_count < open_count:
            generate(curr_str + ")", open_count, close_count + 1, ans, n)

    ans = []
    generate("", 0, 0, ans, n)
    return ans

# take input
n = int(input("Enter n:"))
print(generateParenthesis(n))
