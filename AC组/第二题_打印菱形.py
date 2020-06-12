"""
一个正整数m（1~26），表示菱形的半径（直径就是m*2+1）
"""


class Solution:
    def __init__(self):
        self.alpha = [chr(i) for i in range(65, 91)]

    def printLingXing(self, m: int) -> None:
        for i in range(m):
            p_str = [' '] * (2 * m - 1)
            for j in range(i + 1):
                p_str[m + j - 1] = self.alpha[i - j]
                p_str[m - j - 1] = self.alpha[i - j]
            print(''.join(p_str))
        for i in range(m - 2, -1, -1):
            p_str = [' '] * (2 * m - 1)
            for j in range(i + 1):
                p_str[m + j - 1] = self.alpha[i - j]
                p_str[m - j - 1] = self.alpha[i - j]
            print(''.join(p_str))


if __name__ == '__main__':
    m = 8
    sol = Solution()
    sol.printLingXing(m)
