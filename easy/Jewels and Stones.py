# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 0013 14:58
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Jewels and Stones.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""


def numJewelsInStones(J: str, S: str) -> int:
	j_dict = {}
	count = 0
	for j in J:
		j_dict[j] = 0
	for s in S:
		if s in j_dict:
			count += 1
	return count


if __name__ == '__main__':
	J = "z"
	S = "ZZ"

	result = numJewelsInStones(J, S)
	print(result)
