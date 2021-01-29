'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''
import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        len_ = len(nums)
        res, diff = 0, math.inf
        for first in range(len_):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second, third = first + 1, len_ - 1
            while second < third:
                sum_ = nums[first] + nums[second] + nums[third]
                if abs(sum_ - target) < diff:
                    res, diff = sum_, abs(sum_ - target)
                if sum_ == target:
                    return res
                elif sum_ > target:
                    third -= 1
                else:
                    second += 1
        return res


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    sol = Solution()
    print(sol.threeSumClosest(nums, target))
