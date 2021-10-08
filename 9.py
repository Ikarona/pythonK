def divdigit(N: int)->int:
    M = N
    num = 0
    while M > 0:
        tmp = M % 10
        if tmp != 0 and N % tmp == 0:
            num += 1
        M = M // 10
    return num
