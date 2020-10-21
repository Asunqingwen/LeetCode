"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
"""
import math
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2 = math.inf, math.inf
        max1, max2, max3 = -math.inf, -math.inf, -math.inf
        for num in nums:
            if num <= min1:
                min2, min1 = min1, num
            elif num <= min2:
                min2 = num

            if num >= max1:
                max1, max2, max3 = num, max1, max2
            elif num >= max2:
                max2, max3 = num, max2
            elif num >= max3:
                max3 = num
        return max(min1 * min2 * max1, max1 * max2 * max3)


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.maximumProduct(nums))
