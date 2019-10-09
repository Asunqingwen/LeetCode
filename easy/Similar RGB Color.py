# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 0009 10:25
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Similar RGB Color.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
In the following, every capital letter represents some hexadecimal digit from 0 to f.

The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.  For example, "#15c" is shorthand for the color "#1155cc".

Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.

Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ"

Example 1:
Input: color = "#09f166"
Output: "#11ee66"
Explanation:
The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
This is the highest among any shorthand color.
Note:

color is a string of length 7.
color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
Any answer which has the same (highest) similarity as the best answer will be accepted.
All inputs and outputs should use lowercase letters, and the output is 7 characters.
"""


def similarRGB(color: str) -> str:
	r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16)
	res = '#'

	def helper(c):
		dd = [0] * 2
		while True:
			for d in dd:
				ans = c + d
				if ans % 16 == ans // 16:
					ans = format(ans, 'x')
					if ans == '0':
						return ans + '0'
					else:
						return ans
			dd[0] += 1
			dd[1] -= 1

	res += helper(r) + helper(g) + helper(b)
	return res


if __name__ == '__main__':
	color = "#1c9e03"
	result = similarRGB(color)
	print(result)
