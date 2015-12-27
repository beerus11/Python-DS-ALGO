__author__ = 'Anurag Goel'

class Node:
    def init(self):
        self.data=None
        self.next=None
    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next=next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next!=None

print "Enter No of Elements to Insert : "
num=int(input())
length=num
head=None
tail=None
while(num!=0):
    if length==num:
        head=Node()
        head.setData(int(input("Enter a No to Insert : ")))
        tail=Node()
        head.setNext(tail)
    else:
        tail.setData(int(input("Enter a No to Insert : ")))
        node=Node()
        tail.setNext(node)
        tail=node
    num=num-1
    
print "Elements In Linked List After Insertion : "
while(length):
    print head.getData()
    head=head.getNext()
    length=length-1