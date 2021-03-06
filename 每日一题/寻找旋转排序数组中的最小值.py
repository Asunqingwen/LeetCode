"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    result = sol.findMin(nums)
    print(result)
