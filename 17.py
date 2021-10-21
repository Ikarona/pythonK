def GetCoord():
    inp = ''
    inputList = []
    while 1:
        inp = input()
        if inp == ".":
            break
        else:
            tmp = inp.split(' ')
            inputList.append(tuple([float(tmp[0]), float(tmp[1]), float(tmp[2]), tmp[3]]))
    return inputList

def CoordDist(first, second):
    # first = [float(i)for i in firstS]
    # second = [float(i)for i in secondS]
    return (first[0] - second[0])*(first[0] - second[0]) + \
           (first[1] - second[1])*(first[1] - second[1]) + \
           (first[2] - second[2])*(first[2] - second[2])

def MaxDist(coordList):
    maxLen = -1
    pairName = ('', '')
    listLen = len(coordList)
    for i in range(0, listLen - 1):
        for j in range(i+1, listLen):
            currLen  = CoordDist((coordList[i][0],coordList[i][1],coordList[i][2]), (coordList[j][0],coordList[j][1],coordList[j][2]))
            if currLen > maxLen:
                pairName = (coordList[i][3], coordList[j][3])
                maxLen = currLen
    return pairName

def main():
    res = MaxDist(GetCoord())
    if res[0] < res[1]:
        print(*res)
    else:
        print(res[1], res[0])

if __name__ == "__main__":
    main()
