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
title_jy = "Add-Bold-Tag-in-String(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
You are given a string ``s`` and an array of strings ``words``. You should add a closed
pair of bold tag <b> and </b> to wrap the substrings in ``s`` that exist in ``words``. If
two such substrings overlap, you should wrap them together with only one pair of closed
bold-tag. If two substrings wrapped by bold tags are consecutive, you should combine them.
Return ``s`` after adding the bold tags.
 

Example 1:
Input: s = "abcxyz123", words = ["abc","123"]
Output: "<b>abc</b>xyz<b>123</b>"

Example 2:
Input: s = "aaabbcc", words = ["aaa","aab","bc"]
Output: "<b>aaabbc</b>c"
 

Constraints:
1 <= s.length <= 1000
0 <= words.length <= 100
1 <= words[i].length <= 1000
s and words[i] consist of English letters and digits.
All the values of words are unique.
 

Note: This question is the same as 758: https://leetcode.com/problems/bold-words-in-string/
"""

import itertools
from typing import List

class Solution:
    """
解法1: 用等长列表 mask 记录需要首末加标签的下标位置(mask 中连续为 True 的下标位置的两边需要加上首末标签)
    """
    def addBoldTag_v1(self, s, words):
        _len = len(s)
        # jy: mask 中连续为 True 的下标位置的两边需要加上首末标签;
        mask = [False] * _len
        for i in range(_len):
            prefix = s[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, min(i + len(word), _len)):
                        mask[j] = True
        # jy-version-1-Begin: 不使用 itertools ---------------------------------------------
        is_prev_false = True
        res_str = ""
        for i in range(len(mask)):
            if mask[i] and is_prev_false:
                is_prev_false = False
                res_str += "<b>" + s[i]
            elif not mask[i] and not is_prev_false:
                res_str += "</b>" + s[i]
                is_prev_false = True
            else:
                res_str += s[i]
        if mask[-1]:
            res_str += "</b>"
        # jy-version-1-End: 不使用 itertools -----------------------------------------------
        # jy-version-2-Begin: 使用 itertools -----------------------------------------------
        '''
        ls_res = []
        # jy: 利用 itertools.groupby 将 zip(s, mask) 基于 mask 进行分组, 得到的 grp 为一个迭代器;
        #     mask_tag 为分组时的键值标签;
        for mask_tag, grp in itertools.groupby(zip(s, mask), lambda z: z[1]):
            if mask_tag:
                ls_res.append("<b>")
            grp_str = "".join(z[0] for z in grp)
            ans.append(grp_str)
            if mask_tag:
                ls_res.append("</b>")
        res_str = "".join(ls_res)
        # jy-version-2-End: 使用 itertools --------------------------------------------------
        '''
        return res_str

    """
解法2: 思路类似解法 1, 但使用下标区间记录需要加首末标签的位置;
    """
    def addBoldTag_v2(self, s: str, words: List[str]) -> str:
        # jy: 起优化作用;
        if not words:
            return s
        # jy: 用以记录需要在两边加标签的位置下标, 元素值 (x, y) 表示需要在 s[x:y] 的左右两边分别加 <b> 和 </b>;
        ls_position = []
        _len = len(s)
        for i in range(_len):
            # jy: 注意, 此处将 s[i:] 赋值给变量 tmp 能大大改善性能(避免了下面 for 循环中不断重复计算);
            tmp = s[i:]
            for word in words:
                # jy: 如果当前单词 word 为 s[i:] 的前缀, 表明需要在 s[i: i + len(word)] 两边加标签, 将其加入到
                #     ls_position 中, 加入时需注意判断当前的下标区间范围是否与原先的区间范围重合, 如果重合, 则
                #     对重合部分进行合并;
                if tmp.startswith(word):
                    # jy: 如果 ls_position 为空, 或者当前下标位置 i 大于上一个区间的末尾下标位置, 则将新下标区
                    #     间加入到 ls_position 中;
                    if not ls_position or i > ls_position[-1][1]:
                        ls_position.append([i, i + len(word)])
                    # jy: 如果以上 if 不成立, 表明 ls_position 不为空, 且 i 小于上一个区间的末尾下标位置, 此时
                    #     表明当前的区间与上一个区间有重合, 需判断是否更新上一个区间的末尾下标位置(如果当前区间
                    #     的末尾下标位置 ``i + len(word)`` 大于上一个区间的末尾下标位置, 则对上一个区间的末尾下
                    #     标位置进行更新)
                    elif i + len(word) > ls_position[-1][1]:
                        ls_position[-1][1] = i + len(word)
        # jy: 倒序遍历 ls_position 中的元组, 使得 s 由后往前更新, 后面添加标签后不影响前面需
        #     要添加标签的位置记录;
        for i in range(len(ls_position) - 1, -1, -1):
            _begin = ls_position[i][0]
            _end = ls_position[i][1]
            s = s[:_begin] + "<b>" + s[_begin: _end] + "</b>" + s[_end:]
        return s

    """
