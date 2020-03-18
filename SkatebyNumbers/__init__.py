if __name__ == "__main__":
    speed = 1
    N = input()
    heights = []
    heights.append(input())
    x = 0
    for x in range(0,N-1):
        if x == 0:
            speed = 1
        else:
            if heights[x] > heights[x-1]:
                speed -= 1
            else:
                speed += 1
    print(speed)

