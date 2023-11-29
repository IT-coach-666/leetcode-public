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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "First-Unique-Character-in-a-String(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""




"""
Given a string ``s``, return the first non-repeating character in it and return its
index. If it does not exist, return -1.


Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1


Constraints:
1 <= s.length <= 10^5
s consists of only lowercase English letters.
"""


from collections import Counter
import collections

 
class Solution:
    """
解法1: 遍历字符串, 使用字典记录每个字符出现的次数及首个字符出现的位置, 然后
遍历 Map, 找到只出现一次的字符中最早出现的位置;

时间复杂度: O(n), n 为字符串长度;
空间复杂度: O(n), 如果字符串中仅包含小写字母, 则空间复杂度中的 n 最大为 26; 可以理解为 O(1);
    """
    def firstUniqChar_v1(self, s: str) -> int:
        occurrences = {}
        # jy: 记录字符出现的次数及首个出现的位置: {字符:  (出现次数, 首次出现位置)}
        for i, c in enumerate(s):
            if c in occurrences:
                occurrences[c] = (occurrences[c][0] + 1, occurrences[c][1])
            else:
                occurrences[c] = (1, i)

        # jy: min_position 记录最早出现的下标位置(由于遍历的是字典, 是无序的, 因此需要额外通过一个变
        #     量记录最早出现的下标位置)
        min_position = -1
        # jy: 遍历字典中的 value, 即: (出现次数, 字符首次出现的位置)
        for occurrence in occurrences.values():
            # jy: 如果出现次数为 1, 则判断其是否出现位置最小的字符(即从出现次数为 1 的字
            #     符中找出最开始出现的字符)
            if occurrence[0] == 1:
                if min_position == -1:
                    min_position = occurrence[1]
                elif min_position > occurrence[1]:
                    min_position = occurrence[1]
        return min_position

    """
解法2: 简化解法 1 (字典中并不需要记录字符出现的位置)
以下解法中使用 collections.Counter 实现相同的功能, 但性能明确提高, 待后续明确 collections
中的相关实现代码逻辑;

时间复杂度: O(n), n 为字符串长度;
空间复杂度: O(n), 如果字符串中仅包含小写字母, 则空间复杂度中的 n 最大为 26; 可以理解为 O(1);
    """
    def firstUniqChar_v2(self, s: str) -> int:
        # jy-version-1-Begin ------------------------
        '''
        c_count = {}
        for c in s:
            if c in c_count:
                c_count[c] += 1
            else:
                c_count[c] = 1
        '''
        # jy-version-1-End --------------------------
        # jy-version-2-Begin ------------------------
        c_count = Counter(s)
        # jy-version-2-End --------------------------

        for idx, c in enumerate(s):
            if c_count[c] == 1:
                return idx
        return -1

    """
解法3: 对解法 1 进行优化: 用字典存储字符串中的字符下标, 如果字符并非第一次出现, 则下标置为
-1, 表示其为不满足条件的字符, 因此字典中的字符对应的有效下标位置均表示只出现过一次的字符的
下标, 循环遍历, 获取其中的最小值即可; (该方法相较于解法 2 的时间复杂度在某些情况下会有改善,
因为解法 2 中遍历的是整个字符串, 而当前解法遍历的是字典中的字符集合, 可极大减少遍历量)

时间复杂度: O(n), n 为字符串长度;
空间复杂度: O(n), 如果字符串中仅包含小写字母, 则空间复杂度中的 n 最大为 26; 可以理解为 O(1);
    """
    def firstUniqChar_v3(self, s: str) -> int:
        position = {}
        n = len(s)
        for i, ch in enumerate(s):
            if ch in position:
                position[ch] = -1
            else:
                position[ch] = i
        first = n
        for pos in position.values():
            if pos != -1 and pos < first:
                first = pos
        if first == n:
            first = -1
        return first

    """
解法4: 可以借助队列找到第一个不重复的字符; 队列具有先进先出的性质, 很适合用来找出第一个满足某个条件的元素;
使用哈希映射, 并且使用一个额外的队列, 按照顺序存储每一个字符以及它们第一次出现的位置; 当对字符串进行遍历时,
如果当前遍历到的字符 c 不在哈希映射中, 就将 c 与它的索引作为一个二元组放入队尾, 否则需要检查队列中的元素是
否都满足只出现一次的要求, 即不断地根据哈希映射中存储的值是否为 −1 选择弹出队首的元素, 直到队首元素只出现一
次或队列为空; 遍历完成后如果队列为空, 说明没有不重复的字符, 返回 −1，否则队首的元素即为第一个不重复的字符,
返回其下标位置;

时间复杂度: O(n), n 为字符串长度;
空间复杂度: O(n), 如果字符串中仅包含小写字母, 则空间复杂度中的 n 最大为 26; 可以理解为 O(1);
    """
    def firstUniqChar_v4(self, s: str) -> int:
        position = {}
        q = collections.deque()
        for i, ch in enumerate(s):
            if ch not in position:
                position[ch] = i
                q.append((s[i], i))
            else:
                position[ch] = -1
                while q and position[q[0][0]] == -1:
                    q.popleft()
        return -1 if not q else q[0][1]

    """
解法5: 基于字符串特性以及 python 中的字符串内置查找算法;

时间复杂度: 外层 for 循环为: O(1), 内部的 str.find 方法复杂度参考: 
    https://stackoverflow.com/questions/26008904/python-cost-of-find-function
空间复杂度: O(1)
    """
    def firstUniqChar_v5(self, s: str) -> int:
        # jy: 先假设最小索引为一个不可能的大数值
        min_unique_char_index = len(s)

        # jy: 已知字符串由小写字母构成, 故可以直接遍历 a 至 z (也可以遍历字符串 s, 但不能确保 26 次遍历能完成)
        for c in "abcdefghijklmnopqrstuvwxyz":
            i = s.find(c)
            # jy: 分别从字符串头和字符串尾查找对应字母的索引, 如果两索引相等, 说明为单一字符;
            #     此处使用了字符串的内置函数, 后续需要了解内置函数的具体逻辑并复现, 避免调用内置函数;
            if i != -1 and i == s.rfind(c):
                # jy: 更新最新的最小索引(由于不能确保是顺序遍历 s 的中字符, 因此需要不断更新最小值)
                min_unique_char_index = min(min_unique_char_index, i)

        # jy: 如果返回值不为初始化时的不可能的下标值, 则返回最小索引值; 否则, 根据题意返回 -1
        return min_unique_char_index if min_unique_char_index != len(s) else -1


s = "leetcode"
# Output: 0
res = Solution().firstUniqChar_v1(s)
print(res)


s = "loveleetcode"
# Output: 2
res = Solution().firstUniqChar_v1(s)
print(res)


s = "aabb"
# Output: -1
res = Solution().firstUniqChar_v2(s)
print(res)







