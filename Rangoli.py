import string

def print_rangoli(size):
    # your code goes here
    N = int(size)
    max1 = N
    center = (N*2)-2
    M = N
    stack1 = []
    line1 = []
    left = center
    right = center
    letter1 = dict(zip(range(1, 27), string.ascii_lowercase))
    i = 1
    for i in range((N*4) - 3):
        line1.append('-')


    while N > 0:
        if N == max1:
            line1[left] = letter1[M]
            print(''.join(str(elem) for elem in line1))
            stack1.append(line1[:])
            N -= 1
            M = N
        else:
            while M <= max1:
                line1[left] = letter1[M]
                line1[right] = letter1[M]

                left = left - 2
                right = right + 2
                M += 1

            N -= 1
            M = N
            left = center
            right = center
            print(''.join(str(elem) for elem in line1))
            stack1.append(line1[:])



    newline1 = stack1.pop()
    while stack1:
        newline1 = stack1.pop()
        print(''.join(str(elem) for elem in newline1))






if __name__ == "__main__":
    n = input()
    print_rangoli(n)
