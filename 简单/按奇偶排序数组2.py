'''
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

 

示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
 

提示：

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        len_ = len(A)
        even, odd = 0, 1
        while even < len_ and odd < len_:
            while even < len_ and A[even] % 2 == 0:
                even += 2
            if even >= len_:
                break
            while odd < len_ and A[odd] % 2 == 1:
                odd += 2
            if odd >= len_:
                break
            A[even], A[odd] = A[odd], A[even]
            even += 2
            odd += 2
        return A


if __name__ == '__main__':
    A = [4, 2, 5, 7]
    sol = Solution()
    print(sol.sortArrayByParityII(A))
