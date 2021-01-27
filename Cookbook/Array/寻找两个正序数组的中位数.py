'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000
 

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        half = (len1 + len2 + 1) >> 1
        left, right = 0, len1
        mid1 = mid2 = 0
        while left <= right:
            mid1 = (left + right) >> 1
            mid2 = half - mid1
            if mid1 > 0 and nums2[mid2] < nums1[mid1 - 1]:
                right = mid1 - 1
            elif mid1 < len1 and nums1[mid1] < nums2[mid2 - 1]:
                left = mid1 + 1
            else:
                break
        if mid1 == 0:
            midLeft = nums2[mid2 - 1]
        elif mid2 == 0:
            midLeft = nums1[mid1 - 1]
        else:
            midLeft = max(nums1[mid1 - 1], nums2[mid2 - 1])
        if (len1 + len2) & 1 == 1:
            return midLeft

        if mid1 == len1:
            midRight = nums2[mid2]
        elif mid2 == len2:
            midRight = nums1[mid1]
        else:
            midRight = min(nums1[mid1], nums2[mid2])
        return (midLeft + midRight) / 2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))
