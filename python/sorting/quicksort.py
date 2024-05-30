def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        pivot = arr[mid]
        less = [num for num in arr if num < pivot]
        greater = [num for num in arr if num > pivot]
        
        return quicksort(less) + [pivot] + quicksort(greater)


random = [4, 2, 9, 5, 1, 7, 3]
print(quicksort(random))