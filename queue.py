import random


class Queue:
	def __init__(self):
		self.queue = []

	def push(self, value):
		self.queue.append(value)

	def pop(self):
		if len(queue) == 0:
			return None
		return self.queue.pop(0)

	def front(self):
		return self.queue[0]

	def __len__(self):
		return len(self.queue)

	def __repr__(self):
		return f"{self.queue}"


queue = Queue()
for _ in range(10):
	queue.push(random.randint(-10, 10))

print(queue)
print(queue.pop())
print(queue)
queue.push(1000)
print(queue.front())
for _ in range(len(queue)):
	queue.pop()
print(queue.pop())
print(queue)
