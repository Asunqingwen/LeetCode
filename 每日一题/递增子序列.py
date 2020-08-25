"""
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
"""
from collections import defaultdict
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums: List[int], tmp: List[int]) -> None:
            if len(tmp) > 1:
                res.append(tmp)
            curPres = defaultdict(int)
            for inx, i in enumerate(nums):
                if curPres[i]:
                    continue
                if not tmp or i >= tmp[-1]:
                    curPres[i] = 1
                    dfs(nums[inx+1:], tmp+[i])

        dfs(nums, [])
        return res


if __name__ == '__main__':
    nums = [4, 6, 7, 7]
    sol = Solution()
    result = sol.findSubsequences(nums)
    ans = [1, 2, 3]
    print(ans.insert(4, 0))
