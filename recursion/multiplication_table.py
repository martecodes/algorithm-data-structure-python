def multiplication_table(arr):
    table  = []
    
    for i in range(len(arr)):
        temp = []
        for j in range(len(arr)):
            temp.append(arr[i] * arr[j])
        
        table.append(temp)
    
    return table;

print(multiplication_table([2, 3, 7, 8, 10]))