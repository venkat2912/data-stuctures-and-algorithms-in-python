# Python3 program to implement Queue using 
# two stacks with costly enQueue() 

class Queue: 
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def enQueue(self, x):
    #[] [] a
    #[1] [] b 1 is pushed
    
    #[2] [1] b 1 is popped and pushed to s2 and 2 is pushed in s1
    #[2, 1] [] c 1 is again pushed in s1
    #[3] [1, 2] b 1 is popped and pushed in s2 then 2 is popped and pushed in s2 and 3 is pushed in s1
    #[3, 2, 1] [] c 2 is popped from s2 and pushed in s1 then 1 is popped from s2 and pushed in s1

		#push element in stack 1 then when other element comes stack1 is popped and pushed in stack2 and the new element is inserted and then elements from s2 are again popped and pushed in stack 1
		# Move all elements from s1 to s2 
		while len(self.s1) != 0: 
			self.s2.append(self.s1[-1]) 
			self.s1.pop()

		# Push item into self.s1 
		self.s1.append(x) 

		# Push everything back to s1 
		while len(self.s2) != 0: 
			self.s1.append(self.s2[-1]) 
			self.s2.pop()

	# Dequeue an item from the queue 
	def deQueue(self):
		
			# if first stack is empty 
		if len(self.s1) == 0: 
			return -1;
	
		# Return top of self.s1 
		x = self.s1[-1] 
		self.s1.pop() 
		return x

# Driver code 
if __name__ == '__main__':
	q = Queue()
	q.enQueue(1) 
	q.enQueue(2) 
	q.enQueue(3) 

	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())

