'''
给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。

你可以返回满足此条件的任何数组作为答案。

 

示例：

输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
 

提示：

1 <= A.length <= 5000
0 <= A[i] <= 5000
'''
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        len_ = len(A)
        odd = even = 0
        while odd < len_ and even < len_:
            while odd < len_ and A[odd] % 2 == 0:
                odd += 1
            if odd >= len_:
                break
            even = odd
            while even < len_ and A[even] % 2 == 1:
                even += 1
            if even >= len_:
                break
            A[odd], A[even] = A[even], A[odd]
            odd += 1
            even += 1
        return A


if __name__ == '__main__':
    A = [2, 2, 2, 4, 3, 5, 1, 1, 1, 1, 1, 1]
    sol = Solution()
    print(sol.sortArrayByParity(A))
