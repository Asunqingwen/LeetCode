"""
给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。

示例：

输入: nums = [-2,0,1,3], target = 2
输出: 2
解释: 因为一共有两个三元组满足累加和小于 2:
     [-2,0,1]
     [-2,0,3]
进阶：是否能在 O(n2) 的时间复杂度内解决？
"""
from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        ans = 0
        for first in range(length - 2):
            second, third = first + 1, length - 1
            while second < third:
                sum = nums[first] + nums[second] + nums[third]
                if sum < target:
                    ans += third - second
                    second += 1
                else:
                    third -= 1
        return ans


if __name__ == '__main__':
    nums = [-1, 1, -1, -1]
    target = -1
    sol = Solution()
    result = sol.threeSumSmaller(nums, target)
    print(result)
