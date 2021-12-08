from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        max_, min_ = 0, 14
        for num in nums:
            if num == 0:
                continue
            max_ = max(max_, num)
            min_ = min(min_, num)
            if num in repeat:
                return False
            repeat.add(num)
        return max_ - min_ < 5
