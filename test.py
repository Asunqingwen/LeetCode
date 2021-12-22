from collections import Counter


class Solution(object):
    def originalDigits(self, s):
        str2nums = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
                    'seven': '7', 'eight': '8', 'nine': '9'}
        str_count = Counter(s)
        res = ''
        digits = [i for i in range(10)]
        digits[0] = str_count.get('z', 0)
        digits[2] = str_count.get('w', 0)
        digits[4] = str_count.get('u', 0)
        digits[5] = str_count.get('f', 0) - digits[4]
        digits[6] = str_count.get('x', 0)
        digits[3] = str_count.get('r', 0) - digits[4]
        digits[1] = str_count.get('o', 0) - digits[0] - digits[2] - digits[4]
        digits[7] = str_count.get('s', 0) - digits[6]
        digits[8] = str_count.get('g', 0)
        digits[9] = str_count.get('i', 0) - digits[5] - digits[6] - digits[8]
        for i in range(10):
            if digits[i] > 0:
                res += str(i) * digits[i]
        return res


if __name__ == '__main__':
    sol = Solution()
    sol.originalDigits('sssss')
