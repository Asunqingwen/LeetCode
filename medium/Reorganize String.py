# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 0008 16:20
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Reorganize String.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""


def reorganizeString(S: str) -> str:
	count = {}
	for s in S:
		count[s] = count.get(s, 0) + 1
	ans = sorted(count.items(), key=lambda x: x[1], reverse=True)
	if ans[0][1] > (len(S) + 1) // 2:
		return ''
	res = ['a'] * len(S)
	index = 0
	for k, v in ans:
		while index < len(S) and v > 0:
			res[index] = k
			index += 2
			if index >= len(S):
				index = 1
			v -= 1
	return ''.join(res)


if __name__ == '__main__':
	S = "aba"
	result = reorganizeString(S)
	print(result)
