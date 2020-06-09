"""
1、给定一个整数数组 nums ，不使用暴力循环法，在该数组中找到满足一种计算方式blah 的值并返回他们的数组下标。
blah：a = 2b

给定数组 nums = 【-4,-2,0,2,3,6,8,11,16】
"""
from typing import List


class Solution:
    def addSum(self, nums: List) -> List:
        sum = dict()
        ans = []
        for i in range(len(nums)):
            index = nums[i] / 2
            if index in sum:
                ans.append((i, sum[index]))
            else:
                sum[nums[i]] = i
        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 3, 5, 9, 15, 31, 0]
    sol = Solution()
    result = sol.addSum(nums)
    print(result)
