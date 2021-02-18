'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(s=[], lc=0, rc=0):
            if len(s) == 2 * n:
                res.append(''.join(s))
                return
            if lc < n:
                s.append('(')
                helper(s, lc + 1, rc)
                s.pop()
            if rc < lc:
                s.append(')')
                helper(s, lc, rc + 1)
                s.pop()

        res = []
        helper()
        return res


if __name__ == '__main__':
    n = 3
    sol = Solution()
    print(sol.generateParenthesis(n))
