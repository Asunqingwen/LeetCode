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
"""


def strStr(source, target):
	if not source or not target:
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
