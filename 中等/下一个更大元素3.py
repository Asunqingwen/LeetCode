'''
给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。

注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

 

示例 1：

输入：n = 12
输出：21
示例 2：

输入：n = 21
输出：-1
 

提示：

1 <= n <= 231 - 1
'''


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [int(s) for s in str(n)]
        len_ = len(nums)
        i = len_ - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1
        if i == 0:
            return -1
        p = i - 1
        while i < len_:
            if nums[i] <= nums[p]:
                break
            i += 1
        nums[p], nums[i - 1] = nums[i - 1], nums[p]
        i = len_ - 1
        p += 1
        while p < i:
            nums[p], nums[i] = nums[i], nums[p]
            p += 1
            i -= 1
        res = 0

        for num in nums:
            res = 10 * res + num
        return res if res < 2 ** 31 else -1


if __name__ == '__main__':
    n = 12388123
    sol = Solution()
    print(sol.nextGreaterElement(n))
