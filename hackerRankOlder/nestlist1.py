from operator import itemgetter

if __name__ == '__main__':
    sList = []
    i = 0
    for i in range(int(input())):
        name = input()
        score = float(input())
        sList.append([name,score])
    sSort = sorted(sList,key=itemgetter(1))
    bottom1 = sSort.pop(0)
    bottomScore = bottom1[1]

    while sSort:
        if sSort[0][1] == bottomScore:
            sSort.pop(0)
        else:
            bottom2 = sSort[0]

            break
    sSort = sorted(sSort,key=itemgetter(0))

    j =0
    for j in range(len(sSort)):
        if sSort[j][1] == bottom2[1]:
            print(sSort[j][0])
            j+=1
        else:
            j+=1






