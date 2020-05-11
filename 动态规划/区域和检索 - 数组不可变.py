"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dp = [0 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.dp[i+1] = self.dp[i] + self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    nums = [-2,0,3,-5,2,-1]
    obj = NumArray(nums)
    param_1 = obj.sumRange(0, 2)
    print(param_1)
    param_1 = obj.sumRange(2, 5)
    print(param_1)
    param_1 = obj.sumRange(0, 5)
    print(param_1)
