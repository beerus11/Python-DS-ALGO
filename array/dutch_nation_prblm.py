def sort(arr):
    a=0
    b=0
    for i in arr:
        if i==0:
            a+=1
        elif i==1:
            b+=1
    for j in range(0,len(arr)):
        if j <a:
            arr[j]=0
        elif j >=a and j <b+a:
            arr[j]=1
        elif j >=b+a:
            arr[j]=2
    return arr


arr = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
print sort(arr)
