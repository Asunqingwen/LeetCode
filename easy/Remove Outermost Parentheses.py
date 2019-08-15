# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 14:41
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Remove Outermost Parentheses.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
"""


def removeOuterParentheses(S: str) -> str:
	s_list = []
	temp_str = ""
	count = 0
	for s in S:
		if s == "(":
			count += 1
		elif s == ")":
			count -= 1
		temp_str += s
		if count == 0:
			s_list.append(temp_str[1:-1])
			temp_str = ""
	return ''.join(s_list)


if __name__ == '__main__':
	S = "(()())(())(()(()))"
	result = removeOuterParentheses(S)
	print(result)
