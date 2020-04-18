# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 0018 14:09
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: 盛最多水的容器.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

 

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_h, right_h = height[0], height[-1]
        left_w, right_w = 0, len(height) - 1
        h = left_h if left_h < right_h else right_h
        result = h * (right_w - left_w)
        while left_w < right_w:
            if right_h > left_h:
                left_w += 1
                left_h = height[left_w]
            else:
                right_w -= 1
                right_h = height[right_w]
            h = left_h if left_h < right_h else right_h
            temp_result = h * (right_w - left_w)
            result = max(temp_result, result)
        return result


if __name__ == '__main__':
    height = [2,3,4,5,18,17,6]
    sol = Solution()
    result = sol.maxArea(height)
    print(result)
