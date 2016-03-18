class stack():
	def __init__(self,size):
		self.size=size;
		self.stack=[]
		self.top=-1
	def push(self,content):
		if self.full():
			print("the stack is full")
		else:
			self.stack.append(content)
			self.top+=1
	def full(self):
		if self.top==self.size:
			return True 
		else:
		    return False
	def empty(self):
		if self.top==-1:
			return True
	def out(self):
		if self.empty():
			print("the stack is null")
		else:
			self.top-=1	

