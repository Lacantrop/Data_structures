import random


class Stack:
	def __init__(self):
		self.stack = []

	def push(self, value):
		self.stack.append(value)

	def pop(self):
		if len(self.stack) == 0:
			return None
		else:
			return self.stack.pop()

	def __len__(self):
		return len(self.stack)

	def __repr__(self):
		return f"[{', '.join(str(item) for item in self.stack)}]"


stack = Stack()
for _ in range(10):
	stack.push(random.randint(10, 20))
print(stack)

stack.pop()
print(stack)
print(len(stack))
