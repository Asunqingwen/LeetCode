# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 0028 11:28
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Valid Palindrome.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

企业：Facebook 今日头条 百度 阿里巴巴 微软 优步 美团 Adobe 字节跳动
标签：双子针 字符串
"""
import re


def isPalindrome(s: str) -> bool:
	s = s.lower()
	head = 0
	tail = len(s) - 1
	while head <= tail:
		if s[head].isalnum() and s[tail].isalnum():
			if s[head] == s[tail]:
				head += 1
				tail -= 1
				continue
			else:
				return False
		if not s[head].isalnum():
			head += 1
		if not s[tail].isalnum():
			tail -= 1
	return True


def isPalindrome1(s: str) -> bool:
	if not s:
		return True
	s = s.lower()
	s = re.sub(r'\W+', '', s)
	return s == s[::-1]

def isPalindrome2(s: str) -> bool:
	s_dict = {}
	for i in range(10):
		s_dict[str(i)] = i+1
	for i in range(26):
		s_dict[chr(i+ord('a'))] = i+10
		s_dict[chr(i+ord('A'))] = i+10

	head = 0
	tail = len(s) - 1
	while head <= tail:
		head_num = s_dict.get(s[head],0)
		tail_num = s_dict.get(s[tail],0)
		if head_num and tail_num:
			if head_num == tail_num:
				head += 1
				tail -= 1
				continue
			else:
				return False
		if not head_num:
			head += 1
		if not tail_num:
			tail -= 1
	return True



if __name__ == '__main__':
	input = "0P"
	result = isPalindrome2(input)
	print(result)
