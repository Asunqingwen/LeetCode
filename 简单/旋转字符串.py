"""
给定两个字符串, A 和 B。

A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后，A 能变成B，那么返回True。

示例 1:
输入: A = 'abcde', B = 'cdeab'
输出: true

示例 2:
输入: A = 'abcde', B = 'abced'
输出: false
注意：

A 和 B 长度不超过 100。
"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        lena, lenb = len(A), len(B)
        if lena != lenb:
            return False
        if lena == 0:
            return True
        A += A
        lena *= 2
        dp = [[0] * 128 for _ in range(lenb)]
        dp[0][ord(B[0])] = 1
        x = 0
        for j in range(1, lenb):
            for c in range(128):
                dp[j][c] = dp[x][c]
            dp[j][ord(B[j])] = j + 1
            x = dp[x][ord(B[j])]
        j = 0
        for i in range(lena):
            j = dp[j][ord(A[i])]
            if j == lenb:
                return True
        return False


if __name__ == '__main__':
    A = "bbbacddceeb"
    B = "ceebbbbacdd"
    sol = Solution()
    print(sol.rotateString(A, B))
