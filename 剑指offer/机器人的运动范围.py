class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k == 0:
            return 1

        def getSum(num: int) -> int:
            sum_ = 0
            while num > 0:
                div, mod = divmod(num, 10)
                sum_ += mod
                num = div
            return sum_

        paths = [(0, 0)]
        dd = [(0, 1), (1, 0)]
        s = set()
        s.add(paths[0])
        while paths:
            x, y = paths.pop(0)
            for i, j in dd:
                new_x, new_y = i + x, j + y
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or (new_x, new_y) in s or getSum(
                        new_x) + getSum(new_y) > k:
                    continue
                paths.append((new_x, new_y))
                s.add((new_x, new_y))
        return len(s)


if __name__ == '__main__':
    m = 2
    n = 3
    k = 1
    sol = Solution()
    sol.movingCount(m, n, k)
