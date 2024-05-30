def fact(x):
    if x == 1:
        return 1
    
    return x * fact(x - 1)


arr = [[0, 0, 1, 1], [1, 0, 0, 1], [1, 1, 1, 0], [0, 1, 0, 0]]

def number_of_islands(arr):
    count = 0
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                check_for_neighbors(arr, i, j)
                count += 1
    
    return count

def check_for_neighbors(arr, i, j):
    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[i]) or arr[i][j] == 0:
        return
    
    if arr[i][j] == 1:
        arr[i][j] = 0
    
    check_for_neighbors(arr, i - 1, j)
    check_for_neighbors(arr, i + 1, j)
    check_for_neighbors(arr, i, j - 1)
    check_for_neighbors(arr, i, j + 1)

print(number_of_islands(arr))