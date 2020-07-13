"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            return self.intersect(nums2, nums1)
        ans = dict()
        res = []
        for num in nums1:
            ans[num] = ans.get(num, 0) + 1
        for num in nums2:
            if ans.get(num, 0):
                res.append(num)
                ans[num] -= 1
        return res


if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    sol = Solution()
    result = sol.intersect(nums1, nums2)
    print(result)
