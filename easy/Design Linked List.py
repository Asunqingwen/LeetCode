# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 0024 14:11
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Design Linked List.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
Note:

All values will be in the range of [1, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in LinkedList library.
"""


class MyLinkedList:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.data = []
		self.size = len(self.data)

	def get(self, index: int) -> int:
		"""
		Get the value of the index-th node in the linked list. If the index is invalid, return -1.
		"""
		if index < 0 or index >= self.size:
			return -1
		return self.data[index]

	def addAtHead(self, val: int) -> None:
		"""
		Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
		"""
		self.data.insert(0, val)
		self.size += 1

	def addAtTail(self, val: int) -> None:
		"""
		Append a node of value val to the last element of the linked list.
		"""
		self.data.append(val)
		self.size += 1

	def addAtIndex(self, index: int, val: int) -> None:
		"""
		Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
		"""
		if index > self.size:
			return
		elif index < 0:
			self.data.insert(0, val)
		elif index == self.size:
			self.data.append(val)
		else:
			self.data.insert(index, val)
		self.size += 1

	def deleteAtIndex(self, index: int) -> None:
		"""
		Delete the index-th node in the linked list, if the index is valid.
		"""
		if 0 <= index < self.size:
			self.data.pop(index)
			self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
if __name__ == '__main__':
	obj = MyLinkedList()
	print(obj.data)
	obj.addAtHead(1)
	print(obj.data)
	obj.addAtTail(3)
	print(obj.data)
	obj.addAtIndex(1, 2)
	print(obj.data)
	obj.get(1)
	print(obj.data)
	obj.deleteAtIndex(1)
	print(obj.data)
	obj.get(1)
	print(obj.data)
