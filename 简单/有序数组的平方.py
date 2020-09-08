"""
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

 

示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：

输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
 

提示：

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
"""
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        length = len(A)
        p1, p2, p = 0, length - 1, length - 1
        res = [0] * length
        while p1 <= p2:
            pow2 = A[p2] ** 2
            if A[p1] < 0:
                pow1 = A[p1] ** 2
                if pow1 > pow2:
                    res[p] = pow1
                    p1 += 1
                else:
                    res[p] = pow2
                    p2 -= 1
            else:
                res[p] = pow2
                p2 -= 1
            p -= 1
        return res


if __name__ == '__main__':
    A = [-4, -3, -2, -1]
    sol = Solution()
    result = sol.sortedSquares(A)
    print(result)
