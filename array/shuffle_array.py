import random
arr= [1, 2, 3, 4, 5, 6 ]
for i in range(0,len(arr)):
    index=random.randint(0,len(arr)-1)
    temp=arr[index]
    arr[index]=arr[i]
    arr[i]=temp
print arr
