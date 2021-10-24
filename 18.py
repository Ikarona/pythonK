def generate(maxNum):
    import math
    maxSet = set()
    for i in range(1, int(math.sqrt(maxNum)) + 1):
        ii = i * i
        for j in range(i, int(math.sqrt(maxNum - ii)) + 1):
            jj = j * j
            for k in range(j, int(math.sqrt(maxNum - ii - jj)) + 1):
                maxSet.add( ii + jj + k * k)
    return maxSet

def main():
    seq = set(eval(input()))
    maxNum = max(seq)
    maxSet = generate(maxNum)
    print(len(seq.intersection(maxSet)))


if __name__ == "__main__":
    main()