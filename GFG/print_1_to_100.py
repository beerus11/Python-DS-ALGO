def printNos(n):
    if n==101:
        return
    print(n)
    printNos(n+1)

printNos(1)