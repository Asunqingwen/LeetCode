"""
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [1] * length
        lens = [1] * length
        for i in range(1, length):
            ans = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    #获取最大长度
                    if dp[j] >= dp[i]:
                        dp[i] = dp[j] + 1
                        lens[i] = lens[j]
                    #相等长度累积
                    elif dp[j] + 1 == dp[i]:
                        lens[i] += lens[j]

            dp[i] += ans
        res = 0
        max_length = max(dp)
        for i, l in enumerate(lens):
            if dp[i] == max_length:
                res += l
        return res


if __name__ == '__main__':
    nums = [2, 2, 2, 2, 2]
    sol = Solution()
    result = sol.findNumberOfLIS(nums)
    print(result)
