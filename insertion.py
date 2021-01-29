def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(insertion_sort([6,5,3,1,8,7,2,4]))