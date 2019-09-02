# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 0002 16:39
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Print FooBar Alternately.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads. Thread A will call foo() while thread B will call bar(). Modify the given program to output "foobar" n times.

 

Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar(). "foobar" is being output 1 time.
"""
from threading import Thread, Condition, Lock


def Foo():
	print('foo', end='')


def Bar():
	print('bar', end='')


class FooBar1:
	def __init__(self, n):
		self.n = n
		self.flag = True
		self.cd = Condition()

	def foo(self, printFoo: 'Callable[[], None]') -> None:

		for i in range(self.n):
			# printFoo() outputs "foo". Do not change or remove this line.
			self.cd.acquire()
			while not self.flag:
				self.cd.wait()
			printFoo()
			self.flag = False
			self.cd.notify_all()
			self.cd.release()

	def bar(self, printBar: 'Callable[[], None]') -> None:

		for i in range(self.n):
			# printBar() outputs "bar". Do not change or remove this line.
			self.cd.acquire()
			while self.flag:
				self.cd.wait()
			printBar()
			self.flag = True
			self.cd.notify_all()
			self.cd.release()

class FooBar2:
	def __init__(self, n):
		self.n = n
		self.flag = True
		self.mutex1 = Lock()
		self.mutex2 = Lock()
		self.mutex2.acquire()

	def foo(self, printFoo: 'Callable[[], None]') -> None:

		for i in range(self.n):
			# printFoo() outputs "foo". Do not change or remove this line.
			self.mutex1.acquire()
			printFoo()
			self.mutex2.release()

	def bar(self, printBar: 'Callable[[], None]') -> None:

		for i in range(self.n):
			# printBar() outputs "bar". Do not change or remove this line.
			self.mutex2.acquire()
			printBar()
			self.mutex1.release()


if __name__ == '__main__':
	n = 5
	foobar = FooBar2(n)
	call_list = [foobar.foo, foobar.bar]
	call_args = [Foo, Bar]
	t1 = Thread(target=call_list[0], args=(call_args[0],))
	t2 = Thread(target=call_list[1], args=(call_args[1],))
	t1.start()
	t2.start()
