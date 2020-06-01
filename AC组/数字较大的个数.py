"""
给定一个整数数组，去除数组中的负数元素后，按如下规则返回一个结果数组：如果数组元素相邻两项之间后一项大于前一项则打印true，否则打印false

示例1：

数组：【1，3，5，2，7】
输出：  [True, True, False, True]

示例2：

数组： [-9, 3, -2, 0, 7] -> [3,0,7]
输出： [False, True]
"""
from typing import List


class Solution:
    def countOfBoolean(self, nums: List[int]) -> List:
        nums = [num for num in nums if num >= 0]
        return [nums[i] < nums[i + 1] for i in range(len(nums)) if i < len(nums) - 1]


if __name__ == '__main__':
    nums = [-9, 3, -2, 0, 7]
    sol = Solution()
    result = sol.countOfBoolean(nums)
    print(result)
