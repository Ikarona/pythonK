def LookSay():
    import itertools as it
    LookSayStr = '1'

    while True:
        for i in LookSayStr:
            yield int(i)
        LookSayStr = ''.join(str(len(list(g))) + k  for k, g in it.groupby(LookSayStr))

