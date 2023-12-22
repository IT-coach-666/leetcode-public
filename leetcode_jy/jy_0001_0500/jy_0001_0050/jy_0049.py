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
title_jy = "group-anagrams(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "字典解法技巧 | 巧用素数 | IMP"


"""
Given an array of strings, group anagrams (anagram: 相同字母异序词) together.
The order of your output does not matter.


Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[ ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]]


Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


class Solution:
    """
解法 1: 暴力求解 (超时)

使用 Map 保存相同的 anagram, 遍历数组中 word 的同时也遍历 Map, 判断
该 word 应放在 Map 中的哪个 key 下
    """
    def groupAnagrams_v1(self, strs: List[str]) -> List[List[str]]:
        import collections
        if not strs:
            return []

        dict_anagram = {strs[0]: [strs[0]]}

        for word in strs[1:]:
            # jy: 记录当前遍历的 word 是否在 dict_anagram 中有对应的 key 存在
            found_ = False
            # jy: 遍历 dict_anagram 中的 key, 判断 key 和 word 是否为 anagram,
            #     如果是, 则将该 word 加入到指定的 key 的结果中
            for key in dict_anagram:
                if self._is_anagram(key, word):
                    dict_anagram[key].append(word)
                    found_ = True
                    # jy: 如果已经找到一个 key, 则不再需要遍历后续的 key
                    break 
            if not found_:
                dict_anagram[word] = [word]
        return list(dict_anagram.values())

    def _is_anagram(self, a: str, b: str) -> bool:
        """
        判断 a 和 b 是否为 anagram
        """
        # jy: 基于 collections 直接判断
        return collections.Counter(a) == collections.Counter(b)


    """
解法 2: 优化解法 1

解法 1 的耗时主要在遍历 Map 查找当前 word 在哪个 key 下, 由于相同的 anagram
排序后的值相等, 所以可以将当前元素排序后作为 key 放入 Map, 即可降低查找的时
间复杂度
    """
    def groupAnagrams_v2(self, strs: List[str]) -> List[List[str]]:
        dict_anagram = {}
        # jy: 遍历字符串列表
        for word in strs:
            # jy: 对字符串进行排序, 并将排序的结果作为字典的 key, 如果 key 相同, 则属于
            #    同一类, 否则在字典中新增该 key;
            key = ''.join(sorted(word))
            if key in dict_anagram:
                dict_anagram[key].append(word)
            else:
                dict_anagram[key] = [word]
        return list(dict_anagram.values())


    """
解法 3: 基于素数 (无需对 word 进行排序)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # jy: 26 个素数, 对应 26 个英文字母 (不同组合的素数相乘结果必
        #     定不同, 相加可能会相同)
        ls_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47,
                    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        
        dict_anagram = defaultdict(list)
        for word in strs:
            # jy: 将 word 中的每一个英文字符对应的素数相乘, 得到的值作为
            #     dict_anagram 的 key (注意: 不能相加, 否则 ["ac", "d"]
            #     会被分到同一类中, 因为 2+5=7)
            key = 1
            for char in word:
                key *= ls_prime[ord(char) - 97]
            dict_anagram[key].append(word)
        return list(dict_anagram.values())



ls_str = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = Solution().groupAnagrams_v1(ls_str)
print(res)

res = Solution().groupAnagrams_v2(ls_str)
print(res)

res = Solution().groupAnagrams_jy(ls_str)
print(res)


