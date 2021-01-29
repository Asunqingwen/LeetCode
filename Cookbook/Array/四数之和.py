'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        len_ = len(nums)
        res = []
        for first in range(len_ - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, len_ - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                four = len_ - 1
                ans = target - nums[first] - nums[second]
                for third in range(second + 1, len_ - 1):
                    if third > second + 1 and nums[third] == nums[third - 1]:
                        continue
                    while third < four and nums[third] + nums[four] > ans:
                        four -= 1
                    if third == four:
                        break
                    if nums[third] + nums[four] == ans:
                        res.append([nums[first], nums[second], nums[third], nums[four]])
        return res


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    sol = Solution()
    print(sol.fourSum(nums, target))
