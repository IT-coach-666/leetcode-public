version = "0.0.1"
url_ = "www.yuque.com/it-coach"
project_name = "leetcode_jy"
print("-" * 50)
print("【%s: version-%s】" % (project_name, version))
print("【语雀知识库: %s】" % url_)
print("-" * 50)

"""
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

#=============================================================================
题目类型: 
array_dim_1
array_dim_2
linked_list
string
number

"""

import os
import io


def num_format(num):
    return "{0:0>4}".format(num)


def get_statistic(f_name):
    """
    传入参数:
    f_name: 如 "jy_0001_0500/jy_0001_0050/jy_0001.py"
    """
    split_ = f_name.split("/")
    obj_num = split_[-1].lstrip("jy_").rstrip(".py")

    type_jy, title_jy, q_type, tag_jy = None, None, None, None
    with io.open(f_name) as f_:
        for line in f_:
            if line.startswith("type_jy"):
                type_jy = line.split("=")[-1].strip("\"\' \n")
            if line.startswith("title_jy"):
                tmp_ = line.split("=")[-1].strip().split("(")
                title_jy = tmp_[0].strip("\"\'")
                q_type = "{0:<11}".format(tmp_[1].strip("\"\')"))
            if line.startswith("tag_jy"):
                tag_jy = line.split("=")[-1].strip("\"\' \n")
            if type_jy and title_jy and q_type and tag_jy:
                return [obj_num, type_jy, q_type, title_jy, tag_jy, f_name]
    return []

def generate_dir_file(type_=""):
    """
    创建项目的目录结构和文件

    type_ 参数取值如下:
    "get_statistic": 统计汇总各题目的属性 (难度系数、题目类型)
    "write_prefix": 向空文件中写入公共前缀部分
    整数数值: 返回指定题目的路径
    """
    # jy: 判断 type_ 的有效性
    if type_ in ["get_statistic", "write_prefix"]:
        pass
    elif isinstance(type_, int):
        pass
    else:
        print("ERROR, 传入参数 type_ 不符合要求")
        return


    max_num = 2500
    first_step = 500
    sec_step = 50
    ls_all_info = []
    # jy: 一级目录
    for i in range(0, max_num, first_step):
        # jy: 一级目录名
        dir_name = "jy_%s_%s" % (num_format(i+1), num_format(i + first_step))
        #print(dir_name)
        if not os.path.isdir(dir_name):
            print("创建一级目录: %s" % dir_name)
            os.mkdir(dir_name)

        # jy: 二级目录
        for j in range(i, i + first_step, sec_step):
            if j > max_num:
                break
            # jy: 二级目录名
            sec_dir_name = "%s/jy_%s_%s" % (dir_name, num_format(j+1),
                                            num_format(j + sec_step))
            #print(sec_dir_name) 
            if not os.path.isdir(sec_dir_name):
                print("创建二级目录: %s" % sec_dir_name)
                os.mkdir(sec_dir_name)
            #else:
            #    print("删除已存在的目录: %s" % sec_dir_name)
            #    os.rmdir(sec_dir_name)

            # jy: 三级目录(对应具体文件名)
            for k in range(j, j + sec_step):
                # jy: 文件名
                f_name = "%s/jy_%s.py" % (sec_dir_name, num_format(k+1))
                #print(f_name)
                if not os.path.isfile(f_name):
                    print("创建空文件: %s" % f_name)
                    os.mknod(f_name)
                # jy: 读取文件中的 "type_jy" 和 "title_jy" 变量值
                if type_ == "get_statistic":
                    ls_info = get_statistic(f_name)
                    if ls_info:
                        #print(ls_info)
                        ls_all_info.append(ls_info)
                elif type_ == "write_prefix":
                    add_prefix2file(f_name)
                elif isinstance(type_, int):
                    if k+1 == type_:
                        print(f_name)
                        return
    return ls_all_info


def get_file_bit(f_name):
    """
    获取文件大小, 以 bit 为单位
    """
    return os.stat(f_name).st_size


