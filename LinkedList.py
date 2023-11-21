class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def add_node(self, data):
		new_node = Node(data)

		if not self.head:
			self.head = new_node
			return
		current = self.head

		while current.next:
			current = current.next
		current.next = new_node

	def show_nodes(self):
		current = self.head
		while current:
			if current.next is None:
				print(current.data)
			else:
				print(current.data, end=" --> ")
			current = current.next


linked_list = LinkedList()

linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)

linked_list.show_nodes()

