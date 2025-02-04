

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def isEmpty(self):
        return self.front and self.rear
    def enqueue(self,new_data):
        new_node=Node(new_data)
        if self.rear is None:
            self.front=self.rear=new_node
            return
        self.rear.next=new_node #last node pointer set to new added last
        self.rear=new_node # last made rear
    def dequeue(self):
        if self.isEmpty():
            print('Empty')
            return
        temp=self.front
        self.front=self.front.next
        if self.front is None:
            self.rear=None
    def get_front(self):
        if self.isEmpty():
            print('Queue is empty')
            return 'empty'
        return self.front.data

    def get_rear(self):

        # Checking if the queue is empty
        if self.is_empty():
            print("Queue is empty")
            return float('-inf')
        return self.rear.data
    

    
