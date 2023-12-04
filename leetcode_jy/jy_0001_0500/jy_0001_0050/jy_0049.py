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
tag_jy = ""


"""
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
• All inputs will be in lowercase.
• The order of your output does not matter.
"""



import collections
from typing import List
class Solution:
    """
解法1(超时): 使用一个 Map 保存相同的 anagram, 遍历数组的同时遍历 Map, 判断
当前元素应该放在 Map 中的哪个位置, 但会导致此题超时;
    """
    # Time Limit Exceeded!
    def groupAnagrams_v1(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        anagrams = {
            strs[0]: [strs[0]]
        }
        for i in range(1, len(strs)):
            found_ = False
            # jy: 遍历 anagrams 中的 key, 判断 key 和 strs[i] 是否为 anagram;
            #for key, value in anagrams.items():
            for key in anagrams:
                # jy: 判断 key 和 strs[i] 是否是 anagram;
                if self._is_anagram(key, strs[i]):
                    anagrams[key].append(strs[i])
                    found_ = True
                    break  # jy: 补充此项, 减少循环次数;
            if not found_:
                anagrams[strs[i]] = [strs[i]]
        return list(anagrams.values())

    def _is_anagram(self, a: str, b: str) -> bool:
        """
        判断 a 和 b 是否为 anagram;
        """
        chars = collections.Counter(a)
        for c in b:
            if c not in chars:
                return False
            elif chars[c] == 1:
                chars.pop(c)
            else:
                chars[c] -= 1
        return len(chars) == 0


    """
解法2: 解法 1 的耗时在于遍历 Map 查找当前元素的相同 anagram, 由于相同的 anagram 排序
后的值相等, 所以可以将当前元素排序后作为 key 放入 Map, 这样就降低了查找的时间复杂度;
    """
    def groupAnagrams_v2(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        # jy: 遍历字符串列表
        for s in strs:
            # jy: 对字符串进行排序, 并将排序的结果作为字典的 key, 如果 key 相同, 则属于
            #    同一类, 否则在字典中新增该 key;
            key = ''.join(sorted(s))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
        return list(anagrams.values())

    """
解法3: 该方法是类比解法 1 的实现, 效果上多了一些重复的排序操作, 具体还是以解法 2 为主;
    """
    def groupAnagrams_jy(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        anagrams = {
            ''.join(sorted(strs[0])): [strs[0]]
        }
        for i in range(1, len(strs)):
            found_ = False
            # jy: 遍历 anagrams 中的 key, 判断 key 和 strs[i] 是否为 anagram;
            #for key, value in anagrams.items():
            for key in anagrams:
                # jy: 判断 key 和 strs[i] 是否是 anagram;
                if key == ''.join(sorted(strs[i])):
                    anagrams[key].append(strs[i])
                    found_ = True
                    break  # jy: 补充此项, 减少循环次数;
            if not found_:
                anagrams[''.join(sorted(strs[i]))] = [strs[i]]
        return list(anagrams.values())


ls_str = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = Solution().groupAnagrams_v1(ls_str)
print(res)

res = Solution().groupAnagrams_v2(ls_str)
print(res)

res = Solution().groupAnagrams_jy(ls_str)
print(res)


