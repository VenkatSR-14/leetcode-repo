class myHashset:

	def __init__(self):
		pass

	def add(self, key: int) -> None:
		pass

	def delete(self, key: int) -> None:
		pass

	def contains(self, key: int) -> bool:
		pass


class ListNode:
	def __init__(self, val, next_val: ListNode):
		self.val = val
		self.next = next_val


class Bucket:
	def __init__(self):
		self.head = ListNode(0)

	def add(self, key):
		curr = self.head
		if not exists(key):
			new_node = ListNode(key, self.head.next)
			self.head.next = new_node

	def delete(self, key):
		curr = self.head
		if not exists(key):
			return
		prev = self.head
		curr = self.head.next

		while curr is not None:
			if curr.val == key:
				prev.next = curr.next
				return
			curr = curr.next
			prev = prev.next

	def exists(self, key):
		curr = self.head.next
		while curr:
			if curr.val == key:
				return True

			curr = curr.next
		return False
		



