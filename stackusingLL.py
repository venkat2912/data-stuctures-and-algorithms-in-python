#dummyhead-->node1-->node2:
#new node is pushed
#newnode=dummyhead.next i.e=newnode-->node1-->node2
#dummyhead.next=newnode i.e= dummyhead-->newnode-->node1-->node2
# pop= dummyhead-->newnode-->node1-->node2
#remove=self.head.next points to newnode
# self.head.next=remove.next dummynode next is set to node1 from newnode which performs pop
#top= check if empty return None else dummyhead.next.value
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self):
        self.head=Node()
        self.size=0
    def getSize(self):
        self.size=0
    def isEmpty(self):
        return self.size==0
    def top(self):
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            return None

        return self.head.next.value
    def push(self,value):
        node=Node(value)
        node.next=self.head.next# this make the new node the head and now it will point  to the next node
        self.head.next=node
        self.size+=1
    def pop(self):
        if self.isEmpty():
            return 'Empty'
        remove=self.head.next
        self.head.next=remove.next
        self.size-=1
        return remove.value
    
            
        


