# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
from typing import List, Dict
# jy: 记录该题的难度系数
type_jy = "M"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Letter-Combinations-of-a-Phone-Number(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归"


"""
Given a string containing digits from 2-9 inclusive, return all possible 
letter combinations that the number could represent. 

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.
letters = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'}


Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


Note: Although the above answer is in lexicographical order, your answer
could be in any order you want.
"""


class Solution:
    """
解法 1: 递归
将每个数字对应的字母存储在字典中, 然后递归调用一个个组合去尝试
    """
    def __init__(self):
        self.letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }


    def letterCombinations_v1(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []
        self._search(digits, '', result)
        return result

    def _search(self, digits: str, combination: str, result: List[str]):
        """
        digits: 数值字符串, 如 "23"
        combination: 当前拼接的字符组合(不区分组合中的字符排序, 如 "ab" 和
                     "ba" 是同一个组合)
        result: 记录最终的结果
        """
        len_c = len(combination)
        # jy: 如果组成的字符数与传入的 digits 的数值字符数相同, 则将其加入目
        #     标结果并结束当前的递归过程
        if len_c == len(digits):
            result.append(combination)
            return

        # jy: 获取当前要组合的数字字符
        letter = digits[len_c]
        # jy: 遍历数字字符对应的字母字符
        for c in self.letters[letter]:
            self._search(digits, combination + c, result)


    """
解法 2: 递归方式的另一种写法
    """
    def letterCombinations_v2(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
                
        def _search_v2(conbination, nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    _search_v2(conbination + letter, nextdigit[1:])

        res = []
        _search_v2('', digits)
        return res


    """
解法 3: 非递归方式写法 (循环)
    """
    def letterCombinations_v3(self, digits: str) -> List[str]:
        if not digits: 
            return []

        phone = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        # jy: 初始化队列, 初始元素值只有一个空字符串
        queue = ['']
        for digit in digits:
            for _ in range(len(queue)):
                # jy: 从队头出队一个元素
                tmp = queue.pop(0)
                # jy: 此处基于 ASCII 码, ord("2") 的值为 50, 而 "2" 对应
                #     phone[0] 的值, 因此基于 phone 取数时, 用 ord(digit)-50
                #     所得数值进行取数; 
                ascii_num = ord(digit)
                # jy: 遍历数值对应的字符, 并与当前子串拼接后入队
                for letter in phone[ascii_num - 50]:
                    queue.append(tmp + letter)
        return queue


digits = "23"
res = Solution().letterCombinations_v1(digits)
print(digits, " === ", len(res), " === ", res)


digits = "2345"
res = Solution().letterCombinations_v1(digits)
print(digits, " === ", len(res), " === ", res)


digits = "23"
res = Solution().letterCombinations_v2(digits)
print(digits, " === ", len(res), " === ", res)

"""
digits = "234589"
res = Solution().letterCombinations_v2(digits)
print(digits, " === ", len(res), " === ", res)
"""

digits = "23"
res = Solution().letterCombinations_v3(digits)
print(digits, " === ", len(res), " === ", res)

