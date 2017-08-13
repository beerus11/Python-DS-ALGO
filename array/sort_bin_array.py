#Sort binary array in linear time
arr= [0, 1, 0, 1, 0, 0, 1, 1, 1, 0,0,0,1,1]
l=len(arr)
cz=0
for i in xrange(0,l):
    if arr[i]==0:
        cz+=1
for j in xrange(0,l):
    if j<cz:
        arr[j]=0
    else:
        arr[j]=1
print arr
