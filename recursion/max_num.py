def max_num(arr):
    if len(arr) == 1:
        return arr[0]
    
    if arr[0] > max_num(arr[1:]):
        return arr[0]
    else:
        return max_num(arr[1:])

print(max_num([9, 6, 3, 10, 8, 2]))