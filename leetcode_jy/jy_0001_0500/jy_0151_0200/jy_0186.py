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
title_jy = "Reverse-Words-in-a-String-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an input string, reverse the string word by word. 

Example:
Input:  ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
Output: ["b", "l", "u", "e", " ", "i", "s", " ", "s", "k", "y", " ", "t", "h", "e"]

Note: A word is defined as a sequence of non-space characters. The input string does not
contain leading or trailing spaces. The words are always separated by a single space.

Follow up: Could you do it in-place without allocating extra space?
"""


from typing import List
class Solution:
    """
这道题的输入相比 151_Reverse-Words-in-a-String.py 工整了许多, 首先将整个数组反转, 这样每个单词
已经来到了正确的位置, 只是各个单词还需要单独反转一次; 使用两个指针 start 和 end 来标记单词的首
尾, 遍历数组, 遇到空格时 start 和 end 都加 1, 遇到非空格时 end 加 1, 然后根据 start 和 end 反
转当前的单词;
    """
    def reverseWords(self, s: List[str]) -> None:
        # jy: 先将整个数组(字符串)反转, 这样每个单词已经来到了正确的位置, 只是各个单词还需要单
        #    独反转一次;
        self._reverse(s, 0, len(s) - 1)
        # jy: 记录单词的开头与结尾, 均初始化为 0;
        start, end = 0, 0
        # jy: 遍历数组(字符串)
        while end < len(s):
            # jy: 当开头也为空时, 修改原先初始化的 start 和 end, 都进 1 位;
            while start < len(s) and s[start].isspace():
                start += 1
                end += 1
            # jy: 当下标为 end 的字符不为空时, end 进 1 位, 直到 end 为空(此时 end-1 即为单词的结尾)
            while end < len(s) and not s[end].isspace():
                end += 1
            # jy: 对单词进行反转;
            self._reverse(s, start, end - 1)
            # jy: 将 end 赋值给 start, 进行下一轮循环(此时的 end 对应的是空字符, start 会在下一轮循
            #    环更新为下一个单词的开始对应的下标);
            start = end

    def _reverse(self, s: List[str], low: int, high: int) -> None:
        # jy: 当 low 小于 high 时不断调换, 同时 low 进 1, high 退 1;
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1


s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
res = Solution().reverseWords(s)
print(s)

# Output: ["b", "l", "u", "e", " ", "i", "s", " ", "s", "k", "y", " ", "t", "h", "e"]


