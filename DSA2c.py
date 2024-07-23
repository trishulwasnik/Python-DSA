class Stack:
	#Constructor ---->initializaation to stack[]
	def __init__(self):
		self.stk=[]

	#check stack underflow
	def isempty(self):
		return len(self.stk)==0  #0==0 True

	#size of stack
	def size(self):
		return len(self.stk)

	#display or print
	def display(self):
		print(self.stk)

	#push Operation
	def push(self,data):
		self.stk.append(data)

	#pop operation
	def pop(self):
		if self.isempty()==True:
			print("Stack UnderFlow........")
		return self.stk.pop()

stack=Stack()
stack.display()
stack.push(10)
stack.display()
stack.push(20)
stack.display()
stack.push(30)
stack.display()
stack.push(40)
stack.display()
stack.push(50)
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()


