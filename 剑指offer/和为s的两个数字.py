from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [nums[left], nums[right]]
        return []


if __name__ == '__main__':
    nums = [45, 46, 67, 73, 74, 74, 77, 83, 89, 98]
    target = 147
    sol = Solution()
    res = sol.twoSum(nums, target)
    print(res)
