'''
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

 

示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
 

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1
'''
from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        mp = defaultdict()
        counter = 0
        mp[counter] = -1
        len_ = len(nums)
        for i in range(len_):
            num = nums[i]
            if num == 1:
                counter += 1
            else:
                counter -= 1
            if counter in mp:
                prevIndex = mp[counter]
                res = max(res, i - prevIndex)
            else:
                mp[counter] = i

        return res


if __name__ == '__main__':
    nums = [0, 0, 1, 0, 0, 0, 1, 1]
    sol = Solution()
    print(sol.findMaxLength(nums))
