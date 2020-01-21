def bubble(arr)
    for end in range(len(arr)-1,-1,-1): #O(N)
        #swap flag indicated whether the array is already sorted or not (false if already sorted)
        swap = False #O(1)
        for i in range(0,end): #O(N/2)
            #check if greater than next member
            if arr[i] > arr[i+1]: #O(1)
                #swap members
                arr[i], arr[i+1] = arr[i+1],arr[i] #O(1)
                #set swap to True if swap was made (continues loop)
                swap = True #O(1)
        #exit loop if swap is false (array is sorted)
        if swap == False: #O(1)
            break #O(1)
    #assorted array is returned.
    return arr #O(1)
#total complexity:
#O(3(n^2)/2 + 3n + 1)
#O(n^2) Quadratic
#Ω(n) Best case is linear

