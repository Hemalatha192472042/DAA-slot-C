def max_min(arr, low, high):
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2

    max1, min1 = max_min(arr, low, mid)
    max2, min2 = max_min(arr, mid + 1, high)

    return max(max1, max2), min(min1, min2)

arr = [100, 11, 445, 1, 330, 3000]
mx, mn = max_min(arr, 0, len(arr)-1)
print("Maximum =", mx)
print("Minimum =", mn)
