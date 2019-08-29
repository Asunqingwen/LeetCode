# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 0029 16:29
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Employee Importance.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen
"""
You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
 

Note:

One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.

企业：中国联通 优步
标签：深度优先搜索 广度优先搜索 哈希表
"""


# Employee info
class Employee:
	def __init__(self, id, importance, subordinates):
		# It's the unique id of each node.
		# unique id of this employee
		self.id = id
		# the importance value of this employee
		self.importance = importance
		# the id of direct subordinates
		self.subordinates = subordinates


def listToEmployee(input):
	res = []
	for i in input:
		employee = Employee(i[0], i[1], i[2])
		res.append(employee)
	return res


def getImportance(employees, id):
	res = {}
	for em in employees:
		res[em.id] = list([em.importance, em.subordinates])
	count = 0
	sub_queue = []

	count += res[id][0]
	for sub in res[id][1]:
		sub_queue.append(sub)
	while sub_queue:
		temp = sub_queue.pop(0)
		count += res[temp][0]
		if res[temp][1]:
			for sub in res[temp][1]:
				sub_queue.append(sub)
	return count


if __name__ == '__main__':
	input = [[1, 2, [2]], [2, 3, []]]
	employees = listToEmployee(input)
	id = 2
	result = getImportance(employees, id)
	print(result)
