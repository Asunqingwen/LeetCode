"""
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

 

示例 1：

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
示例 2：

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
示例 3：

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
 

提示：

1 <= s.length <= 5 x 10^5
s 只包含小写英文字母。
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 元音字母初始都出现了0次，即status = 0
        result, status, length = 0, 0, len(s)
        # 初始化数组，奇偶性都不确定，赋值为1
        pos = [-1 for _ in range(32)]
        pos[0] = 0
        for i in range(length):
            # u,o,i,e,a的顺序存储
            if s[i] == 'a':
                # 异或，改变当前元音字母的奇偶性
                status ^= 1 << 0
            elif s[i] == 'e':
                status ^= 1 << 1
            elif s[i] == 'i':
                status ^= 1 << 2
            elif s[i] == 'o':
                status ^= 1 << 3
            elif s[i] == 'u':
                status ^= 1 << 4
            # 如果这个位置的奇偶性在之前就出现过，那么更新符合条件字符串的最大长度
            # 奇数减奇数，中间一段元音字母就是偶数；偶数同理
            # if pos[status] != -1:
            if ~pos[status]:
                result = max(result, i + 1 - pos[status])
            else:
                pos[status] = i + 1
        return result


if __name__ == '__main__':
    s = "eleetminicoworoep"
    sol = Solution()
    result = sol.findTheLongestSubstring(s)
    print(result)
