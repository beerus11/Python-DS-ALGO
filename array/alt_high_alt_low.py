#Rearrange the array with alternate high and low elements
arr=[1,2,3,4,5,6,7,8,9]
arr=sorted(arr)
l=len(arr)
for i in xrange(1,l/2):
    if i%2==0:
        continue
    temp=arr[l-i]
    arr[l-i]=arr[i]
    arr[i]=temp
print arr
