'''
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]

        def helper(start, end, ans):
            if start == end:
                return
            for i in range(start, end):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                ans.append(nums[i])
                res.append(ans[:])
                helper(i + 1, end, ans)
                ans.pop()

        helper(0, len(nums), [])
        return list(res)


if __name__ == '__main__':
    nums = [4, 4, 4, 1, 4]
    sol = Solution()
    print(sol.subsetsWithDup(nums))
