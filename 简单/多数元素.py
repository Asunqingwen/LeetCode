"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        tmp = 0
        for num in nums:
            if count == 0:
                tmp = num
            count += (1 if tmp == num else -1)
        return tmp


if __name__ == '__main__':
    nums = [3, 3, 4]
    sol = Solution()
    result = sol.majorityElement(nums)
    print(result)
