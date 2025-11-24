def search_in_rotated_array(arr, key):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        # If element found
        if arr[mid] == key:
            return mid

        # If left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


# ✅ Example usage
arr = [4, 5, 6, 7, 0, 1, 2]
key = 1

result = search_in_rotated_array(arr, key)
print("Index of", key, "is:", result)
