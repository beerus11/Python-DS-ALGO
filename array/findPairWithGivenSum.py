
##Complexity O(N^2)
def findPair(arr,sum):
    for i in xrange(0,len(arr)):
        for j in xrange(1,len(arr)-1):
            if arr[i]+arr[j]==sum:
                return [arr[i],arr[j]]

##Complexity O(NLogN)
def findPair2(arr,sum):
    arr.sort() ##O(NLogN)
    low=0
    high=len(arr)-1
    for j in range(0,len(arr)):
        if arr[low]+arr[high]==sum:
            return [arr[low],arr[high]]
        elif arr[low]+arr[high]>sum:
            high-=1
        elif arr[low]+arr[high]<sum:
            low-=1

##Complexity O(N)
def findPair3(arr,sum):
    dict={}
    for i in range(0,len(arr)):
        if (sum-i) in dict:
            return [arr[i],sum-arr[i]]
        else:
            dict[arr[i]]=i
arr = [8, 7, 2, 5, 3, 1]
print findPair3(arr,10)
