# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 0022 11:21
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Smallest String With Swaps.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.



Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination:
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
"""
from typing import List

import numpy as np


def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
	# 并查集的find函数,找老大
	def ffind(a):
		if a == fa[a]:
			return a
		f = ffind(fa[a])
		fa[a] = f
		return f

	# 并查集的union函数
	def union(a, b):
		a = ffind(a)
		b = ffind(b)
		fa[a] = b

	# 并查集维护集合
	n = len(s)
	fa = np.arange(n)
	for a, b in pairs:
		union(a, b)
	for i in range(n):
		ffind(i)
	# 得到所有的place集合
	unique_fa = np.unique(fa)
	# 得到所有place集合中对应的字符串并排序
	fa_str = {x: '' for x in unique_fa}
	# 把小弟都连接起来
	for i in range(n):
		fa_str[fa[i]] += s[i]
	for x in unique_fa:
		fa_str[x] = sorted(fa_str[x])
	# 计算每个place当前用到的index
	fa_cnt = {x: 0 for x in unique_fa}
	# 将排序完的字符串反映射回原串得到最后结果
	ans = ''
	for i in range(n):
		x = fa[i]
		ans += fa_str[x][fa_cnt[x]]
		fa_cnt[x] += 1
	return ans


if __name__ == '__main__':
	s = "dcab"
	pairs = [[0, 3], [1, 2]]
	result = smallestStringWithSwaps(s, pairs)
	print(result)
