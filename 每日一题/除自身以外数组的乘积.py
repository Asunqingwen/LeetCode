"""
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

 

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
 

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        multipy = [0] * length

        # multipy表示索引为i的值左侧乘积为多少，索引为0的左侧没有值，故值设为1
        multipy[0] = 1
        for i in range(1, length):
            multipy[i] = multipy[i - 1] * nums[i - 1]
        # R为右侧所有元素的乘积，刚开始右边没有元素，所以R=1
        R = 1
        for i in range(length - 1, -1, -1):
            # 当前索引的总乘积为左右元素乘积相乘
            multipy[i] *= R
            # 更新R的值
            R *= nums[i]
        return multipy


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    sol = Solution()
    result = sol.productExceptSelf(nums)
    print(result)
