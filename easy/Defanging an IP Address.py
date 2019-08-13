# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 0013 15:06
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Defanging an IP Address.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Constraints:

The given address is a valid IPv4 address.
"""


def defangIPaddr(address: str) -> str:
	return address.replace('.', '[.]')


if __name__ == '__main__':
	str = "1.1.1.1"

	result = defangIPaddr(str)
	print(result)
