if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    k = tuple(integer_list)
    print(hash(k))
