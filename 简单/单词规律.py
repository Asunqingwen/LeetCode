"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
"""
from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False
        map_p = defaultdict()
        for i, p_c in enumerate(pattern):
            if (p_c in map_p and map_p[p_c] != s_list[i]) or (p_c not in map_p and s_list[i] in map_p.values()):
                return False
            map_p[p_c] = s_list[i]
        return True


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    sol = Solution()
    result = sol.wordPattern(pattern, s)
    print(result)
