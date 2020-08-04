"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
 

示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False
 

注意：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2所需字符
        need = dict()
        for c in s1:
            need[c] = need.get(c, 0) + 1

        # 窗口
        win = dict()
        # 窗口左右指针
        left, right = 0, 0
        # 字符种类
        valid = 0
        while right < len(s2):
            c = s2[right]
            # 窗口扩大
            right += 1
            if c in need:
                win[c] = win.get(c, 0) + 1
                if win[c] == need[c]:
                    valid += 1

            # 窗口缩小
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
                if need.get(d, 0) > 0:
                    if win[d] == need[d]:
                        valid -= 1
                    win[d] -= 1
        return False

    def checkInclusion1(self, s1: str, s2: str) -> bool:
        length = len(s1)
        left, right = 0, length
        win = dict()
        need = dict()
        valid = 0
        for c in s1:
            need[c] = need.get(c, 0) + 1
        while right <= len(s2):
            for i in range(left, right):
                c = s2[i]
                if c not in need:
                    break
                win[c] = win.get(c, 0) + 1
                if win[c] == need[c]:
                    valid += 1
            if valid == len(need):
                return True
            left += 1
            right += 1
            win.clear()
            valid = 0
        return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    sol = Solution()
    result = sol.checkInclusion1(s1, s2)
    print(result)
