def sum(no):
    if no/10 == 0:
        return no
    return sum(no/10)+no%10
no= 297
print(sum(no))