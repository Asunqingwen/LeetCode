# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 0002 17:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Building H2O.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
There are two kinds of threads, oxygen and hydrogen. Your goal is to group these threads to form water molecules. There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given a releaseHydrogen and releaseOxygen method respectfully, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must be able to immediately bond with each other to form a water molecule. You must guarantee that all the threads from one molecule bond before any other threads from the next molecule do.

In other words:

If an oxygen thread arrives at the barrier when no hydrogen threads are present, it has to wait for two hydrogen threads.
If a hydrogen thread arrives at the barrier when no other threads are present, it has to wait for an oxygen thread and another hydrogen thread.
Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.

 

Example 1:

Input: "HOH"
Output: "HHO"
Explanation: "HOH" and "OHH" are also valid answers.

Constraints:

Total length of input string will be 3n, where 1 ≤ n ≤ 50.
Total number of H will be 2n in the input string.
Total number of O will be n in the input string.
"""
from threading import Thread, Lock


def Hydrogen():
	print('H', end='')


def Oxygen():
	print('O', end='')


class H2O:
	def __init__(self):
		self.lock = Lock()
		self.num_h = 0
		self.num_o = 0
		self.release_h = None
		self.release_o = None

	def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
		# releaseHydrogen() outputs "H". Do not change or remove this line.
		self.release_h = releaseHydrogen
		self.control(1, 0)

	def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
		# releaseOxygen() outputs "O". Do not change or remove this line.
		self.release_o = releaseOxygen
		self.control(0, 1)

	def control(self, h, o):
		with self.lock:
			self.num_h += h
			self.num_o += o
			if self.num_h < 2 or self.num_o < 1:
				return
			self.num_h -= 2
			self.num_o -= 1
		self.release_h()
		self.release_h()
		self.release_o()


class H2O1:
	def __init__(self):
		self.h_q, self.o_q = [], []

	def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
		self.h_q.append(releaseHydrogen)
		self.control()

	def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
		self.o_q.append(releaseOxygen)
		self.control()

	def control(self) -> None:
		if len(self.h_q) > 1 and len(self.o_q) > 0:
			self.h_q.pop(0)()
			self.h_q.pop(0)()
			self.o_q.pop(0)()


if __name__ == '__main__':
	input = "OOHHHH"
	h2o = H2O()
	for s in input:
		po = Thread(target=h2o.hydrogen, args=(Hydrogen,))
		ph = Thread(target=h2o.oxygen, args=(Oxygen,))
		po.start()
		ph.start()
