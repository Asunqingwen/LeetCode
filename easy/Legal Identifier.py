# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 0012 17:47
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Legal Identifier.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Please judge if string str is a valid identifier.
Legal identifiers consist of letters (A-Z, a-z), numbers (0-9) and underscores, and the first character cannot be a number.
"""
import string


def isLegalIdentifier(str):
	if not str:
		return False
	alphas = string.ascii_letters+'_'
	nums = string.digits
	if str[0] not in alphas:
		return False
	allChar = alphas + nums
	for s in str:
		if s not in allChar:
			return False
	return True

if __name__ == '__main__':
	n = "123_abc"
	result = isLegalIdentifier(n)
	print(result)
