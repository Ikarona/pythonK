def squares(w, h, *args):
    a = [['.' for i in range(w)] for j in range(h)]
    for x, y, s, c in args:
        for i in range(x, x + s):
            for j in range(y, y + s):
                a[j][i] = c
    for i in a:
        print(*i, sep='')
