array=[1,2,3,4]
frmt="{0:0%sb}"%len(array)
num=map(frmt.format,range(pow(2,len(array))))
for i in num:
    temp=list()
    l=list(i)
    for j in xrange(0,len(i)):
        if l[j]=='1':
            temp.append(array[j])
    print temp
