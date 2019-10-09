# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 0009 15:10
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Rabbits in Forest.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
Note:

answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].
"""
from typing import List


def numRabbits(answers: List[int]) -> int:
	count = {}
	for answer in answers:
		count[answer] = count.get(answer, 0) + 1

	res = 0
	for k, v in count.items():
		if k == 0:
			res += v
		else:
			if v >= k + 1:
				res += v // (k + 1) * (k + 1)
			if v % (k + 1) != 0:
				res += k + 1
	return res


if __name__ == '__main__':
	answers = [0, 0, 7, 6, 6, 0, 1, 3, 5, 2, 5]
	result = numRabbits(answers)
	print(result)
