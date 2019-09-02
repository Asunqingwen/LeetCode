# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 0002 16:17
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Print in Order.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

 

Example 1:

Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.

Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seems to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.
"""
from threading import Thread, Condition


def One():
	print('one', end='')


def Two():
	print('two', end='')


def Three():
	print('three', end='')


class Foo:
	def __init__(self):
		self.cd = Condition()
		self.NUM = 0

	def first(self, printFirst: 'Callable[[], None]') -> None:
		# printFirst() outputs "first". Do not change or remove this line.
		with self.cd:
			while self.NUM != 0:
				self.cd.wait()
			printFirst()
			self.NUM += 1
			self.cd.notify_all()

	def second(self, printSecond: 'Callable[[], None]') -> None:
		# printSecond() outputs "second". Do not change or remove this line.
		self.cd.acquire()
		while self.NUM != 1:
			self.cd.wait()
		printSecond()
		self.NUM += 1
		self.cd.notify_all()
		self.cd.release()

	def third(self, printThird: 'Callable[[], None]') -> None:
		# printThird() outputs "third". Do not change or remove this line.
		self.cd.acquire()
		while self.NUM != 2:
			self.cd.wait()
		printThird()
		self.NUM += 1
		self.cd.notify_all()
		self.cd.release()


if __name__ == '__main__':
	foo = Foo()
	call_list = [foo.first, foo.second, foo.third]
	call_args = [One, Two, Three]
	order = [2, 1, 3]
	A = Thread(target=call_list[order[0] - 1], args=(call_args[order[0] - 1],))
	B = Thread(target=call_list[order[1] - 1], args=(call_args[order[1] - 1],))
	C = Thread(target=call_list[order[2] - 1], args=(call_args[order[2] - 1],))
	A.start()
	B.start()
	C.start()
