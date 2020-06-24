"""
给你一个整数数组 A 和一个整数 K，请在该数组中找出两个元素，使它们的和小于 K 但尽可能地接近 K，返回这两个元素的和。

如不存在这样的两个元素，请返回 -1。

 

示例 1：

输入：A = [34,23,1,24,75,33,54,8], K = 60
输出：58
解释：
34 和 24 相加得到 58，58 小于 60，满足题意。
示例 2：

输入：A = [10,20,30], K = 15
输出：-1
解释：
我们无法找到和小于 15 的两个元素。
 

提示：

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""
from typing import List


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        ans = -1
        left, right = 0, len(A) - 1
        while left < right:
            sum = A[left] + A[right]
            if sum < K:
                # 所以小于K的和里面找到最大值
                ans = max(ans, sum)
                left += 1
            else:
                right -= 1

        return ans


if __name__ == '__main__':
    A = [10, 20, 30]
    K = 15
    sol = Solution()
    result = sol.twoSumLessThanK(A, K)
    print(result)
