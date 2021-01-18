'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 

提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
'''
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k=0):
            nonlocal row, col, len_
            if board[i][j] != word[k]:
                return False
            if k == len_:
                return True
            visited.add((i, j))
            result = False
            for d in dd:
                new_i, new_j = i + d[0], j + d[1]
                if 0 <= new_i < row and 0 <= new_j < col and (new_i, new_j) not in visited and dfs(new_i, new_j, k + 1):
                    result = True
                    break
            visited.remove((i, j))
            return result

        dd = ((-1, 0), (1, 0), (0, -1), (0, 1))
        row, col, len_ = len(board), len(board[0]), len(word) - 1
        visited = set()
        for i in range(row):
            for j in range(col):
                if dfs(i, j):
                    return True
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCB"
    sol = Solution()
    print(sol.exist(board, word))
