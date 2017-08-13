def lcs(x,y):
    m=len(x)
    n=len(y)
    k= [[0]*(n+1) for i in range(m+1)]
    for i in xrange(1,m+1):
        for j in xrange(1,n+1):
            if x[i-1]==y[j-1]:
                k[i][j]=k[i-1][j-1]+1
            else:
                k[i][j]=max(k[i-1][j],k[i][j-1])
    return k[m][n]   

X = "AGGTAB"
Y = "GXTXAYB"   

print lcs(list(X),list(Y))     