'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def helper(candidates, index, target):
            if target == 0:
                res.append(ans[:])
                return
            for i in range(index, len(candidates)):
                if target < candidates[i]:
                    break
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                ans.append(candidates[i])
                helper(candidates, i + 1, target - candidates[i])
                ans.pop()
            return

        if not candidates:
            return []
        res = list()
        ans = list()
        candidates.sort()
        helper(candidates, 0, target)
        return list(res)


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    sol = Solution()
    print(sol.combinationSum2(candidates, target))
