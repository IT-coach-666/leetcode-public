
"""
该脚本功能:
1) 创建该项目的目录结构
2) 统计汇总各题目的属性(难度系数、题目类型)



# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *

#from leetcode_jy.jy_utils import test_name
#print("============= ", test_name)

"""

import os

def num_format(num):
    return "{0:0>4}".format(num)

def generate_dir_file():
    max_num = 2500
    first_step = 500
    sec_step = 50
    for i in range(0, max_num, first_step):
        dir_name = "jy_%s_%s" % (num_format(i+1), num_format(i + first_step))
        #print(dir_name)
        if not os.path.isdir(dir_name):
            print("创建一级目录: %s" % dir_name)
            os.mkdir(dir_name)

        for j in range(i, i + first_step, sec_step):
            if j > max_num:
                break
            sec_dir_name = "%s/jy_%s_%s" % (dir_name, num_format(j+1),
                                            num_format(j + sec_step))
            #print(sec_dir_name) 
            if not os.path.isdir(sec_dir_name):
                print("创建二级目录: %s" % sec_dir_name)
                os.mkdir(sec_dir_name)
            #else:
            #    print("删除已存在的目录: %s" % sec_dir_name)
            #    os.rmdir(sec_dir_name)
            for k in range(j, j + sec_step):
                f_name = "%s/jy_%s.py" % (sec_dir_name, num_format(k+1))
                #print(f_name)
                if not os.path.isfile(f_name):
                    print("创建空文件: %s" % f_name)
                    os.mknod(f_name)

generate_dir_file()


