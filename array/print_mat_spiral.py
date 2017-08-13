mat=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
m=len(mat)
n=len(mat[0])
i=0
j=0
f=1
while True:
    if mat[i][j] == None:
        break
    print mat[i][j]
    mat[i][j]=None
    if f==1:
        if j<n-1 and (mat[i][j+1] != None) :
            j+=1
        else:
            f=2
    if f==2:
        if i<m-1 and (mat[i+1][j] != None) :
            i+=1
        else:
            f=3
    if f==3:
        if j>0 and (mat[i][j-1] != None) :
            j-=1
        else:
            f=4
    if f==4:
        if i>0 and (mat[i-1][j] != None):
            i-=1
        else:
            f=1
            j=j+1
