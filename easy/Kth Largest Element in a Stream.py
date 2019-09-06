# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 0004 9:34
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Kth Largest Element in a Stream.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""
import heapq
from typing import List


class KthLargest:

	def __init__(self, k: int, nums: List[int]):
		self.nums = nums
		heapq.heapify(self.nums)
		self.k = k
		while len(self.nums) > k:
			heapq.heappop(self.nums)

	def add(self, val: int) -> int:
		if len(self.nums) < self.k:
			heapq.heappush(self.nums, val)
		elif val > self.nums[0]:
			heapq.heapreplace(self.nums, val)
		return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
if __name__ == '__main__':
	k = 1
	nums = []
	obj = KthLargest(k, nums)
	result = obj.add(-3)
	print(result)
