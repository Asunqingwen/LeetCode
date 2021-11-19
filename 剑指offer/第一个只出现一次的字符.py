from collections import Counter, defaultdict


class Solution:
    def firstUniqChar1(self, s: str) -> str:
        counts = Counter(s)
        for c in s:
            if counts[c] == 1:
                return c
        return " "

    def firstUniqChar2(self, s: str) -> str:
        if not s:
            return " "
        indexs = defaultdict(int)
        for i, c in enumerate(s):
            if c in indexs:
                indexs[c] = -1
            else:
                indexs[c] = i
        len_ = len(s)
        pos = len_
        for index in indexs.values():
            if index != -1 and index < pos:
                pos = index
        return " " if pos == len_ else s[pos]
