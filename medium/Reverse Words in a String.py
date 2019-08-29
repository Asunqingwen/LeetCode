# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 0028 15:50
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Reverse Words in a String.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.

企业：今日头条 百度 腾讯 360 eBay 微软 Bloomberg 苹果 字节跳动
标签：字符串
"""


def reverseWords(s: str) -> str:
	return ' '.join([ss for ss in s.split(' ') if ss][::-1])


if __name__ == '__main__':
	input = ""
	result = reverseWords(input)
	print(result)
