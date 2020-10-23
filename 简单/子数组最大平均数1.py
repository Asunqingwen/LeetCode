"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
 

注意:

1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        len_ = len(nums)
        sum_ = sum(nums[0:k])
        res = sum_
        for i in range(k, len_):
            sum_ += nums[i] - nums[i - k]
            res = max(res, sum_)
        return res / k


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 1
    sol = Solution()
    print(sol.findMaxAverage(nums, k))
