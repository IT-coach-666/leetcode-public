# M0017_Letter-Combinations-of-a-Phone-Number.py

"""
Given a string containing digits from 2-9 inclusive, return all possible 
letter combinations that the number could represent. 

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.
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


Note: Although the above answer is in lexicographical order, your answer could 
be in any order you want.
"""

from typing import List, Dict
class Solution:
    """
首先将每个数字对应可能的字母存储在 Map 中, 然后递归调用一个个组合去尝试; 
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
            '9': 'wxyz'}


    def letterCombinations_v1(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []
        # jy: 以下的 self.letters 在后续调用过程中总是不变的, 故后续递归中可以直接
        #    使用 self.letters, 而不需将其作为参数传入;
        #self._search(self.letters, digits, 0, '', result)
        self._search_jy(digits, '', result)
        return result


    # jy: 经典组合用法, 将多个 for 循环改写成递归调用;
    def _search(self, letters: Dict[str, str], digits: str, length: int, combination: str, result: List[str]):
        """
        letters: 一个字典, 存放数值对应的字符映射(递归过程不会改变该值, 可直接去除, 使用 self.letters 即可);
        digits: 一个数值字符串;
        length: 表示当前拼接的字符(combination)的长度, 该参数可被优化掉;
        combination: 当前拼接的字符组合(不区分组合中的字符排序, 如 'ab' 和 'ba' 是同一个组合);
        result: 记录最终的结果;
        """
        # jy: 如果当前拼接的字符串长度已与 digits 相等, 表明已构建出一个符合要求的字符串组合,
        #    将该字符串添加到结果中并返回;
        if length == len(digits):
            result.append(combination)
            return
        # jy: 获取当前长度下的对应数值字符;
        letter = digits[length]
        # jy: 获取该数值字符对应的子串, 并遍历, 将其逐个添加到 combination 字符串中;
        for c in letters[letter]:
            self._search(letters, digits, length + 1, combination + c, result)


    def _search_jy(self, digits: str, combination: str, result: List[str]):
        """
        JY: 将参数 length 优化掉的版本;
        """
        # jy: result 数组会不断添加符合要求的组合, 并 return 以结束递归;
        if len(combination) == len(digits):
            result.append(combination)
            return

        # jy: 获取当前要组合的数字字符;
        letter = digits[len(combination)]
        # jy: 遍历数字字符对应的字母字符;
        for c in self.letters[letter]:
            self._search_jy(digits, combination + c, result)


digits = "23"
res = Solution().letterCombinations_v1(digits)
print(digits, " === ", len(res), " === ", res)


digits = "2345"
res = Solution().letterCombinations_v1(digits)
print(digits, " === ", len(res), " === ", res)


digits = "234589"
res = Solution().letterCombinations_v1(digits)
print(digits, " === ", len(res), " === ", res)


