from pprint import pprint

def printerQuadra(N: int, M: int):
    a = [[-1 for i in range(M)] for j in range(N)]
    size = N * M
    i = 0
    k = 0
    num = 0
    while( i < size ):
        k += 1
        # верхняя строка
        for j in range( k - 1, M - k + 1 ):
            a[k - 1][j] = num % 10
            num += 1
            i += 1

        if i >= size:
            break
        # правый столбец
        for j in range(k, N - k + 1):
            # print("here2")
            a[j][M - k] = num % 10
            num += 1
            i += 1

        if i >= size:
            break

        #нижняя строка
        for j in range(M - k - 1, k-1 - 1, -1):
            a[N - k][j] = num % 10
            # print("here3")
            num += 1
            i += 1
        if i >= size:
            break
        # левый столбец
        for j in range(N - k - 1, k-1 , -1):
            a[j][k-1] = num % 10
            num += 1
            i += 1
    for raw in a:
        print(*raw)

N,M = eval(input())
printerQuadra(M,N)