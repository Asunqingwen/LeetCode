"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
 

提示：你可以假定该字符串只包含小写字母。
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if c in count and count[c] == 1:
                return i
        return -1


if __name__ == '__main__':
    s = "leetcode"
    sol = Solution()
    print(sol.firstUniqChar(s))
