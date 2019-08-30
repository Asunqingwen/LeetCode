# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 0029 9:33
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Groups of Special-Equivalent Strings.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
You are given an array A of strings.

Two strings S and T are special-equivalent if after any number of moves, S == T.

A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].

Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any string not in S is not special-equivalent with any string in S.

Return the number of groups of special-equivalent strings from A.

 

Example 1:

Input: ["a","b","c","a","c","c"]
Output: 3
Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]

Note:

1 <= A.length <= 1000
1 <= A[i].length <= 20
All A[i] have the same length.
All A[i] consist of only lowercase letters.

企业：Facebook
标签：字符串
"""
from typing import List


def numSpecialEquivGroups(A: List[str]) -> int:
	count = 0
	s_dict = {}
	for a in A:
		s = ''.join(sorted(a[::2]) + sorted(a[1::2]))
		if s not in s_dict:
			count += 1
			s_dict[s] = 0

	return count


if __name__ == '__main__':
	input = ["abcd","cdab","adcb","cbad"]
	result = numSpecialEquivGroups(input)
	print(result)
