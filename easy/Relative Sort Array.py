# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 0018 10:40
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Relative Sort Array.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.
"""
from typing import List


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
	res = []
	ans = []
	count = {}
	for a2 in arr2:
		count[a2] = 0
	for a1 in arr1:
		if a1 in count:
			count[a1] += 1
		else:
			ans.append(a1)
	for a2 in arr2:
		for i in range(count[a2]):
			res.append(a2)
	ans.sort()
	res.extend(ans)
	return res


if __name__ == '__main__':
	arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
	arr2 = [2,42,38,0,43,21]
	result = relativeSortArray(arr1, arr2)
	print(result)
