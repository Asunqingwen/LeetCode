"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

输入: [2,1,5,6,2,3]
输出: 10
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        left, right = [0] * length, [length] * length
        mono_stack = list()
        for i in range(length):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(length)) if length > 0 else 0
        return ans


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    sol = Solution()
    result = sol.largestRectangleArea(heights)
    print(result)
