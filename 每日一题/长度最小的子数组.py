"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""
import math
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        left, right = 0, 0
        length = len(nums)
        res = length + 1
        ans = 0
        while right < length:
            ans += nums[right]
            while ans >= s:
                res = min(res, right - left + 1)
                ans -= nums[left]
                left += 1
            right += 1
        return 0 if res == length + 1 else res


if __name__ == '__main__':
    s = 15
    nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
    sol = Solution()
    result = sol.minSubArrayLen(s, nums)
    print(result)
