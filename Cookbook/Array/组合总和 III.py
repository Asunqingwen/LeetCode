'''
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
'''
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(index, sum_):
            if k < len(ans) or sum_ <= 0:
                if k == len(ans) and sum_ == 0:
                    res.append(ans[:])
                return
            for i in range(index, 9):
                if i + 1 > sum_:
                    break
                ans.append(i + 1)
                helper(i + 1, sum_ - i - 1)
                ans.pop()
            return

        res = []
        ans = []
        helper(0, n)
        return res


if __name__ == '__main__':
    k = 3
    n = 9
    sol = Solution()
    print(sol.combinationSum3(k, n))
