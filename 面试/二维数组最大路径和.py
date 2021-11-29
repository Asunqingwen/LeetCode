from typing import List


def getMaxSum(nums: List) -> int:
    rows, cols = len(nums), len(nums[0])
    for i in range(1, rows):
        nums[i][0] += nums[i - 1][0]
    for j in range(1, cols):
        nums[0][j] += nums[0][j - 1]
    for i in range(1, rows):
        for j in range(1, cols):
            nums[i][j] += max(nums[i - 1][j], nums[i][j - 1])
    return nums[-1][-1]


if __name__ == '__main__':
    nums = [[1],
            [2],
            [3],
            [4],
            [5]]
    res = getMaxSum(nums)
    print(res)
