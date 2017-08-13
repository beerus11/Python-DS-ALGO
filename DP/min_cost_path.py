def minCost(mat,m,n):
    x=len(mat)
    y=len(mat[0])
    k=[[0]*y for i in range(x)]
    k[0][0]=mat[0][0]
    for i in range(1,x):
        k[i][0]=k[1-1][0]+mat[i][0]

    for i in range(1,y):
        k[0][i]=k[0][i-1]+mat[0][1]

    for i in range(1,m+1):
        for j in range(1,n+1):
            minno=min(k[i-1][j],k[i][j-1],k[i-1][j-1])
            k[i][j]=minno+mat[i][j]
    return k[m][n]

cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(minCost(cost, 2, 2))