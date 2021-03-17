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
        row, col = len(board), len(board[0])
        len_ = len(word)
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = set()

        def check(i, j, k, len_, row, col):
            if board[i][j] != word[k]:
                return False
            if k == len_ - 1:
                return True
            visited.add((i, j))
            result = False
            for dx, dy in directions:
                new_i = dx + i
                new_j = dy + j
                if 0 <= new_i < row and 0 <= new_j < col:
                    if (new_i, new_j) not in visited:
                        if check(new_i, new_j, k + 1, len_, row, col):
                            result = True
                            break
            visited.remove((i, j))
            return result

        for i in range(row):
            for j in range(col):
                if check(i, j, 0, len_, row, col):
                    return True
        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    sol = Solution()
    word = "ABCCED"
    print(sol.exist(board, word))
