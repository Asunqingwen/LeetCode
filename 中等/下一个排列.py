'''
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。

 

示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]
示例 4：

输入：nums = [1]
输出：[1]
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''
from typing import List


# 搞清楚，什么是字典序
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_ = len(nums)
        i = len_ - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i -= 1
        if i > 0:
            left_i = i - 1
            while i < len_ and nums[i] > nums[left_i]:
                i += 1
            right_i = i - 1
            nums[left_i], nums[right_i] = nums[right_i], nums[left_i]
        left_i += 1
        right_i = len_ - 1
        while left_i < right_i:
            nums[left_i], nums[right_i] = nums[right_i], nums[left_i]
            left_i += 1
            right_i -= 1


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    sol.nextPermutation(nums)
    print(nums)