def add_prefix2file(f_name):
    """
    向文件中写入公共前缀部分
    """
    ls_line = [
        "# jy: 以下的设置使得能正常在当前文件中基",
        "#     于 leetcode_jy 包导入相应模块",
        "import os",
        "import sys",
        "abs_path = os.path.abspath(__file__)",
        'dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")',
        "sys.path.append(dir_project)",
        "from leetcode_jy import *",
        'assert project_name == "leetcode_jy" and project_name == "leetcode_jy" and \\',
        '       url_ == "www.yuque.com/it-coach"',
        "from typing import List, Dict",
        "# jy: 记录该题的难度系数",
        'type_jy = ""',
        "# jy: 记录该题的英文简称以及所属类别",
        'title_jy = "(array_dim_1)"',
        '# jy: 记录不同解法思路的关键词',
        'tag_jy = ""'
    ]
    if get_file_bit(f_name) > 100:
        print("【%s】文件中已有内容, 跳过" % f_name)
        return 

    with io.open(f_name, "w") as f_:
        for line in ls_line:
            f_.write(line + "\n")


def get_undo_num(ls_done_info, start=1, end=None):
    """
    获取未完成的题目

    传入参数:
    ls_done_info: 已完成的题目的相关信息
    """
    if not end:
        end = int(ls_done_info[-1][0])

    ls_done_num = [int(ls_info[0]) for ls_info in ls_done_info]
    ls_done_half = ["%s-UNDO" % int(ls_info[0]) for ls_info in ls_done_info if "UNDO" in ls_info[-1]]
    ls_range_num = [i for i in range(start, end)]

    ls_undo_num = [i for i in ls_range_num if i not in ls_done_num]

    return ls_undo_num + ls_done_half


def get_tag_num(ls_done_info, ls_obj, obj="tag"):
    """
    ls_done_info: 已完成的题目信息
    ls_obj: 目标标签列表或目标题目类型列表
    obj: 可选值为 ["tag", "type", "level"] 中的一个
        "tag": 基于标签进行搜索
        "type": 基于题目类型进行搜索
        "level": 基于难度等级进行搜索
    """
    allow_obj = ["tag", "type", "level"]
    assert obj in allow_obj, "obj 参数值必须为 %s" % allow_obj

    ls_obj_info = []
    for ls_info in ls_done_info:
        if obj == "tag":
            obj_jy = ls_info[4]
        elif obj == "type":
            obj_jy = ls_info[2]
        elif obj == "level":
            obj_jy = ls_info[1]
 
        for obj_ in ls_obj:
            if obj_ in obj_jy:
                ls_obj_info.append(ls_info)
                break
    return ls_obj_info

if __name__ == "__main__":
    # jy: 1) 创建项目目录结构并往空文件中写入公共前缀部分 =============================
    """
    generate_dir_file()
    # 往空文件中写入前缀部分
    generate_dir_file(type_="write_prefix")
    #add_prefix2file("./tmp-jy.py")
    """


    # jy: 2) 打印输出已完成的题目以及相关信息、搜索指定类型/标签/难度等级的题目 =======
    #"""
    # 获取已完成的题目 ------------------------------------------
    ls_all_info = generate_dir_file(type_="get_statistic")
    #print("\n".join([str(ls_info) for ls_info in ls_all_info]))

    # 从已完成的题目中搜索指定标签的题目 ------------------------
    '''
    #ls_obj = ["字典", "双指针"]
    ls_obj = ["动态规划"]
    ls_obj_info = get_tag_num(ls_all_info, ls_obj, obj="tag")
    print("\n".join([str(ls_info) for ls_info in ls_obj_info]))
    '''

    # 从已完成的题目中搜索指定题目类型的题目 --------------------
    '''
    #ls_obj = ["字典", "双指针"]
    ls_obj = ["string"]
    ls_obj_info = get_tag_num(ls_all_info, ls_obj, obj="type")
    print("\n".join([str(ls_info) for ls_info in ls_obj_info]))
    '''

    # 从已完成的题目中搜索指定难度等级的题目 --------------------
    #'''
    #ls_obj = ["字典", "双指针"]
    ls_obj = ["M"]
    ls_obj_info = get_tag_num(ls_all_info, ls_obj, obj="level")
    print("\n".join([str(ls_info) for ls_info in ls_obj_info]))
    #'''
    #"""

    # jy 3) 输出指定范围内的 UNDO 题目 ================================================
    """
    ls_all_info = generate_dir_file(type_="get_statistic")
    #ls_undo_num = get_undo_num(ls_all_info)
    ls_undo_num = get_undo_num(ls_all_info, start=1, end=200)
    print(ls_undo_num)
    """

    # jy: 4) 基于题目号找题目路径
    """
    num_ = 771
    generate_dir_file(type_=num_)
    """

