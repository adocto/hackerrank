def print_formatted(number):
    # your code goes here
    i = 1
    number = number
    for i in range(number):
        print("%d" % number + "%s" %(number," ") + "%d" % oct(number) + "%s" %(number," ") + "%d" %hex(number).capitalize() + "%d" % bin(number))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)