def KnuthMorrisPratt(text, pattern):
    pattern = list(pattern)
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and (pattern[pos] != pattern[pos-shift] and pattern[pos - shift] != "@"):
            shift += shifts[pos-shift]
        shifts[pos+1] = shift
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and (pattern[matchLen] != c \
              and pattern[matchLen] != "@"):
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            return startPos
    return -1
s = input()
subs = input()
res = KnuthMorrisPratt(s, subs)
print((res))