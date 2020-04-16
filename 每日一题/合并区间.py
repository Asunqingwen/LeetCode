"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        i = 0
        j = i + 1
        while i < len(intervals):
            value = intervals[i]
            j = i + 1
            while j < len(intervals):
                temp = intervals[j]
                if temp[0] > value[1]:
                    break
                if temp[0] < value[0]:
                    value[0] = temp[0]
                if value[1] < temp[1]:
                    value[1] = temp[1]
                j += 1
            result.append(value)
            i = j
        return result


if __name__ == '__main__':
    intervals = [[1,4],[0,0]]
    sol = Solution()
    result = sol.merge(intervals)
    print(result)
