def smallest_number(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index

def selection_sort(arr):
    sorted = []
    
    for i in range(len(arr)):
        smallest = smallest_number(arr)
        sorted.append(arr.pop(smallest))
    
    return sorted

random = [4, 2, 9, 5, 1, 7, 3]

print(selection_sort(random))