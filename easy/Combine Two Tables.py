# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 0026 14:29
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Combine Two Tables.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

FirstName, LastName, City, State
"""

"""
select FirstName,LastName,City,State from Person left join Address on Person.PersonId = Address.PersonId
"""
