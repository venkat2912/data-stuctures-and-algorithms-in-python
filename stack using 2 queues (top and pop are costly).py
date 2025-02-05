from collections import deque
class stack:
    def __init__(self):
        self.q1=deque()
        self.q2=deque()
    def push(self,x):
        self.q1.append(x)

    def pop(self):
        # if no elements are there in q1
        #here in pop q1 is pushed in q2 except last element which is held and returned
        #as pop and after that q1 and q2 are swapped.

        if not self.q1:
            return
        #Leave one element in q1 and push others in q2
        while (len(self.q1) != 1):
            self.q2.append(self.q1.popleft())
            # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

    def top(self):
        #in top after storing the last element left in q1 it is also pushed in q2 and both are then q1 and q2 are swapped.  
        # if no elements are there in q1
        if (not self.q1):
            return
        # Leave one element in q1 and push others in q2
        while(len(self.q1) != 1):
            self.q2.append(self.q1.popleft())

        # Pop the only left element from q1 to q2
        top = self.q1[0]
        self.q2.append(self.q1.popleft())

        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

        return top

    def size(self):
        return len(self.q1)
s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)





