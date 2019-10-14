# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 0014 9:37
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Short Encoding of Words.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].
 

Note:

1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters.
"""
from typing import List


def minimumLengthEncoding(words: List[str]) -> int:
	words = [word[::-1] for word in words]
	words.sort()
	res = 0
	for i in range(len(words)):
		if i + 1 < len(words) and words[i + 1][:len(words[i])] == words[i]:
			continue
		res += len(words[i]) + 1
	return res


def minimumLengthEncoding1(words: List[str]) -> int:
	words = sorted(words, key=lambda x: x[::-1], reverse=True)
	res = []
	cur_word = words[0]
	res.append(cur_word)
	for word in words:
		if word not in cur_word:
			cur_word = word
			res.append(cur_word)
	count = 0
	for i in res:
		count += len(i)
	return len(res) + count


if __name__ == '__main__':
	words = ["me", "time", "bell"]
	result = minimumLengthEncoding1(words)
	print(result)
