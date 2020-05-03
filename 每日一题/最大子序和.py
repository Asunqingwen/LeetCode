"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        sum_value = 0
        for i_value in nums:
            if sum_value > 0:
                sum_value = i_value + sum_value
            else:
                sum_value = i_value

            max_value = max(max_value, sum_value)
        return max_value


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    result = sol.maxSubArray(nums)
    print(result)
