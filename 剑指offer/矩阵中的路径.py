from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        i = 0
        for row in rows:
            for col in cols:
                if board[row][col] == word[i]:
