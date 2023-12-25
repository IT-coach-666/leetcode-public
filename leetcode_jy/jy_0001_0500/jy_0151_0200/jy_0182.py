# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
assert project_name == "leetcode_jy" and project_name == "leetcode_jy" and \
       url_ == "www.yuque.com/it-coach"
from typing import List, Dict
# jy: 记录该题的难度系数
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Duplicate-Emails(SQL)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

The result format is in the following example.

 

Example 1:
Input: 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output: 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.
"""

# 解法 1: 使用 GROUP BY 和临时表
# 重复的电子邮箱存在多次; 要计算每封电子邮件的存在次数, 可以使用以下代码:
select Email, count(Email) as num
from Person
group by Email;
'''
| Email   | num |
|---------|-----|
| a@b.com | 2   |
| c@d.com | 1   |
'''

# 以此作为临时表, 可以得到下面的解决方案:
select Email from
(
  select Email, count(Email) as num
  from Person
  group by Email
) as statistic
where num > 1
;


# 解法 2: 使用 GROUP BY 和 HAVING 条件
# 向 GROUP BY 添加条件的一种更常用的方法是使用 HAVING 子句, 该子句更为简单高效

select Email
from Person
group by Email
having count(Email) > 1;


