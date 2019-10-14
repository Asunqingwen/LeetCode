# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 0014 11:47
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Water and Jug Problem.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
"""
from math import gcd


def canMeasureWater(x: int, y: int, z: int) -> bool:
	if x == 0 or y == 0:
		return z == 0
	if z > x + y:
		return False
	return z % gcd(x, y) == 0


if __name__ == '__main__':
	x = 2
	y = 6
	z = 5
	result = canMeasureWater(x, y, z)
	print(result)
