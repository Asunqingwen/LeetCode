"""
f(x) 是 x! 末尾是0的数量。（回想一下 x! = 1 * 2 * 3 * ... * x，且0! = 1）

例如， f(3) = 0 ，因为3! = 6的末尾没有0；而 f(11) = 2 ，因为11!= 39916800末端有2个0。给定 K，找出多少个非负整数x ，有 f(x) = K 的性质。

示例 1:
输入:K = 0
输出:5
解释: 0!, 1!, 2!, 3!, and 4! 均符合 K = 0 的条件。

示例 2:
输入:K = 5
输出:0
解释:没有匹配到这样的 x!，符合K = 5 的条件。
注意：

K是范围在 [0, 10^9] 的整数。
"""


class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        def helper(n):
            count = 0
            while n > 0:
                n //= 5
                count += n
            return count

        if K == 0:
            return 5
        left, right = 5, 10 * K + 1
        while left < right:
            mid = left + (right - left) // 2
            count = helper(mid)
            if count == K:
                return 5
            elif count < K:
                left = mid + 1
            else:
                right = mid - 1

        return 0


if __name__ == '__main__':
    K = 3
    sol = Solution()
    result = sol.preimageSizeFZF(K)
    print(result)
