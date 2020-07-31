"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

提示：

皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或七步，可进可退。（引用自 百度百科 - 皇后 ）
"""
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:

        def can_place(row, col):
            return not (cols[col] or hill_diagonals[row - col] or dale_diagonals[row + col])

        def place_queen(row, col):
            queens.append((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def remove_queen(row, col):
            queens.pop()
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        def helper(row=0):
            for col in range(n):
                if can_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        nonlocal res
                        res += 1
                    else:
                        helper(row + 1)
                    remove_queen(row, col)

        # 主对角线，左上角到右下角
        hill_diagonals = [0] * (2 * n - 1)
        # 次对角线，右下角到左下角
        dale_diagonals = [0] * (2 * n - 1)
        cols = [0] * n
        res = 0
        queens = []
        helper()
        return res


if __name__ == '__main__':
    n = 4
    sol = Solution()
    result = sol.solveNQueens(n)
    print(result)