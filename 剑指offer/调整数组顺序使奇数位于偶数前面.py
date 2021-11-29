from typing import List

from decorator_ import print_run_time


class Solution:
    @print_run_time
    def exchange(self, nums: List[int]) -> List[int]:
        len_ = len(nums)
        odd, even = 0, len_ - 1
        while odd < even:
            while odd < even and nums[odd] & 1 == 1:
                odd += 1
            if odd == even:
                break
            while odd < even and nums[even] & 1 == 0:
                even -= 1
            if even == odd:
                break
            nums[odd], nums[even] = nums[even], nums[odd]
        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    sol = Solution()
    res = sol.exchange(nums)
    print(res)
