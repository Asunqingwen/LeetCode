'''
给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。

 

示例 1：

输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案。
示例 2：

输入：nums = [1,2,4,8]
输出：[1,2,4,8]
 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
nums 中的所有整数 互不相同
'''
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        len_ = len(nums)
        nums.sort()

        dp = [1] * len_
        maxSize = 1
        maxVal = dp[0]  ## 初始化不影响结果
        for i in range(len_):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)  ## 以nums[j]为最大整数的集合加入nums[i]之后，整个集合大小和以nums[i]为最大整数的集合大小取最大的

            if dp[i] > maxSize:
                maxSize = dp[i]
                maxVal = nums[i]

        res = []
        if maxSize == 1:
            res.append(nums[0])
            return res
        for i in range(len_ - 1, -1, -1):
            if dp[i] == maxSize and maxVal % nums[i] == 0:
                res.append(nums[i])
                maxVal = nums[i]
                maxSize -= 1
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.largestDivisibleSubset(nums))
