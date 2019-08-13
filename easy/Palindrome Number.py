"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
"""


def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    revert_num = 0
    while revert_num < x:
        revert_num = revert_num * 10 + x % 10
        x //= 10
    return x == revert_num or x == revert_num // 10


if __name__ == '__main__':
    m = 10

    result = isPalindrome(m)
    print(result)
