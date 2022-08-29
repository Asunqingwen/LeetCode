
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def isUgly(self, num: int) -> bool:
            if num <= 0:
                return False
            while num % 2 == 0:
                num /= 2
            while num % 3 == 0:
                num /= 3
            while num % 5 == 0:
                num /= 5
            return num == 1

# leetcode submit region end(Prohibit modification and deletion)
