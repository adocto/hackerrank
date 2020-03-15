def bubble(arr):
    for end in range(len(arr)-1,-1,-1):
        #if it is sorted no need to swap, return array
        swap = False

        for i in range(0,end):
            #check if member is greater than next
            if arr[i] > arr[i+1]:
                #swap with next member if greater
                arr[i] , arr[i+1] = arr[i+1],arr[i]
                #loop should continue as a swap has been done
                swap = True

    if swap == False:
        break
    return arr

#complexity:
#O((3/2)n^2 + 3n + 1)
#O(n^2) Quadratic
#best case Ω(n) linear if already sorted