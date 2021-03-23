'''
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
说明:

A.length == n + m
'''
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index, first, second = m + n - 1, m - 1, n - 1
        while first >= 0 and second >= 0:
            if nums1[first] >= nums2[second]:
                nums1[index] = nums1[first]
                first -= 1
            else:
                nums1[index] = nums2[second]
                second -= 1
            index -= 1
        while second >= 0:
            nums1[index] = nums2[second]
            second -= 1
            index -= 1


if __name__ == '__main__':
    A = [1, 2, 3, 0, 0, 0]
    m = 3
    B = [2, 5, 6]
    n = 3
    sol = Solution()
    sol.merge(A, m, B, n)
    print(A)
