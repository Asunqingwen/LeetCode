"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 231
"""


class Solution:
    def translateNum(self, num: int) -> int:
        dp_1, dp0, ans = 0, 0, 1
        num = str(num)
        for i in range(0, len(num)):
            dp_1 = dp0
            dp0 = ans
            ans = 0
            ans += dp0
            if i == 0:
                continue
            str_num = num[i - 1:i + 1]
            if "10" <= str_num <= "25":
                ans += dp_1
        return ans


if __name__ == '__main__':
    num = 12258
    sol = Solution()
    result = sol.translateNum(num)
    print(result)
