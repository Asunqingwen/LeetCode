# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 0026 10:43
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Nth Digit.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""


# 2**31 = 2,147,483,648
def findNthDigit(n: int) -> int:
	if n < 10:
		return n
	max_bit, max_count = 1, 0
	while max_count < n:
		max_count += 9 * (10 ** (max_bit - 1)) * max_bit
		max_bit += 1
	size = max_bit - 1
	pre_bit = max_count - 9 * (10 ** (size - 1)) * size
	pre_last_num = (10 ** (size - 1)) - 1
	curr_num = (n - pre_bit) // size + pre_last_num
	if (n - pre_bit) % size == 0:
		return curr_num % 10
	else:
		curr_num += 1
	index = n - (curr_num - pre_last_num - 1) * size - pre_bit

	return int(str(curr_num)[index - 1])


def findNthDigit1(n: int) -> int:
	# 所在位数规律：9 * pow(10, i - 1) * i
	i, max_count = 0, 0
	while max_count < n:
		i += 1
		max_count += i * (9 * 10 ** (i - 1))

	# 起始值对应的次数(n)
	start_count = max_count - i * (9 * 10 ** (i - 1))

	power = i - 1  # 幂（用于求所在位数）
	start_val = 10 ** power  # 起始值

	step = n - start_count - 1  # 剩余移动步数
	step_length = i  # 每增一需要的步长
	# offset - 偏移值（从起始值开始）
	# pos - 结果值指向的位数 - 从最高位开始偏移
	offset, pos = divmod(step, step_length)

	curr_val = start_val + offset  # 当前数值 - 起始值 + 偏移值
	# 对应位数的数字，即解
	result = curr_val // 10 ** (power - pos) % 10

	return result


if __name__ == '__main__':
	input = 10000
	result = findNthDigit(input)
	print(result)
