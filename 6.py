def segments(coord: tuple) -> int:
    listLen = len( coord )
    lstBool =  [[0,]] * ( listLen * 2 ) # (int, bool)
    for i in range(0, listLen):
        lstBool[ i * 2 ] = [coord[i][0], False]
        lstBool[ i * 2 + 1 ] = [coord[i][1], True]
    lstBool.sort(key=lambda x:x[0])
    res = 0
    overlappedSegm = 0
    for i in range(0, listLen * 2):
        if overlappedSegm and i:
            res += abs( lstBool[i][0] - lstBool[i-1][0])
        if lstBool[i][1]:
            overlappedSegm += 1
        else:
            overlappedSegm -= 1
    return res
nums = eval(input())
print(segments(nums))