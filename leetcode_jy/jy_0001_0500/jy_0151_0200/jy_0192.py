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
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Word-Frequency(shell)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Write a bash script to calculate the frequency of each word in a text file `words.txt`.

For simplicity sake, you may assume:
1) `words.txt` contains only lowercase characters and space ' ' characters.
2) Each word must consist of lowercase characters only.
3) Words are separated by one or more whitespace characters.

Example:
Assume that `words.txt` has the following content:
'''
the day is sunny the the
the sunny is is
'''

Your script should output the following, sorted by descending frequency:
'''
the 4
is 3
sunny 2
day 1
'''

Note:
1) Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
2) Could you write it in one-line using Unix pipes?
"""

# 综合使用的 shell 命令
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2, $1 }'

# 注意: 当单词的出现次数大于 10 时, sort 需要考虑按数字排序, 而非默认的按 ascii 码排序
cat words.txt | tr -s ' ' '\n'|sort|uniq -c|sort -nr|awk '{print $2" "$1}'


# 1) 切割
#    tr 命令用于转换或删除文件中的字符
#    -s: 缩减连续重复的字符成指定的单个字符
cat Words.txt| tr -s ' ' '\n'
'''
the
day
is
sunny
the
the
the
sunny
is
is
'''



# 2) 排序单词
cat Words.txt| tr -s ' ' '\n' | sort
'''
day
is
is
is
sunny
sunny
the
the
the
the
'''


# 3) 统计单词出现次数
#    uniq 命令用于检查及删除文本文件中重复出现的行列, 一般与 sort 命令结合使用
#    -c: 在每列旁边显示该行重复出现的次数
cat Words.txt| tr -s ' ' '\n' | sort | uniq -c
'''
1 day
3 is
2 sunny
4 the
'''


# 4) 排序单词出现次数
#    -r: 以相反的顺序来排序
cat Words.txt| tr -s ' ' '\n' | sort | uniq -c | sort -r
'''
4 the
3 is
2 sunny
1 day
'''


# 5) 打印
cat Words.txt| tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'
'''
the 4
is 3
sunny 2
day 1
'''


# 解法 2: awk + sort
cat words.txt |awk '{for (i=1; i<=NF; i++) {g[$i] += 1}} END{for (j in g) print j,g[j]}' |sort -k2,2 -nr


# 解法 3: 替换/排序/统计次数/过滤空行/排序次数/打印
sed 's/ /\n/g' words.txt|sort|uniq -c|grep -Ev ' $' |sort -nr |awk '{print $2,$1}'
