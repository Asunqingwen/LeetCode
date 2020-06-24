"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def update(cur):
            nonlocal ans
            # 说明当前的和比之前的和更接近于target
            if abs(cur - target) < abs(ans - target):
                ans = cur

        nums.sort()
        length = len(nums)
        ans = 10 ** 7
        for first in range(length):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second, third = first + 1, length - 1
            while second < third:
                sum = nums[first] + nums[second] + nums[third]
                if sum == target:
                    return target
                # 更新当前最接近target的和
                update(sum)
                # 三数之和大于target，右指针左移，减小和
                if sum > target:
                    # 跳过和上一个数重复的数
                    third0 = third - 1
                    while third0 > second and nums[third0] == nums[third0 + 1]:
                        third0 -= 1
                    third = third0
                # 三数之和小于target，左指针右移，增加和
                else:
                    # 跳过和上一个数重复的数
                    second0 = second + 1
                    while second0 < third and nums[second0] == nums[second0 - 1]:
                        second0 += 1
                    second = second0
        return ans


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    sol = Solution()
    result = sol.threeSumClosest(nums, target)
    print(result)
