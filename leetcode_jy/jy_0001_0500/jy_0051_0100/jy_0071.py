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
title_jy = "Simplify-Path(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string `path`, which is an absolute path (starting with a slash '/')
to a file or directory in a Unix-style file system, convert it to the 
simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a
double period '..' refers to the directory up a level, and any multiple 
consecutive slashes (i.e. '//') are treated as a single slash '/'. 

For this problem, any other format of periods such as '...' are treated as
file/directory names.

The canonical path should have the following format:
1) The path starts with a single slash '/'.
2) Any two directories are separated by a single slash '/'.
3) The path does not end with a trailing '/'.
4) The path only contains the directories on the path from the root directory
   to the target file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.

 

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root
             level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced
             by a single one.
 

Constraints:
1) 1 <= path.length <= 3000
2) `path` consists of English letters, digits, period '.', slash '/' or '_'.
3) `path` is a valid absolute Unix path.
"""


class Solution:
    """
解法 1: 栈解决,把当前目录压入栈中,遇到..弹出栈顶,最后返回栈中元素.

    """
    def simplifyPath_v1(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for item in path:
            if item == "..":
                if stack : stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)


path = "/home/"
res = Solution().simplifyPath_v1(path)
# jy: "/home"
print(res)


path = "/../"
res = Solution().simplifyPath_v1(path)
# jy: "/"
print(res)


path = "/home//foo/"
res = Solution().simplifyPath_v1(path)
# jy: "/home/foo"
print(res)

