if __name__ == '__main__':
    s = input()

    # In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
    isAN = False
    h = 0
    for h in range(len(s)):
        if s[h].isalnum():
            isAN = True
            break
        else:
            h +=1
    print(isAN)
    # In the second line, print True if  has any alphabetical characters. Otherwise, print False.
    isAlpha1 = False
    i = 0
    for i in range(len(s)):
        if s[i].isalpha():
            isAlpha1 = True
            break
        else:
            i +=1
    print(isAlpha1)
    # In the third line, print True if  has any digits. Otherwise, print False.
    j = 0
    isDigit1 = False
    for j in range(len(s)):
        if s[j].isdigit():
            isDigit1 = True
            break
        else:
            j+=1
    print(isDigit1)
    # In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
    k = 0
    isLower1 = False
    for k in range(len(s)):
        if s[k].islower():
            isLower1 = True
            break
        else:
            k+=1
    print(isLower1)
    # In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
    l = 0
    isUpper1 = False
    for l in range(len(s)):
        if s[l].isupper():
            isUpper1 = True
            break
        else:
            l +=1
    print(isUpper1)