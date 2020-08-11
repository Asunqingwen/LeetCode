"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def threeSum(n, nums, start, target) -> List[List[int]]:
            ans = []
            # 枚举 a
            for first in range(start, n):
                # 需要和上一次枚举的数不相同
                if first > start and nums[first] == nums[first - 1]:
                    continue
                # c 对应的指针初始指向数组的最右端
                third = n - 1
                tmp = target - nums[first]
                # 枚举 b
                for second in range(first + 1, n):
                    # 需要和上一次枚举的数不相同
                    if second > first + 1 and nums[second] == nums[second - 1]:
                        continue
                    # 需要保证 b 的指针在 c 的指针的左侧
                    while second < third and nums[second] + nums[third] > tmp:
                        third -= 1
                    # 如果指针重合，随着 b 后续的增加
                    # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                    if second == third:
                        break
                    if nums[second] + nums[third] == tmp:
                        ans.append([nums[first], nums[second], nums[third]])
            return ans

        res = []
        n = len(nums)
        nums.sort()
        i = 0
        while i < n:
            triples = threeSum(n, nums, i + 1, target - nums[i])
            for triple in triples:
                triple.append(nums[i])
                res.append(triple)
            # while i < n - 1 and nums[i] == nums[i + 1]:
            #     i += 1
            i += 1
        return res


if __name__ == '__main__':
    nums = [0, 0, 0, 0]
    target = 0
    sol = Solution()
    result = sol.fourSum(nums, target)
    print(result)
