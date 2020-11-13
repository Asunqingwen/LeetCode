'''
给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

如果 S[i] == "I"，那么 A[i] < A[i+1]
如果 S[i] == "D"，那么 A[i] > A[i+1]
 

示例 1：

输入："IDID"
输出：[0,4,1,3,2]
示例 2：

输入："III"
输出：[0,1,2,3]
示例 3：

输入："DDI"
输出：[3,2,0,1]
 

提示：

1 <= S.length <= 10000
S 只包含字符 "I" 或 "D"。
'''
from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        len_ = len(S)
        min, max = 0, len_
        res = [0] * (len_ + 1)
        for i in range(len_):
            if S[i] == 'I':
                res[i] = min
                min += 1
            elif S[i] == 'D':
                res[i] = max
                max -= 1
        res[len_] = max
        return res


if __name__ == '__main__':
    S = "IDID"
    sol = Solution()
    print(sol.diStringMatch(S))
