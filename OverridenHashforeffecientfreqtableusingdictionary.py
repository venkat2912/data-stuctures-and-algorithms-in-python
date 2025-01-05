def freqcustomhash(arr):
    di = dict()
    mx = 0
    for x in arr:
        wx = Wrapper(x)
        di[wx] = di.get(wx, 0) + 1
        mx = max(mx, di[wx])
    return di    
from random import randint

RANDOM = randint(1, 10 ** 9)


class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)

    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM
