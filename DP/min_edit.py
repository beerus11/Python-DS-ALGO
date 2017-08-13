def minEditDis(str1,str2,m,n):
    k= [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                k[i][j]=j
            elif j==0:
                k[i][j]=i
            elif str1[i-1]==str2[j-1]:
                k[i][j]=k[i-1][j-1]
            else:
                k[i][j]=1+min(k[i-1][j],k[i][j-1],k[i-1][j-1])
    return k[m][n]       

X="Saturday"
Y="Sunday"
print minEditDis(X,Y,len(X),len(Y))    
                


