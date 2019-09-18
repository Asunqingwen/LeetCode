# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 0018 11:43
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Design HashMap.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);        
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""


class MyHashMap:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.data = [-1] * 1000001

	def put(self, key: int, value: int) -> None:
		"""
		value will always be non-negative.
		"""
		self.data[key] = value

	def get(self, key: int) -> int:
		"""
		Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
		"""
		return self.data[key]

	def remove(self, key: int) -> None:
		"""
		Removes the mapping of the specified value key if this map contains a mapping for the key
		"""
		self.data[key] = -1


if __name__ == '__main__':
	hashMap = MyHashMap()
	hashMap.put(1, 1)
	hashMap.put(2, 2)
	hashMap.get(1)  # 返回1
	hashMap.get(3)  # 返回 - 1(未找到)
	hashMap.put(2, 1)  # 更新已有的值
	hashMap.get(2)  # 返回1
	hashMap.remove(2)  # 删除键为2的数据
	hashMap.get(2)  # 返回 - 1(未找到)
