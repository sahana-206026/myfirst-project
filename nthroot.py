# Program to find the Nth root of a number using formula

M = float(input("Enter the number (M): "))
N = float(input("Enter the value of N: "))

root = M ** (1/N)

print(f"The {N}th root of {M} is: {root}")
