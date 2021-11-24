class Solution:
    def translateNum(self, num: int) -> int:
        str_num = str(num)
        len_ = len(str_num)
        dp0 = 1
        dp1 = 1
        dp = 1
        for i in range(2, len_):
            if str_num[i - 2] == '1' or (str_num[i - 2] == '2' and str_num[i - 1] < '6'):
                dp = dp1 + dp0
            else:
                dp = dp1
            dp0, dp1 = dp1, dp
        return dp

if __name__ == '__main__':
    sol =Solution()
    sol.translateNum(18580)