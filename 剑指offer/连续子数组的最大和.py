from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_sum = 0
        max_sum = nums[0]
        for num in nums:
            pre_sum = max(pre_sum + num, num)
            if max_sum < pre_sum:
                max_sum = pre_sum
        return max_sum
