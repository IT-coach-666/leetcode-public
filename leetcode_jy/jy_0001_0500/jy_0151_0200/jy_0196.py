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
type_jy = ""
# jy: 记录该题的英文简称以及所属类别
title_jy = "Delete-Duplicate-Emails(SQL)"
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
 

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

For Pandas users, please note that you are supposed to modify Person in place.

After running your script, the answer shown is the `Person` table. The driver will first compile and run your piece of code and then show the Person table. The final order of the `Person` table does not matter.

The result format is in the following example.

 

Example 1:
Input: 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output: 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.
"""


# 自连接的方式
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

    
"""
有慢查询优化经验的同学会清楚，在实际生产中，面对千万上亿级别的数据，连接的效率往往最高，因为用到索引的概率较高

1) DELETE p1
在 DELETE 官方文档 (https://dev.mysql.com/doc/refman/8.0/en/delete.html) 中, 给出了这一用法, 比如下面这个 DELETE 语句:
DELETE t1 FROM t1 LEFT JOIN t2 ON t1.id=t2.id WHERE t2.id IS NULL;

这种 DELETE 方式很陌生, 竟然和 SELETE 的写法类似; 它涉及到 t1 和 t2 两张表, DELETE t1 表示要删除 t1 的一些记录, 具体删哪些, 就看 WHERE 条件, 满足就删

这里删的是 t1 表中, 跟 t2 匹配不上的那些记录

所以 DELETE p1 就表示从 p1 表中删除满足 WHERE 条件的记录


2) p1.Id > p2.Id

继续之前, 先简单看一下表的连接过程, 这个搞懂, 理解 WHERE 条件就简单了:
a) 从驱动表（左表）取出 N 条记录
b) 拿着这 N 条记录, 依次到被驱动表（右表）查找满足 WHERE 条件的记录

所以 sql 的过程就是:
a) 从表 p1 取出 3 条记录；
b) 拿着第 1 条记录去表 p2 查找满足 WHERE 的记录, 代入该条件 p1.Email = p2.Email AND p1.Id > p2.Id 后, 发现没有满足的, 所以不用删掉记录 1
c) 记录 2 同理
d) 拿着第 3 条记录去表 p2 查找满足 WHERE 的记录, 发现有一条记录满足, 所以要从 p1 删掉记录 3
e) 3 条记录遍历完, 删掉了 1 条记录, 这个 DELETE 也就结束了

"""
    
