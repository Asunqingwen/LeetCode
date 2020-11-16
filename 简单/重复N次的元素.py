'''
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。

返回重复了 N 次的那个元素。

 

示例 1：

输入：[1,2,3,3]
输出：3
示例 2：

输入：[2,1,2,5,3,2]
输出：2
示例 3：

输入：[5,1,5,2,5,3,5,4]
输出：5
 

提示：

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length 为偶数
'''
from typing import List
from collections import Counter


class Solution(object):
    def repeatedNTimes(self, A):
        for k in range(1, 4):
            for i in range(len(A) - k):
                if A[i] == A[i + k]:
                    return A[i]



if __name__ == '__main__':
    A = [1, 2, 3, 3]
    sol = Solution()
    print(sol.repeatedNTimes(A))
