# -*- coding: utf-8 -*-
# @Time    : 2019/10/25 0025 15:36
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Minimum Window Subsequence.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input:
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
 

Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
"""


def minWindow(S: str, T: str) -> str:
	if S == T:
		return S
	if len(T) == 1 and T in S:
		return T
	i, j = 0, 0
	res = ''
	max_len = len(S)
	while i < len(S):
		if S[i] == T[j]:
			j += 1
			if j == len(T):
				right = i
				j -= 1
				while j >= 0:
					if S[i] == T[j]:
						j -= 1
					i -= 1
				i += 1
				if len(S[i:right + 1]) < max_len:
					res = S[i:right + 1]
					max_len = len(res)
				j += 1
		i += 1

	return '' if max_len == len(S) else res


if __name__ == '__main__':
	S = "abcdebddebdee"
	T = "bdee"
	result = minWindow(S, T)
	print(result)
