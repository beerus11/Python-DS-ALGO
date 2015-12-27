__author__ = 'Anurag Goel'

class Node:
    def __init__(self):
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
        
class SLL:
    def __init__(self):
        self.length=0
        
    def listLength(self):
        current =self.head
        count=0
        while current !=None:
            count=count+1
            current=current.getNext()
        return count
        
    def insertAtEnd(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.length ==0:
            self.head=newNode
            self.tail=newNode
        else :
            self.tail.setNext(newNode)
            self.tail=newNode
        self.length+=1
        
    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.length ==0:
            self.head=newNode
            self.tail=newNode
        else :
            newNode.setNext(self.head)
            self.head=newNode
        self.length+=1
        
    def insertAtPos(self,pos,data):
        if pos > self.length or pos < 0 :
            return None
        else :
            if pos == 0:
                self.insertAtBeginning(data)
            elif pos == self.length :
                self.insertAtEnd(data)
            else :
                newNode = Node()
                newNode.setData(data)
                count=0
                current=self.head
                while count<pos-1:
                    count=count+1
                    current=current.getNext()
                newNode.setNext(current.getNext())
                current.setNext(newNode)   
                self.length+=1
                
    def deleteFromBeginning(self) :
        if self.length==0:
            print "This list is empty"
        else :
            self.head=self.head.getNext()
            self.length-=1  
                
    def deleteFromEnd(self) :
        if self.length==0:
            print "This list is empty"
        else :
            currentNode =self.head
            previousNode =self.head
            while currentNode.getNext()!=None:
                previousNode=currentNode
                currentNode=currentNode.getNext()
            previousNode.setNext(None)
            self.length-=1 
            
    def printAllElements(self):
        newNode=self.head
        while newNode :
            print newNode.getData()
            newNode=newNode.getNext()
    def clear(self):
        self.head=None
        self.tail=None
        self.length=0
       
sll = SLL()             
while True :
    choice = int(input("Enter Your Choice :\n\
1)Insert From Beginning \n2)Insert From End \n3)Insert at Positon \n\
4)Delete From Beginning \n5)Delete From End \n\
6)Print Length \n7)Print List \n8)Clear List\n9)Exit\n"))
    if choice == 1 :
        sll.insertAtBeginning(input("Enter a No to insert at Beginning"))
    elif choice == 2 :
        sll.insertAtEnd(input("Enter a No to insert At End"))
    elif choice == 3 :
        pos= int(input("Enter a Position"))
        element =int(input("Enter a Element"))
        sll.insertAtPos(pos,element)       
    elif choice == 4 :
        sll.deleteFromBeginning()
    elif choice == 5 :
        sll.deleteFromEnd()
    elif choice == 6 :
        print sll.listLength()
    elif choice == 7 :
        sll.printAllElements()
    elif choice == 8 :
        sll.clear()
    elif choice == 9 :
        break
    else :
        break
    
                           

       