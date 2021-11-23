class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        f0, f1 = 1, 1
        res = 0
        for _ in range(2, n + 1):
            res = f0 + f1
            f0, f1 = f1, res
        return res % (1000000007)
