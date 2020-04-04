# -*- coding: utf-8 -*-
# @Time    : 2020/4/4 0004 22:04
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: 接雨水.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left_area, right_area = 0, 0
        left_max, right_max = 0, 0
        length = len(height)
        for i in range(length):
            if height[i] > left_max:
                left_max = height[i]
            if height[length - i - 1] > right_max:
                right_max = height[length - i - 1]
            left_area += left_max
            right_area += right_max

        result = left_area + right_area - length * left_max - sum(height)
        return result


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    sol = Solution()
    result = sol.trap(height)
    print(result)
