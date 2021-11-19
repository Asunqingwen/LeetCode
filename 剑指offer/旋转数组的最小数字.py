from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = (left + right) >> 1
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right -= 1
        return numbers[left]


if __name__ == '__main__':
    sol = Solution()
    numbers = [3, 4, 5, 1, 2]
    res = sol.minArray(numbers)
    print(res)
