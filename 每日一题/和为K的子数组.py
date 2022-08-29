"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数k的范围是 [-1e7, 1e7]。
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, pre = 0, 0
        mp = dict()
        mp[0] = 1
        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in mp:
                count += mp[pre - k]
            mp[pre] = mp.get(pre, 0) + 1
        return count


if __name__ == '__main__':
    nums = [-1, -1, 1]
    k = 0
    sol = Solution()
    result = sol.subarraySum(nums, k)
    print(result)
