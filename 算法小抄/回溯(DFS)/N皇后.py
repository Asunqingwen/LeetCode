"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
 

提示：

皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自 百度百科 - 皇后 ）
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

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

        def add_solution():
            solution = []
            for _, col in queens:
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            res.append(solution)

        def helper(row=0):
            for col in range(n):
                if can_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        helper(row + 1)
                    remove_queen(row, col)

        # 主对角线，左上角到右下角
        hill_diagonals = [0] * (2 * n - 1)
        # 次对角线，右下角到左下角
        dale_diagonals = [0] * (2 * n - 1)
        cols = [0] * n
        res = []
        queens = []
        helper()
        return res


if __name__ == '__main__':
    n = 4
    sol = Solution()
    result = sol.solveNQueens(n)
    print(result)
