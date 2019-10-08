# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 0008 11:37
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Minimum Index Sum of Two Lists.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""
from typing import List


def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
	dict1 = {}
	for index, l in enumerate(list1):
		dict1[l] = index
	min_index = 2000
	res = []
	for index, l in enumerate(list2):
		if l in dict1:
			curr_index = index + dict1[l]
			if curr_index < min_index:
				res.clear()
				res.append(l)
				min_index = index + dict1[l]
			elif curr_index == min_index:
				res.append(l)
	return res


if __name__ == '__main__':
	list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
	list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]
	result = findRestaurant(list1, list2)
	print(result)
