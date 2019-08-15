# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 15:05
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Remove All Adjacent Duplicates In String.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 

Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.
"""


def removeDuplicates(S: str) -> str:
	str = ""
	for s in S:
		if str and s == str[-1]:
			str = str[:-1]
		else:
			str += s
	return str


if __name__ == '__main__':
	S = "abbaca"
	result = removeDuplicates(S)
	print(result)
