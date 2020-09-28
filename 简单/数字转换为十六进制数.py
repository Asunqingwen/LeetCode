"""
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:

十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
示例 1：

输入:
26

输出:
"1a"
示例 2：

输入:
-1

输出:
"ffffffff"
"""


class Solution:
    def toHex(self, num: int) -> str:
        hex_str = '0123456789abcdef'
        num &= 0xffffffff  # 高位都是 0，移位也是补 0
        digits = []
        # 手动执行一次循环
        lowbit4 = num & 0xf
        num >>= 4
        digits.append(hex_str[lowbit4])
        # 开始执行 while 循环
        while num:
            lowbit4 = num & 0xf
            num >>= 4
            digits.append(hex_str[lowbit4])

        # 最后反转一下再连接
        return ''.join(reversed(digits))


if __name__ == '__main__':
    num = 26
    sol = Solution()
    print(sol.toHex(num))
