class quene:
	def __init__(self,size):
		self.size=size 
		self.top=-1
		self.tail=-1
		self.quene=[]
	def empty(self):
		if self.top==self.tail:
			return True
		else:
			return False	
	def full(self):
		if self.tail-self.top+1==self.size:
			return True
		else:
			return False
	def inQuene(self,content):
		if not self.full():
			self.quene.append(content)
			self.tail+=1
		else:
			print("the quene is full ")
	def outQuene(self):
		if not self.empty():
			self.top+=1
		else:
			print("the quene is empty")
