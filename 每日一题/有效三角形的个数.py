"""
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。
"""
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        ans = 0
        #固定最长边
        for first in range(length - 1, 1, -1):
            second, third = 0, first - 1
            while second < third:
                if nums[second] + nums[third] > nums[first]:
                    ans += third - second
                    third -= 1
                else:
                    second += 1
        return ans


if __name__ == '__main__':
    nums = [2, 2, 3, 4]
    sol = Solution()
    result = sol.triangleNumber(nums)
    print(result)
