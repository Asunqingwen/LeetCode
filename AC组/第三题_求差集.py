"""
两个数组的差集，给定两个数组，编写一个函数来计算它们的差集
"""
from typing import List


class Solution:
    def differentSet(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    sol = Solution()
    result = sol.differentSet(nums1, nums2)
    print(result)
