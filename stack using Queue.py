from collections import deque
class stack:
    def __init__(self):
        self.q1=deque()
        self.q2=deque()
    def push(self,x):
        #two queue's are used here-- entry is made in q2 then the entire q1 is appended to q1 and q1 q2 are swapped. Thus q1 holds element in a way of stack
        self.q2.append(x)
        #print(self.q2)
        while(self.q1):
            self.q2.append(self.q1.popleft())
        print(self.q1,self.q2)
        self.q1, self.q2 = self.q2, self.q1
        
    def pop(self):

        # if no elements are there in q1
        if self.q1:
            self.q1.popleft()

    def pop(self):

        # if no elements are there in q1
        if self.q1:
            self.q1.popleft()

    def top(self):
        if (self.q1):
            return self.q1[0]
        return None

    def size(self):
        return len(self.q1)
s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)





