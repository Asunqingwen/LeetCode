"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_sum, min_sum, sum = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            mx, mn = max_sum, min_sum
            max_sum = max(mx * nums[i], mn * nums[i], nums[i])
            min_sum = min(mn * nums[i], mx * nums[i], nums[i])
            sum = max(max_sum, sum)
        return sum


if __name__ == '__main__':
    nums = [-4, -3, -2]
    sol = Solution()
    result = sol.maxProduct(nums)
    print(result)
