from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = -1
        len_ = len(s)
        res = 0
        hash_ = defaultdict(str)
        for right in range(len_):
            if s[right] in hash_ and hash_[s[right]] > left:
                left = hash_[s[right]]  # 更新左指针
            hash_[s[right]] = right
            if res < right - left:
                res = right - left

        return res


if __name__ == '__main__':
    sol = Solution()
    sol.lengthOfLongestSubstring("abcabcbb")
