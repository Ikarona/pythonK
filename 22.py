from itertools import *
def chainslice(begin, end, *args):
    res = chain(*args)
    it = 0
    while it < end:
        if it < begin:
            next(res)
        else:
            yield next(res)
        it+=1
