# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 0021 13:54
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Basic Calculator III.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
 

Note: Do not use the eval built-in library function.
"""


def calculate(s: str) -> int:
	def helper(s):
		sign = '+'
		num, res = 0, 0
		ans = []
		i = 0
		while i < len(s):
			if s[i].isnumeric():
				num = num * 10 + int(s[i])
			elif s[i] == '(':
				count = 1
				i += 1
				j = i
				while i < len(s):
					if s[i] == '(':
						count += 1
					elif s[i] == ')':
						count -= 1
					if count == 0:
						break
					i += 1
				num = helper(s[j:i])
			if s[i] in ['+', '-', '*', '/'] or i == len(s) - 1:
				if sign == '+':
					ans.append(num)
				elif sign == '-':
					ans.append(-num)
				elif sign == '*':
					ans.append(ans.pop() * num)
				elif sign == '/':
					tmp = ans.pop()
					ans.append(int(tmp / num))
				sign = s[i]
				num = 0
			i += 1
		while ans:
			res += ans.pop()
		return res

	return helper(s)


def calculate1(s: str) -> int:
	def helper(pre, curr, next, sign):
		if sign == '+':
			pre += curr
			curr = next
		elif sign == '-':
			pre += curr
			curr = -next
		elif sign == '*':
			curr *= next
		elif sign == '/':
			curr = int(curr / next)
		return pre, curr, 0

	def cal(s):
		pre, curr, next = 0, 0, 0
		sign = '+'
		i = 0
		while i < len(s):
			if s[i].isnumeric():
				next = next * 10 + int(s[i])
			elif s[i] == '(':
				count = 1
				i += 1
				j = i
				while i < len(s):
					if s[i] == '(':
						count += 1
					elif s[i] == ')':
						count -= 1
					if count == 0:
						break
					i += 1
				next = cal(s[j:i])
			if s[i] in ['+', '-', '*', '/'] or i == len(s) - 1:
				pre, curr, next = helper(pre, curr, next, sign)
				sign = s[i]
			i += 1
		return pre + curr

	return cal(s)


if __name__ == '__main__':
	s = "((  13 /(  (   6+ 19  )/ 14  )  ) +( (   17 * (   ((   (  ( (   ( 18+19  )   +  (5  +   7   ) )*(  17+ (   14   /16 ) )) +7)  / ( ( (   (   14  +  14   )+  ( 7 /  10   ))  * 15  )  /(  (   (  20   +  4)  *13   ) + 1   ))   )*   ( 10+   15 )  )- ( (  (((   (   4  +   17  )   +   (4   * 6) )   +   (   12   +   15   )  )   +   5)+  (  ((( 14  +   19  ) +( 10 +  1  )) -(  ( 11   +17)+ ( 10  +   1)   )   ) +(( (  13  +   20  ) - (18 +17  )   )-  ( (   7  /15  )  -  (  7   - 19   ))   ) ))   -  (  (   17   +  (   ( ( 15 + 2 )  * (  2   -  6 )   )  + (   (  6   +  14   ) + ( 19   * 2  )   ))   )/ (   (  (  ( 18   -3   )+(  6 *13   ) )   +15 )+((   (  17 -19)   +  ( 2  +10)  )+(  ( 8 +18 )  +  (9+  8)   ) ) ))  ) )  )   -( (( (( 14 /   5 )+ ( (   (  ( 13  + 11  ) - ( 3* 20 )   )   -  (   (  15 *  10)  +  (14+ 19  )   ) )-(   ((   8   +  20  )   -  (   5*16   ) )   *(  ( 13 - 1)   /  (   8/ 6) ) ) ) ) +  8) +  5   )  / ( (  (   (( (   ( 18  + 17   )+(  4 + 8 ))  +(   ( 19  *16 )  + (11   *   14  )   )  )   +   (( (   6   + 19  )  *  (7- 17  ) ) +  ( (  12+ 16)   *  (15+ 7  )) )   )* ((   (   (  3 +13)  +   ( 19   +19  )  )   -   (  (4*   7  )  +  11) ) * 18) )   - ((   14  +20 )   *   ((   (   (   12   *   8   )   * (   7   + 12 ) )  /   13 ) * (   (   (  3   -  6  )  +(8/   10   )  )  +(  2+ (15 -   20  )   )  )  )  )) +((   (  (   1*   ( ( 12  -  1   )  +( 7*18  ) )  )*  6   )   + (  (   ((4+   20 ) -   2 )   *(   (   8  -  13  )   *(14 -19 )))*  (  (( 19  +   1   )   +  ( 4  -  13 )   )+  (  (  19  +  4)  *(  19  +   19 )   ) )  )   ) + (  (   (  7 +  (  9   +  (14 +   4)) )  - 9)   *  ((   5  /  (   (  19  +3   )  + (  9   *   15 ) )   ) + ( (( 20   +   12  )+ (17 +   12 ) )  *(  (17  +6   ) +   16 ))))) )  ) ))"
	result = calculate1(s)
	print(result)
