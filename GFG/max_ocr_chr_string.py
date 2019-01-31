def countMax(string):
    map = {}
    mxChr = None
    mxCount = 0
    for i in string:
        if i in map:
            map[i]+=1
        else:
            map[i]=1
        if map[i] > mxCount:
            mxCount = map[i]
            mxChr = i
    return mxChr
string = "mynameisanurag"
print (countMax(string))