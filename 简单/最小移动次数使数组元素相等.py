"""
给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动将会使 n - 1 个元素增加 1。

 

示例:

输入:
[1,2,3]

输出:
3

解释:
只需要3次移动（注意每次移动会增加两个元素的值）：

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_ = min(nums)
        res = 0
        for num in nums:
            res += num - min_
        return res


if __name__ == '__main__':
    nums = [5, 6, 8, 8, 5]
    sol = Solution()
    print(sol.minMoves(nums))
