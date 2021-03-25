'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
 

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成
 

进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
'''
import math
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def check():  # 检查当前滑动窗口内字母的个数是否和t中字母个数符合
            for k, v in ori.items():
                if cnt[k] < v:
                    return False
            return True

        ori = Counter(t)
        cnt = defaultdict(int)
        left, right = 0, 0
        len_, ans_left = math.inf, -1
        while right < len(s):
            if s[right] in ori:
                cnt[s[right]] += 1
            while check() and left <= right:  # 缩小滑动窗口左边界
                if right - left + 1 < len_:
                    len_ = right - left + 1
                    ans_left = left
                if s[left] in ori:
                    cnt[s[left]] -= 1
                left += 1
            right += 1

        return "" if ans_left == -1 else s[ans_left:ans_left + len_]


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    print(sol.minWindow(s, t))
