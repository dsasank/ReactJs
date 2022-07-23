'''
reversing upto kth element in queue
from queue import Queue
from queue import LifoQueue
q=Queue(maxsize=5)
s=LifoQueue(maxsize=5)
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

for i in range(0,6):
    if(i<3):
        s.put(q.get())
    elif(i>=3):
        q.put(s.get())
for i in range(0,2):
    x=q.get()
    q.put(x)
for i in range(0,5):
    print(q.get())
    '''
'''
inserting elemnt fronthe latst in linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def addfirst(self,data):
        n=Node(data)
        n.next=self.head
        self.head=n
    def addlast(self,data):
        n=Node(data)
        
        if(self.head == None):
            self.head = n
            return
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.next=n
            
    def disp(self):
        if(self.head is None):
            print("empty linled list")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.next
l=ll()
l.addlast(123)
l.addlast(234)
l.addlast(34)
l.disp()
'''
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class insmid:
    def __init__(self):
        self.head=None
        
    def insert(self,middle,data):
        n=Node(data)
        n.next=middle.next
        middle.next=n
    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
        
l=insmid()
l.head=Node(1)
l2=Node(2)
l3=Node(4)
l.head.next=l2
l2.next=l3
l.insert(l2,3)
l.display()
'''
'''
#delete any value node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ope:
    def __init__(self):
        self.head=None
    def addi(self,data):
        n=Node(data)
        if(self.head==None):
            self.head=n
            return n
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.next=n
    def dele(self,key):
        x=self.head
        while(x.next is not None):
            if(x.next.data==key):
                x.next=x.next.next
            x=x.next
    
        
    def display(self):
        n=self.head
        while(n is not None):
            print(n.data)
            n=n.next
cl=ope()
cl.addi(1)
cl.addi(4)
cl.addi(55)
cl.addi(90)
cl.dele(55)
cl.display()
'''
'''
#reversing a linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ope:
    def __init__(self):
        self.head=None
    def adding(self,data):
        n=Node(data)
        if(self.head==None):
            self.head=n
            return
        else:
            temp=self.head
        
            while(temp.next is not None):
                temp=temp.next
            temp.next=n
        
    def rev(self):
        if(self.head is None):
            print("empty linked list")
        else:
            prev=None
            curr=self.head
            while(curr!=None):
                nextt=curr.next
                curr.next=prev
                prev=curr
                curr=nextt
            self.head=prev
    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
o=ope()
o.adding(1)
o.adding(2)
o.adding(56)
o.adding(3)
o.rev()
o.display()
'''
'''
sorting a linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ope:
    def __init__(self):
        self.head=None
    def ad(self,data):
        n=Node(data)
        if(self.head==None):
            n=Node(data)
            self.head=n
            return
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.next=n
    def sort(self):
        curr=self.head
        index=None
        while(curr is not None):
            index=curr.next
            while(index is not None):
                if(curr.data>index.data):
                    a=curr.data
                    b=index.data
                    index.data=a
                    curr.data=b
                index=index.next
            curr=curr.next
             
    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
o=ope()
o.ad(1)
o.ad(20)
o.ad(4)
o.ad(3)
o.sort()
o.display()
'''
        
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ope:
    def __init__(self):
        self.head=None
    def ad(self,data):
        n=Node(data)
        if(self.head==None):
            n=Node(data)
            self.head=n
            return
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.next=n
    def tad(self,data1,data2):
        newnode=Node()
        curr=newnode.head
        while(data1 is not None and data2 is not None):
            if(data1.data<data2.data):
                curr.next=data1
                daata1=data1.next
            else:
                curr.next=data2
                data2=data2.next
            curr=curr.next
        if(l1.next is not None):
            curr.next=l1
        else:
            curr.next=l2
            
                
    
      
        
    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
o=ope()
p=ope()
o.ad(1)
o.ad(20)
o.ad(87)
p.ad(4)
p.ad(3)
o.tad(o,p)
p.display()
        

                
                
        




    
