from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, index) -> bool:
            if len_ == index:
                return True
            if r < 0 or r >= rows:
                return False
            if c < 0 or c >= cols:
                return False
            if word[index] != board[r][c]:
                return False
            board[r][c] = '*'
            if dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or dfs(r, c + 1, index + 1) or dfs(r, c - 1,
                                                                                                       index + 1):
                return True
            board[r][c] = word[index]
            return False

        if not board or not board[0]:
            return True
        rows, cols = len(board), len(board[0])
        len_ = len(word)
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False
