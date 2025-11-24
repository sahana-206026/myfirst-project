def binary_search(arr, x):
	lo = 0
	hi = len(arr) - 1
	while lo <= hi:
		mid = (lo + hi) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			lo = mid + 1
		elif arr[mid] > x:
			hi = mid - 1
	return -1

if __name__ == "__main__":
	arr = list(map(int, input().split()))
	x = int(input())
	print(binary_search(arr, x))