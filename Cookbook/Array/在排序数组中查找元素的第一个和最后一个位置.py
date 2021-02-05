'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109
'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(left, right, target):
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        ans1 = binarySearch(0, len(nums) - 1, target)
        ans2 = binarySearch(0, len(nums) - 1, target + 1)
        if ans1 == len(nums) or nums[ans1] != target:
            return [-1, -1]
        return [ans1, ans2 - 1]


if __name__ == '__main__':
    nums = [5,5,6, 7, 9, 9, 11]
    target = 9
    sol = Solution()
    print(sol.searchRange(nums, target))
