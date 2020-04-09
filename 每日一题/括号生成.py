"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur_str = ""

        def dfs(cur_str, left, right):
            if left == n and right == n:
                res.append(cur_str)
                return
            if left < right:
                return
            if left < n:
                dfs(cur_str + "(", left + 1, right)
            if right < n:
                dfs(cur_str + ")", left, right + 1)

        dfs(cur_str, 0, 0)
        return res


if __name__ == '__main__':
    n = 3
    sol = Solution()
    result = sol.generateParenthesis(n)
    print(result)