解法3: 思路同解法 2 (记录单词在字符串中的下标区间, 区间去重处理), 但采用了 Trie 树的思路进
行优化, 使得在字符串 s 中查找 words 中的单词的首末下标区间更高效;
    """
    def addBoldTag_v3(self, s: str, words: List[str]) -> str:
        if not words:
            return s

        root = {}
        # jy: 先将 words 中的所有单词 word 加入到 Trie 树中;
        for word in words:
            # jy: 从 Trie 树的根节点将 word 插入;
            p = root
            for c in word:
                if c not in p:
                    p[c] = {}
                p = p[c]
            # jy: 经过以上循环后, p 为 word 的最后一个字符对应的子节点 {}, 在该
            #     子节点中加入 {"$": True} 表示该字符为一个单词的末尾;
            p['$'] = True

        _len = len(s)
        intervals = []
        # jy: 遍历字符串 s 中的每一个字符的下标;
        for i in range(_len):
            # jy: 从字符串 s 的下标为 i 的字符开始判断是否能构成某单词的前缀, 如果不能,
            #     则继续判断 s 字符串的下一个下标位置; 如果能, 则将相应的前缀的首末位置
            #     下标记录到区间列表 intervals 中(记录的过程会对区间进行去重处理);
            p = root
            j = i
            while j < _len and s[j] in p:
                p = p[s[j]]
                # jy: 如果 '$' 在当前节点 p 的子节点中, 表明当前节点 p 对应的字符的下标
                #     j 为止的部分(即 s[i: j+1] 存在于 words 中), 将首末下标位置 [i, j]
                #     添加到区间列表 intervals 中;
                if '$' in p:
                    # jy: 注意, 由于区间列表 intervals 中首末区间的末区间下标是前缀的最后
                    #     一个字符下标, 并非最后一个字符下标的下一个, 故判断是否要新增区间
                    #     时要确保新增区间的起始下标大于上一区间的末尾下标加 1 的结果, 因为
                    #     [1, 3] 和 [4, 6] 其实还是相邻的区间, 依然需要合并连接起来;
                    if not intervals or i > intervals[-1][1] + 1:
                        intervals.append([i, j])
                    elif j > intervals[-1][1]:
                        intervals[-1][1] = j
                j += 1

        # jy: 将 s 转换为字符列表, 随后在需要添加标签的首末下标区间的两侧对应的字符添加标签,
        #     最终将字符(部分已经是包含标签的子串)列表拼接为字符串;
        # jy: 也可以基于解法 2 中的思路对去重后的区间进行加标签;
        chars = list(s)
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            chars[start] = "<b>" + chars[start]
            chars[end] = chars[end] + "</b>"
        return "".join(chars)

    def addBoldTag_2022_03_04(self, s: str, words: List[str]) -> str:
        """
        看了官网解题思路后 code 出的代码
        """
        if not words:
            return s
        ls_position = []
        _len = len(s)
        for i in range(_len):
            for word in words:
                if s[i:].startswith(word):
                    # jy: 以下 if 逻辑比较凌乱, 区间合并思路;
                    if ls_position:
                        if i == ls_position[-1][0]:
                            if len(word) > ls_position[-1][1]:
                                ls_position[-1][1] = i + len(word)
                        else:
                            if i > ls_position[-1][1]:
                                ls_position.append([i, i + len(word)])
                            else:
                                ls_position[-1][1] = max(ls_position[-1][1], i + len(word))
                    else:
                        ls_position.append([i, i + len(word)])

        for i in range(len(ls_position) - 1, -1, -1):
            _begin = ls_position[i][0]
            _end = ls_position[i][1]
            s = s[:_begin] + "<b>" + s[_begin: _end] + "</b>" + s[_end:]
        return s


s = "abcxyz123"
words = ["abc", "123"]
# Output: "<b>abc</b>xyz<b>123</b>"
res = Solution().addBoldTag_v1(s, words)
print(res)


s = "aaabbcc"
words = ["aaa", "aab", "bc"]
# Output: "<b>aaabbc</b>c"
res = Solution().addBoldTag_v2(s, words)
print(res)


s = "aaabbcc"
words = ["aaa", "aab", "bc", "aaabbcc"]
res = Solution().addBoldTag_v3(s, words)
print(res)


s = "aaabbcc"
words = ["a", "b", "c"]
# Output: <b>aaabbcc</b>
res = Solution().addBoldTag_v1(s, words)
print(res)


