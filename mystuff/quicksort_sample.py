# Started with Quicksort

# Quick Sort
# pick a pivot and start and end
# sort everything in the list to either the right or left

example = [3, 9, 1, 4, 7]


def quicksort(inp):
    # base case is if inp is empty
    if len(inp) == 0:
        return []
    if len(inp) == 1:
        return inp
    # pick pivot
    pivot = inp[len(inp) // 2]
    # create lesser, greater, equal arrays
    lesser, greater, equal = [], [], []

    # going through array put elements in corresponding sub array.
    for i in inp:

        # put values into the different arrays based on comparison to pivot
        if pivot == i:
            equal.append(i)
        elif i < pivot:
            lesser.append(i)
        else:
            greater.append(i)
    # pass smaller array into quicksort

    # submit to quicksort to review again for smaller arrays
    # combine the lists and output
    return quicksort(lesser) + equal + quicksort(greater)


quicksort(example)
print(quicksort(example))
