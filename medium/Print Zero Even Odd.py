# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 0002 17:09
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Print Zero Even Odd.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Suppose you are given the following code:

class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // constructor
  public void zero(printNumber) { ... }  // only output 0's
  public void even(printNumber) { ... }  // only output even numbers
  public void odd(printNumber) { ... }   // only output odd numbers
}
The same instance of ZeroEvenOdd will be passed to three different threads:

Thread A will call zero() which should only output 0's.
Thread B will call even() which should only ouput even numbers.
Thread C will call odd() which should only output odd numbers.
Each of the thread is given a printNumber method to output an integer. Modify the given program to output the series 010203040506... where the length of the series must be 2n.

 

Example 1:

Input: n = 2
Output: "0102"
Explanation: There are three threads being fired asynchronously. One of them calls zero(), the other calls even(), and the last one calls odd(). "0102" is the correct output.
"""
from threading import Thread, Lock


def Number(n):
	print(n, end='')


class ZeroEvenOdd:
	def __init__(self, n):
		self.n = n
		self.num = 0
		self.mutex1 = Lock()
		self.mutex2 = Lock()
		self.mutex3 = Lock()
		self.mutex2.acquire()
		self.mutex3.acquire()

	# printNumber(x) outputs "x", where x is an integer.
	def zero(self, printNumber: 'Callable[[int], None]') -> None:
		for x in range(self.n):
			self.mutex1.acquire()
			printNumber(0)
			self.num += 1
			if self.num % 2:
				self.mutex3.release()
			else:
				self.mutex2.release()

	def even(self, printNumber: 'Callable[[int], None]') -> None:
		for x in range(2, self.n + 1, 2):
			self.mutex2.acquire()
			printNumber(self.num)
			self.mutex1.release()

	def odd(self, printNumber: 'Callable[[int], None]') -> None:
		for x in range(1, self.n + 1, 2):
			self.mutex3.acquire()
			printNumber(self.num)
			self.mutex1.release()


if __name__ == '__main__':
	n = 5
	zeroEvenOdd = ZeroEvenOdd(n)
	A = Thread(target=zeroEvenOdd.zero, args=(Number,))
	B = Thread(target=zeroEvenOdd.even, args=(Number,))
	C = Thread(target=zeroEvenOdd.odd, args=(Number,))
	A.start()
	B.start()
	C.start()
