# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 0003 15:19
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Find the Town Judge.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2

Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N m
"""
from typing import List


def findJudge(N: int, trust: List[List[int]]) -> int:
	# 统计初入度
	ans = {}
	for row in trust:
		ans[row[0]] = ans.get(row[0], 0) - 1
		ans[row[1]] = ans.get(row[1], 0) + 1
	for i in range(1, N + 1):
		res = ans.get(i, 0)
		if res == N - 1:
			return i
	return -1


if __name__ == '__main__':
	N = 3
	trust = [[1, 3], [2, 3]]
	result = findJudge(N, trust)
	print(result)
