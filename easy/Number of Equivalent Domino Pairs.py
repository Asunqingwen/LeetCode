# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 0024 15:48
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Number of Equivalent Domino Pairs.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
 

Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
"""
from typing import List


def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
	if len(dominoes) < 2:
		return 0
	count = {}
	res = 0
	for dominoe in dominoes:
		dominoe.sort()
		key = ''.join([str(i) for i in dominoe])
		count[key] = count.get(key, 0) + 1
	for v in count.values():
		res += v * (v - 1) // 2
	return res


if __name__ == '__main__':
	dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
	result = numEquivDominoPairs(dominoes)
	print(result)
