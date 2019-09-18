# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 0018 10:53
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Logger Rate Limiter.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true;

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
"""


class Logger:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.data = {}

	def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
		"""
		Returns true if the message should be printed in the given timestamp, otherwise returns false.
		If this method returns false, the message will not be printed.
		The timestamp is in seconds granularity.
		"""
		if message in self.data:
			ans_time = self.data[message]
			if timestamp-ans_time>=10:
				self.data[message] = timestamp
				return True
			else:
				return False
		else:
			self.data[message] = timestamp
			return True



if __name__ == '__main__':
	logger = Logger()
	logger.shouldPrintMessage(1, "foo")
	logger.shouldPrintMessage(2, "bar")
	logger.shouldPrintMessage(3, "foo")
	logger.shouldPrintMessage(8, "bar")
	logger.shouldPrintMessage(10, "foo")
	logger.shouldPrintMessage(11, "foo")
