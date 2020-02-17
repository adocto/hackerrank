def split_and_join(line):
    # write your code here
    newLine = line.split(" ")
    result = "-".join(newLine)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)