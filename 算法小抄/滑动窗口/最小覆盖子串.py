"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        # 窗口
        win = dict()
        t_dict = dict()
        # 字符种类数
        valid = 0
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1

        # 记录最小覆盖子串的起始索引与长度
        start, length = 0, math.inf
        while right < len(s):
            # 移入窗口的字符
            c = s[right]
            # 窗口右滑
            right += 1
            # 窗口数据更新
            if c in t_dict:
                win[c] = win.get(c, 0) + 1
                # 如果对应字符个数相等，说明该字符已经匹配完
                if win[c] == t_dict[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while valid == len(t_dict):
                # 更新最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left
                # 移出窗口的字符
                d = s[left]
                # 左移窗口
                left += 1
                if t_dict.get(d, 0) > 0:
                    if win[d] == t_dict[d]:
                        valid -= 1
                    win[d] -= 1
        return "" if length == math.inf else s[start:start + length]


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    sol = Solution()
    result = sol.minWindow(S, T)
    print(result)
