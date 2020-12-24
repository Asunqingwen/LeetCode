'''
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13
提示:

n范围在[1, 1000000]之间
'''


class Solution:
    def waysToStep(self, n: int) -> int:
        if n < 3:
            return n
        n0, n1, n2 = 1, 1, 2
        for _ in range(3, n + 1):
            n0, n1, n2 = n1, n2, (n0 + n1 + n2) % 1000000007

        return n2 % 1000000007


if __name__ == '__main__':
    n = 5
    sol = Solution()
    print(sol.waysToStep(n))
