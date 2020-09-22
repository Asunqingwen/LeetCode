"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

 

示例：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            num = 0
            while n > 0:
                n, digit = divmod(n, 10)
                num += digit ** 2
            return num

        # 快慢指针
        slow_num = n
        fast_num = get_next(n)
        while fast_num != 1 and slow_num != fast_num:
            # 每次计算下一个数
            slow_num = get_next(slow_num)
            # 每次计算下两个数
            fast_num = get_next(get_next(fast_num))
        return fast_num == 1


if __name__ == '__main__':
    n = 2
    sol = Solution()
    result = sol.isHappy(n)
    print(result)
