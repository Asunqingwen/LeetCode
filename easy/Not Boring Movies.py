# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 10:10
# @Author  : 没有蜡笔的小新
# @E-mail  : sqw123az@sina.com
# @FileName: Not Boring Movies.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/Asunqingwen
# @GitHub  ：https://github.com/Asunqingwen

"""
X city opened a new cinema, many people would like to go to this cinema. The cinema also gives out a poster indicating the movies’ ratings and descriptions.
Please write a SQL query to output movies with an odd numbered ID and a description that is not 'boring'. Order the result by rating.
"""
"""
select id,movie,description,rating from cinema where id %2 != 0 and description != 'boring' order by rating desc 
"""