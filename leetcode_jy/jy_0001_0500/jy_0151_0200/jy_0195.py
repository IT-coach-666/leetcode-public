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
title_jy = "Tenth-Line(shell)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a text file `file.txt`, print just the 10-th line of the file.

Example:
Assume that `file.txt` has the following content:
'''
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
'''

Your script should output the tenth line, which is:
'''
Line 10
'''

Note:
1) If the file contains less than 10 lines, what should you output?
2) There's at least three different solutions. Try to explore all possibilities.
"""


# 以下三种方式均可以运行通过
grep -n "" file.txt | grep -w '10' | cut -d: -f2
sed -n '10p' file.txt
awk '{if(NR==10){print $0}}' file.txt


# 但是考虑到说明中行数不足 10 的情况处理, 可以做如下处理
row_num=$(cat file.txt | wc -l)
echo $row_num
if [ $row_num -lt 10 ];then
    echo "The number of row is less than 10"
else
    awk '{if(NR==10){print $0}}' file.txt
fi

# 其中文件行数 row_num 可以使用如下几种方式获取
awk '{print NR}' file.txt | tail -n1
10
awk 'END{print NR}' file.txt 
10
grep -nc "" file.txt 
10
grep -c "" file.txt 
10
grep -vc "^$" file.txt 
10
grep -n "" file.txt|awk -F: '{print '}|tail -n1 | cut -d: -f1
10
grep -nc "" file.txt
10
sed -n "$=" file.txt 
10
wc -l file.txt 
10 file.txt
cat file.txt | wc -l
10
wc -l file.txt | cut -d' ' -f1
10


