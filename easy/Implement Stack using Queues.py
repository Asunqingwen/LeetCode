# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 0024 11:23
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Implement Stack using Queues.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""


class MyStack:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.data = []

	def push(self, x: int) -> None:
		"""
		Push element x onto stack.
		"""
		self.data.append(x)

	def pop(self) -> int:
		"""
		Removes the element on top of the stack and returns that element.
		"""
		return self.data.pop()

	def top(self) -> int:
		"""
		Get the top element.
		"""
		return self.data[-1]

	def empty(self) -> bool:
		"""
		Returns whether the stack is empty.
		"""
		return not self.data


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
if __name__ == '__main__':
	obj = MyStack()
	obj.push(3)
	param_2 = obj.pop()
	param_3 = obj.top()
	param_4 = obj.empty()
