def swap_case(s):
    i = 0
    sList = []
    j = 0


    for j in range(len(s)):
        sList.append(s[j])
    for i in range(len(sList)):
        n = sList[i].isupper()
        if n == True:
            sList[i] = sList[i].lower()
        else:
            sList[i] = sList[i].upper()
    result = ''.join(sList)
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)