"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

 

示例 1：

输入："hello"
输出："holle"
示例 2：

输入："leetcode"
输出："leotcede"
 

提示：

元音字母不包含字母 "y" 。
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = list(s)
        l, r = 0, len(ans) - 1
        volume = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while l < r:
            if ans[l] not in volume:
                ans[l] = ans[l]
                l += 1
            elif ans[r] not in volume:
                ans[r] = ans[r]
                r -= 1
            else:
                ans[l], ans[r] = ans[r], ans[l]
                l += 1
                r -= 1
        return ''.join(ans)


if __name__ == '__main__':
    s = "ai"
    sol = Solution()
    print(sol.reverseVowels(s))
