"""
找出数组中重复的数字
在一个长度为n的数组里的所有数字都在0~n+1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请不改变原数组，找出数组中任意一个重复的数字并返回。

输入：【2，3，1，0，2，5，3】
输出： 2或3

请以数组【1，4，6，2，4，3，8，6，1】开始解题
"""
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        counts = dict()
        for num in nums:
            if num in counts:
                return num
            else:
                counts[num] = num
        return -1

if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    sol = Solution()
    result = sol.findRepeatNumber(nums)
    print(result)
