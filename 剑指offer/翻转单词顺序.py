class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.strip().split(' ')
        strs.reverse()
        return ' '.join([str_ for str_ in strs if str_ != ' '])
