# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 0012 15:09
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Implement Magic Dictionary.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""
from typing import List


class MagicDictionary:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.dict = {}

	def buildDict(self, dict: List[str]) -> None:
		"""
		Build a dictionary through a list of words
		"""
		for word in dict:
			key = len(word)
			if key in self.dict:
				self.dict[key].append(word)
			else:
				self.dict[key] = [word]

	def search(self, word: str) -> bool:
		"""
		Returns if there is any word in the trie that equals to the given word after modifying exactly one character
		"""
		key = len(word)
		if key not in self.dict:
			return False
		for w in self.dict[key]:
			dif = 0
			for i in range(key):
				if w[i] != word[i]:
					dif += 1
			if dif == 1:
				return True
		return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
if __name__ == '__main__':
	obj = MagicDictionary()
	param1 = obj.buildDict(['hello', 'leetcode'])
	# param1 = obj.buildDict([])
	param2 = obj.search('hello')
	param3 = obj.search('hhllo')
	param4 = obj.search("hell")
	param5 = obj.search("leetcoded")
	print(param1, param2, param3, param4, param5)
