def evalCol(N, curNum):
    width = len(str(N *N))
    smallWidth = len(str(N))
    resList = []
    for i in range(1, N + 1):
        resList.append("{0:>{3}d} * {1:<{3}d} = {2:<{width}d}".format(curNum, i, curNum * i , smallWidth, width=width, end = ""))
    maxLen = len(resList[N - 1])
    return maxLen, resList

def printEq(M):
    print(M * "=")

def vertGener(N):
    resList = [" | " for i in range(1, N + 1)]
    return resList

N, M = eval(input())
printEq(M)

res3 = vertGener(N)
resList = []
for i in range(1,N + 1):
    resList.append(evalCol(N, i))
i = 0
for j in range(0,N):
    # print(resList[i][1])
    tmp = [resList[i][1]]
    # print("len=",len(resList))
    sum = resList[i][0]
    while sum <= M and (i + 1) < N:
        i += 1
        # print("i=",i)
        sum += resList[i][0]
        tmp.append(vertGener(N))
        tmp.append(resList[i][1])
        sum += 3
    if sum > M:
        tmp.pop()
        # print('here')
        tmp.pop()
        i -= 1
    i+=1
    printList = zip(*tmp)
    for k in printList:
        print(*k, sep='')
    printEq(M)
    if i > N - 1:
        break
