##Complexity O(logN)
def findNo(arr):
    for i,j in enumerate(arr):
        if i <j:
            return j

arr= [0, 1, 2, 6, 9, 11, 15]
print findNo(arr)
