class Node:
	def __init__(self, data):
		self.item = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.start_node = None

	# Insert Element to Empty List
	def insert_to_emptylist(self, data):
		if self.start_node is None:
			new_node = Node(data)
			self.start_node = new_node
		else:
			print("The list is empty")

	# Insert element at the end
	def insert_to_end(self, data):
		# Check if the list is empty
		if self.start_node is None:
			new_node = Node(data)
			self.start_node = new_node
			return
		n = self.start_node
		# Iterate till the next reaches NULL
		while n.next is not None:
			n = n.next
		new_node = Node(data)
		n.next = new_node
		new_node.prev = n

	# Delete the elements from the start
	def delete_at_start(self):
		if self.start_node is None:
			print("The Linked List is empty, no element to delete")
			return
		if self.start_node.next is None:
			self.start_node = None 
			return
		self.start_node = self.start_node.next
		self.start_prev = None;

	# Delete the elements from the end
	def delete_at_end(self):
		# Check if the List is empty
		if self.start_node is None:
			print("The Linked list is empty, no element to delete")
			return
		if self.start_node.next is None:
			self.start_node = None
			return
		n = self.start_node
		while n.next is not None:
			n = n.next
		n.prev.next = None 

	# Traversing and displaying each element of the list
	def display(self):
		if self.start_node is None:
			print("The list is empty")
			return
		else:
			n = self.start_node
			while n is not None:
				print("Element is: ", n.item)
				n = n.next
		print("\n")


new_doubly_linkedlist = DoublyLinkedList()

#Insert the element to empty list
new_doubly_linkedlist.insert_to_emptylist(10)

# Insert at the end
new_doubly_linkedlist.insert_to_end(20)
new_doubly_linkedlist.insert_to_end(30)
new_doubly_linkedlist.insert_to_end(40)
new_doubly_linkedlist.insert_to_end(50)
new_doubly_linkedlist.insert_to_end(60)

# Display data
new_doubly_linkedlist.display()

# Delete elements at start
new_doubly_linkedlist.delete_at_start()

# Delete elements at end
new_doubly_linkedlist.delete_at_end()

new_doubly_linkedlist.display()