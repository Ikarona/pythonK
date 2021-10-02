inputString = ""
firstInput = str(input())
stringList = []
stringList.append(firstInput)
while( "-" not in inputString ):
    inputString = str(input())
    stringList.append(inputString)
rectNum = 0
maxStrLen, rawsNum = len(firstInput), len(stringList)
# for numi, i in enumerate(stringList):
for numi in range(1, rawsNum):
    # for num in enumerate(stringList[numi]):
    for num in range(maxStrLen):
        # print("i = ", stringList[numi], "num = ", num, "rectNum = ", rectNum)
        if stringList[numi][num] == "#":
            rectNum += 1
            ii = numi
            numnum = num
            while ii < rawsNum and stringList[ii][numnum] != "." :
                while numnum < maxStrLen and stringList[ii][numnum] != ".":
                    # print("ii = ", ii, "numnum = ", numnum, "str = ", "".join(stringList[ii][:numnum]+ "." + stringList[ii][numnum + 1:]))
                    stringList[ii] = stringList[ii][:numnum]+ "." + stringList[ii][numnum + 1:]

                    numnum+=1
                numnum = num

                ii+=1
            # num = numnum

print(rectNum)

# for i in stringList:
#     print(*i)
