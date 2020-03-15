def insertion_sort(arr):
    i = 0
#    if arr==[]:
#        return arr
    for i in range(len(arr)):
        if i == 0:
            arr[i] = arr[i]
        else:
            j = i
            for j in range(j, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break
    return arr