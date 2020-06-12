"""
给你一个无序数组，找出数组中的一个数，使得在数组中，这个数之前的所有数字之和等于这个数之后所有数字之和。算法时间复杂度必须低于O(n)^2
"""
from typing import List


class Solution:
    def leftEqualRight(self, nums: List[int]) -> bool:
        if not nums:
            return False
        sum_nums = sum(nums)
        length = len(nums)
        if length == 1 and sum_nums == 0:
            return True
        left_num, right_num = 0, sum_nums - nums[0]
        for i in range(1, length):
            if left_num == right_num:
                return True
            left_num += nums[i - 1]
            right_num -= nums[i]
        return False


if __name__ == '__main__':
    nums = [0, 2, -2, 4, -4]
    sol = Solution()
    result = sol.leftEqualRight(nums)
    print(result)
