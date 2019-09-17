# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 0017 10:08
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Reverse Vowels of a String.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""


def reverseVowels(s: str) -> str:
	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	ans = []
	res = []
	for ss in s:
		if ss in vowels:
			ans.append(ss)
			res.append('-1')
		else:
			res.append(ss)
	ans.reverse()
	j = 0
	for i in range(len(res)):
		if res[i] == '-1':
			res[i] = ans[j]
			j += 1
	return ''.join(res)


if __name__ == '__main__':
	input = "aA"
	result = reverseVowels(input)
	print(result)
