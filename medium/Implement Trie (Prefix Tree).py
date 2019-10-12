# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 0012 14:22
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Implement Trie (Prefix Tree).py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class Trie:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.trie = {}

	def insert(self, word: str) -> None:
		"""
		Inserts a word into the trie.
		"""
		curr_trie = self.trie
		for w in word:
			if w not in curr_trie:
				curr_trie[w] = {}
			curr_trie = curr_trie[w]
		curr_trie['end'] = True

	def search(self, word: str) -> bool:
		"""
		Returns if the word is in the trie.
		"""
		curr_trie = self.trie
		for w in word:
			if w not in curr_trie:
				return False
			curr_trie = curr_trie[w]
		return 'end' in curr_trie

	def startsWith(self, prefix: str) -> bool:
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		"""
		curr_trie = self.trie
		for p in prefix:
			if p not in curr_trie:
				return False
			curr_trie = curr_trie[p]
		return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
	obj = Trie()
	obj.insert("hello")
	param1 = obj.startsWith("helloa")
	print(param1)
