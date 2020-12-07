'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000
'''
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        len_ = len(nums)
        odd, even = 0, len_ - 1
        while odd < even:
            if nums[odd] % 2 == 1:
                odd += 1
            elif nums[even] % 2 == 0:
                even -= 1
            else:
                nums[odd], nums[even] = nums[even], nums[odd]
                odd += 1
                even -= 1
        return nums


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 4]
    sol = Solution()
    print(sol.exchange(nums))
