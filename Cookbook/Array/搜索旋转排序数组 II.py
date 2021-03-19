'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            value = nums[mid]
            if target == value:
                return True
            if nums[left] < value:  # mid值在左边部分
                if nums[left] <= target < value:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[right] > value:  # mid值在右边部分
                if value < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:  # 去重
                if nums[left] == value:
                    left += 1
                if nums[right] == value:
                    right -= 1

        return False


if __name__ == '__main__':
    nums = [1, 0, 1, 1, 1]
    target = 0
    sol = Solution()
    print(sol.search(nums, target))
