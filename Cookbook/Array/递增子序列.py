'''
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是 2 。

 

示例：

输入：[4, 6, 7, 7]
输出：[[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
 

提示：

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
'''
import math
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(last, cur, end, ans=None):
            if cur == end:
                if len(ans) > 1:
                    res.append(ans[:])
                return
            if nums[cur] >= last:  # 当前值不小于上一个值
                ans.append(nums[cur])
                helper(nums[cur], cur + 1, end, ans)
                ans.pop()
            if nums[cur] != last:
                helper(last, cur + 1, end, ans)
            return

        helper(-math.inf, 0, len(nums), [])
        return list(res)


if __name__ == '__main__':
    nums = [4, 6, 7, 7]
    sol = Solution()
    print(sol.findSubsequences(nums))
