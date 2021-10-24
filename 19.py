from collections import defaultdict

def path(inpDict, begin, end):
    beginTunnels = inpDict[begin].copy()
    addedTunnels = set()
    while True:
        newTunnels = set()
        newTunnels = newTunnels.union(beginTunnels)
        if end in newTunnels:
            print("YES")
            return
        for tonnel in beginTunnels.difference(addedTunnels):
            newTunnels = newTunnels.union(inpDict[tonnel])
            addedTunnels.add(tonnel)
        if end in newTunnels:
            print("YES")
            return
        if len(newTunnels.intersection(beginTunnels)) == len(newTunnels):
            print("NO")
            return
        beginTunnels = beginTunnels.union(newTunnels)

def main():
    d = defaultdict(set)
    i = 1
    while i != 1 << 2:
        inp = input()
        inp = inp.split(" ")
        if len(inp) == 1:
            i = i << 2
            begin = inp[0]
            end = input()
        else:
            d[inp[0]].add(inp[1])
            d[inp[1]].add(inp[0])
    path(d, begin, end)


if __name__=="__main__":
    main()
