"""
给定一个升序整数数组，写一个函数搜索 nums 中数字 target。如果 target 存在，返回它的下标，否则返回 -1。注意，这个数组的大小是未知的。你只可以通过 ArrayReader 接口访问这个数组，ArrayReader.get(k) 返回数组中第 k 个元素（下标从 0 开始）。

你可以认为数组中所有的整数都小于 10000。如果你访问数组越界，ArrayReader.get 会返回 2147483647。

 

样例 1：

输入: array = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 存在在 nums 中，下标为 4
样例 2：

输入: array = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不在数组中所以返回 -1
"""


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1

        while left <= right:
            mid = left + (right - left) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                right -= 1
            elif reader.get(mid) < target:
                left += 1
        return -1
