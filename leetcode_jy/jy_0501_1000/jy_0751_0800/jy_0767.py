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
title_jy = "Reorganize-String(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string ``s``, rearrange the characters of ``s`` so that any two
adjacent characters are not the same. Return any possible rearrangement
of ``s`` or return "" if not possible.


Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""


Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""


import collections
import heapq


class Solution:
    """
解法1: 计算出每个字符的个数, 将其放入一个大顶堆中; 每次从堆中出堆两个元素,
将其交替排列, 然后将使用的字符数量减 1 后再放回到堆中; 如果堆中最后剩下的
一个元素对应字符的数量大于 1, 说明无法组成满足条件的排列;
    """
    def reorganizeString_v1(self, s: str) -> str:
        counter = collections.Counter(s)
        counts = []
        result = []
        res_str = ""

        for key, count in counter.items():
            # jy: 由于 heapq 默认是小顶堆, 要基于字符的出现次数构造大顶堆, 则
            #     基于其次数的相反数构造小顶堆即可;
            counts.append((-count, key))

        # jy: 对 counts 列表进行堆化;
        heapq.heapify(counts)

        # jy: 如果堆中的元素个数大于 1, 则每次出堆两个元素, 对应出现个数 top-2
        #     的两个字符;
        while len(counts) > 1:
            count1, char1 = heapq.heappop(counts)
            count2, char2 = heapq.heappop(counts)

            result.extend([char1, char2])
            res_str += char1 + char2
            # jy: 由于 count1 和 count2 在堆中是原先数值的相反数, 故对数值加 1
            #     处理, 结果的绝对值即为相应字符使用后仍有的个数;
            count1 += 1
            count2 += 1

            # jy: 如果使用完当前字符后, 仍有字符可用, 则将其重新入堆;
            if count1 < 0:
                heapq.heappush(counts, (count1, char1))
            if count2 < 0:
                heapq.heappush(counts, (count2, char2))

        # jy: 如果最终的堆中仍有一个元素, 则判断该元素对应字符的个数是否为 1 个,
        #     是则可以构成相邻不重复, 否则不能, 返回空字符;
        if counts:
            if -counts[-1][0] == 1:
                result.append(counts[-1][1])
                res_str += counts[-1][1]
            else:
                return ''

        return res_str
        #return ''.join(result)


s = "aab"
# Output: "aba"
res = Solution().reorganizeString_v1(s)
print(res)


s = "aaab"
# Output: ""
res = Solution().reorganizeString_v1(s)
print(res)


