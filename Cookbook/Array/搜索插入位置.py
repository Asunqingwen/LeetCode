'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_ = len(nums)
        left, right = 0, len_ - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid - 1
            else:
                if mid == len_ - 1 or nums[mid + 1] >= target:
                    return mid + 1
                left = mid + 1
        return left


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 7
    sol = Solution()
    print(sol.searchInsert(nums, target))
