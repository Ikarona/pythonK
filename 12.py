def BinPow(a, N, f):
    res = a
    N = N -1
    while N:
        if N & 1:
            res = f(res,a)
        a = f(a, a)
        N >>= 1
    return res
