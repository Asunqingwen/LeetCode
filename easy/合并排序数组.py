"""
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。

初始化 A 和 B 的元素数量分别为 m 和 n。

示例:

输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
说明:

A.length == n + m
"""
from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        p1, p2 = m - 1, 0
        while p2 < n:
            num = B[p2]
            p1 = m-1
            while p1 >=0 and num < A[p1]:
                A[p1+1],A[p1] = A[p1],A[p1+1]
                p1 -= 1
            A[p1+1] = num
            p2 += 1
            m += 1
        print(A)


if __name__ == '__main__':
    A = [2, 0]
    m = 1
    B = [1]
    n = 1
    sol = Solution()
    sol.merge(A, m, B, n)
