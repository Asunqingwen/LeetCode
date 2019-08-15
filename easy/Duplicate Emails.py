# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 9:16
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Duplicate Emails.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
Write a SQL query to find all duplicate emails in a table named Person.

| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com

For example, your query should return the following for the above table:
| Email   |
+---------+
| a@b.com |
+---------+

Note: All emails are in lowercase.
"""
"""
select Email from Person group by Email having count(Email) > 1
"""