"""
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
"""
from typing import List
import collections


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        return sum(
            sum(t * t - t for t in collections.Counter((x2 - x1) ** 2 + (y2 - y1) ** 2 for x2, y2 in points).values())
            for x1, y1 in points)


if __name__ == '__main__':
    points = [[0, 0], [1, 0], [2, 0]]
    sol = Solution()
    print(sol.numberOfBoomerangs(points))
