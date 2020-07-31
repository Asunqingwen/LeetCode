"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)

        def helper(head=0):
            if head == length:
                res.append(nums[:])
            for i in range(head, length):
                # 将第一个元素放在首位
                nums[head], nums[i] = nums[i], nums[head]
                helper(head + 1)
                nums[head], nums[i] = nums[i], nums[head]

        helper()
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    result = sol.permute(nums)
    print(result)
