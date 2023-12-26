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
title_jy = "Valid-Phone-Numbers(shell)"
# jy: 记录不同解法思路的关键词
tag_jy = ""

"""
Given a text file `file.txt` that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats (x means a digit): 
(xxx) xxx-xxxx
or:  
xxx-xxx-xxxx

You may also assume each line in the text file must not contain leading or trailing white spaces.

Example:
Assume that `file.txt` has the following content:
'''
987-123-4567
123 456 7890
(123) 456-7890
'''

Your script should output the following valid phone numbers:
'''
987-123-4567
(123) 456-7890
'''
"""


# grep 与 awk 或 gawk
grep -P '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt

awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt

gawk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt
