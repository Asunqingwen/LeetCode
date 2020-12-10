'''
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 

限制：

0 <= 数组长度 <= 50000

 

注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        def helper(left, right, target):
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        left, right = 0, len(nums) - 1
        right = helper(left, right, target)
        if right > 0 and nums[right - 1] != target:
            return 0
        left = helper(0, right, target - 1)
        return right - left



if __name__ == '__main__':
    nums = []
    target = 0
    sol = Solution()
    print(sol.search(nums, target))
