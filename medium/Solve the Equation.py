# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 0011 14:40
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Solve the Equation.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""


def solveEquation(equation: str) -> str:
		formula = equation.split("=")

		def get_count(formula):
			num_list = []
			pre_symbol = "+"
			x_count = 0
			num = 0
			for c in formula:
				# 不是运算符
				if c != "+" and c != "-":
					if c == "x":
						add_x = 1 if len(num_list) == 0 else int("".join(num_list))
						if pre_symbol == "+":
							x_count += add_x
						else:
							x_count -= add_x
						num_list = []  # 清空列表
					else:
						# 是数字
						num_list.append(c)
				# 是运算符
				else:
					if len(num_list) != 0:
						num = eval(str(num) + pre_symbol + "".join(num_list))
					pre_symbol = c
					num_list = []
			# 最后遗漏的数字
			if len(num_list) != 0:
				num = eval(str(num) + pre_symbol + "".join(num_list))
			return [x_count, num]

		left = get_count(formula[0])
		right = get_count(formula[1])

		x_count = left[0] - right[0]
		num = left[1] - right[1]

		# 计算结果
		if x_count == 0 and num == 0:
			return "Infinite solutions"
		if x_count == 0 and num != 0:
			return "No solution"
		return "x=" + str(-num // x_count)


if __name__ == '__main__':
	equation = "x=2"
	result = solveEquation(equation)
	print(result)
