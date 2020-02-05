from unittest import TestCase, main


def median(arr1, arr2):
    # initialize empty array (3rd arry)
    arr3 = []
    i = 0
    j = 0
    # sorted merge of the 2 array while i < len(arr1) && j < len(arr2)
    while i < len(arr1) and j < len(arr2):
        # If arr1[i] < arr2[j] put in 3rd array and  i++
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i += 1
            if i == len(arr1):
                #   if i == length of arr1 append rest of array 2
                arr3.append(arr2[j:][0])
        else:  # esle put arr2[j] in 3rd array and j++
            arr3.append(arr2[j])
            j += 1
            if j == len(arr2):  # if j == length of arr2 append rest of array 1
                print(arr1[i:][0])
                arr3.append(arr1[i:][0])

    if len(arr3) % 2 == 1:
        print(' 1 ', arr3)
        return arr3[(len(arr3) // 2)]
    else:
        return arr3[len(arr3) // 2] + arr3[(len(arr3) + 1) // 2
        # )/2

        # If len array 3 is odd return middle index value
        # if length is even return average of two middle index values


class Tester(TestCase):
    def test_1(self):
        self.assertEqual(median([1, 12, 13, 26, 38], [2, 15, 17, 30, 45]), 16)


main()

