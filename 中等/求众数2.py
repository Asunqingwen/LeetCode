"""
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2 = 0, 0
        num1, num2 = nums[0], nums[0]
        for num in nums:
            if num1 == num:
                count1 += 1
                continue
            if num2 == num:
                count2 += 1
                continue
            if count1 == 0:
                num1 = num
                count1 += 1
                continue
            if count2 == 0:
                num2 = num
                count2 += 1
                continue
            count1 -= 1
            count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
        res = []
        if count1 > len(nums) // 3:
            res.append(num1)
        if count2 > len(nums) // 3:
            res.append(num2)
        return res


if __name__ == '__main__':
    nums = [8, 8, 7, 7, 7]
    sol = Solution()
    result = sol.majorityElement(nums)
    print(result)
