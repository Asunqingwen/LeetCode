# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 0012 11:44
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Replace Words.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
 

Note:

The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""
from typing import List


def replaceWords(dict: List[str], sentence: str) -> str:
	# 字典树初始化
	dict_tree = {}
	for word in dict:
		tmp = dict_tree
		for w in word:
			if w not in tmp:
				tmp[w] = {}
			tmp = tmp[w]
		tmp['end'] = True

	def helper(word):
		tmp = dict_tree
		for i, w in enumerate(word):
			if 'end' in tmp:
				return word[:i]
			elif w not in tmp:
				break
			tmp = tmp[w]
		return word

	return ' '.join(map(helper, sentence.split(' ')))


if __name__ == '__main__':
	dict = ["cat", "bat", "rat"]
	sentence = "the cattle was rattled by the battery"
	result = replaceWords(dict, sentence)
	print(result)