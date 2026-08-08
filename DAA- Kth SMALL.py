def mom(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(g)[len(g)//2] for g in groups]

    pivot = mom(medians, len(medians)//2)

    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k < len(low):
        return mom(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return mom(high, k - len(low) - len(equal))

arr = [12, 3, 5, 7, 19, 26, 4]
k = 3
print(mom(arr, k))
