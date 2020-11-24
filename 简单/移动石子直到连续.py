'''
三枚石子放置在数轴上，位置分别为 a，b，c。

每一回合，我们假设这三枚石子当前分别位于位置 x, y, z 且 x < y < z。从位置 x 或者是位置 z 拿起一枚石子，并将该石子移动到某一整数位置 k 处，其中 x < k < z 且 k != y。

当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。

要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：answer = [minimum_moves, maximum_moves]
'''
from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, z = min(a, b, c), max(a, b, c)
        y = a + b + c - x - z
        left = y - x
        right = z - y
        max_ = z - x - 2
        min_ = 1
        if left == right == 1:
            min_ = 0
        elif left > 2 and right > 2:
            min_ = 2
        return [min_, max_]


if __name__ == '__main__':
    a = 4
    b = 3
    c = 2
    sol = Solution()
    print(sol.numMovesStones(a, b, c))
