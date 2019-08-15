# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 0012 17:35
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Implement strStr().py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1

Input:source = "abcdabcdefg" ，target = "bcd"
Output: 1
Explanation: If the source contains the target content, return the location where the target first appeared in the source.

What should we return when target is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when target is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


def strStr(source, target):
	if not target:
		return 0
	if not source:
		return -1
	s_len = len(source)
	t_len = len(target)
	for i in range(s_len-t_len+1):
		j = 0
		while(j < t_len):
			if source[i + j] != target[j]:
				break
			j += 1
		if j == t_len:
			return i
	return -1


if __name__ == '__main__':
	source = "abcdabcdefg"
	target = "bcd"
	result = strStr(source,target)
	print(result)
