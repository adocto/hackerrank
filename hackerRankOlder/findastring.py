def count_substring(string, sub_string):
    i = 0
    count = 0

    for i in range(len(string)-1):

        if string[i] == sub_string[0]:
            if string[i:(i + len(sub_string))] == sub_string:
                count += 1
        i +=1




    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)