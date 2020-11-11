'''
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

 

示例 1：

输入："ab-cd"
输出："dc-ba"
示例 2：

输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：

输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
 

提示：

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S 中不包含 \ or "
'''


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        len_ = len(S)
        res = [''] * len_
        left, right = 0, len_ - 1
        while left <= right:
            while left < right and not S[left].isalpha():
                res[left] = S[left]
                left += 1
            while left < right and not S[right].isalpha():
                res[right] = S[right]
                right -= 1

            res[left], res[right] = S[right], S[left]
            left += 1
            right -= 1
        return ''.join(res)


if __name__ == '__main__':
    S = ""
    sol = Solution()
    print(sol.reverseOnlyLetters(S))
