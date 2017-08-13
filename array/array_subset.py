from itertools import permutations
def printSubset(arr):
    l=list()
    for i in range(1,len(arr)+1):
        for j in range(0,len(arr)-i+1):
            l.append(arr[j:j+i])
    return l

perms = [p for p in permutations("123")]
for i in perms:
    s=set()
    for x in  printSubset(i):
        s.add(x)
print x

