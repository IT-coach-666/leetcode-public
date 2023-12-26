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
title_jy = "Transpose-File(shell)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a text file `file.txt`, transpose its content.

You may assume that each row has the same number of columns, and each field is separated by the ' ' character.

Example:
If `file.txt` has the following content:
'''
name age
alice 21
ryan 30
'''

Output the following:
'''
name alice ryan
age 21 30
'''
"""

# 解法 1:
"""
awk 是一行一行地处理文本文件, 运行流程:
1) 先运行 BEGIN 后的 {Action}, 相当于表头
2) 再运行 {Action} 中的文件处理主体命令
3) 最后运行 END 后的 {Action} 中的命令

有几个经常用到的 awk 常量: 
NF 是当前行的 field 字段数
NR 是正在处理的当前行数

注意到是转置, 假如原始文本有 m 行 n 列 (字段), 则转置后的文本应该有 n 行 m 列, 即原始文本的每个字段都对应新文本的一行; 我们可以用数组 res 来储存新文本, 将新文本的每一行存为数组 res 的一个元素

在 END 之前我们遍历 file.txt 的每一行, 并做一个判断: 在第一行时, 每碰到一个字段就将其按顺序放在 res 数组中; 从第二行开始起, 每碰到一个字段就将其追加到对应元素的末尾 (中间添加一个空格)

文本处理完了, 最后需要输出; 在 END 后遍历数组, 输出每一行; 注意 printf 不会自动换行, 而 print 会自动换行
"""

awk '{
    for (i=1;i<=NF;i++){
        if (NR==1){
            res[i]=$i
        }
        else{
            res[i]=res[i]" "$i
        }
    }
}END{
    for(j=1;j<=NF;j++){
        print res[j]
    }
}' file.txt



