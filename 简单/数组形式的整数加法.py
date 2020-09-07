"""
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

 

示例 1：

输入：A = [1,2,0,0], K = 34
输出：[1,2,3,4]
解释：1200 + 34 = 1234
示例 2：

输入：A = [2,7,4], K = 181
输出：[4,5,5]
解释：274 + 181 = 455
示例 3：

输入：A = [2,1,5], K = 806
输出：[1,0,2,1]
解释：215 + 806 = 1021
示例 4：

输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
输出：[1,0,0,0,0,0,0,0,0,0,0]
解释：9999999999 + 1 = 10000000000
 

提示：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
如果 A.length > 1，那么 A[0] != 0
"""
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        num1 = ''.join([str(a) for a in A])
        num2 = str(K)
        num1l, num2l = len(num1), len(num2)
        if num1l < num2l:
            num1, num2 = num2, num1
            num1l, num2l = num2l, num1l
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = ''
        i, j = 0, 0
        dd = 0
        while i < num1l and j < num2l:
            tmp = int(num1[i]) + int(num2[i]) + dd
            curr = tmp % 10
            dd = tmp // 10
            res = str(curr) + res
            i += 1
            j += 1
        while i < num1l:
            tmp = int(num1[i]) + dd
            curr = tmp % 10
            dd = tmp // 10
            res = str(curr) + res
            i += 1
        if dd > 0:
            res = str(dd) + res
        return res


if __name__ == '__main__':
    A = [1, 2, 0, 0]
    K = 34
    sol = Solution()
    result = sol.addToArrayForm(A, K)
    print(result)
