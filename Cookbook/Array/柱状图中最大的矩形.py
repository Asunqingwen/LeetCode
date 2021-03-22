'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 



以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

 



图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

 

示例:

输入: [2,1,5,6,2,3]
输出: 10
'''
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        len_ = len(heights)
        if len_ == 0:
            return 0
        left = [0] * len_
        right = [len_] * len_
        indexs = []
        for i in range(len_):
            while indexs and heights[indexs[-1]] >= heights[i]:
                right[indexs[-1]] = i
                indexs.pop()
            left[i] = indexs[-1] if indexs else -1
            indexs.append(i)

        res = max([(right[i] - left[i] - 1) * heights[i] for i in range(len_)])
        print(left,right)
        return res


if __name__ == '__main__':
    heights = [4, 6, 5, 6, 4]
    sol = Solution()
    print(sol.largestRectangleArea(heights))
