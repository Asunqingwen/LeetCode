from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        count_ = set()
        for num in nums:
            if num in count_:
                return num
            count_.add(num)
