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
title_jy = "Top-K-Frequent-Words(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a non-empty list of words, return the k most frequent elements. Your answer should be
sorted by frequency from highest to lowest. If two words have the same frequency, then the
word with the lower alphabetical order comes first.


Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
             Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
              with the number of occurrence being 4, 3, 2 and 1 respectively.


Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.


Follow up: Try to solve it in O(n log k) time and O(n) extra space.
"""


import collections
from typing import List
import heapq


# jy: 解法 2 中使用到;
class Word:
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency

    def __lt__(self, other):
        if self.frequency == other.frequency:
            return self.word > other.word

        return self.frequency < other.frequency

print("class Word 测试-Begin")
a = Word("a", 2)
b = Word("b", 2)
c = Word("c", 2)
d = Word("d", 1)
# jy: True, 当次数相同时, 会按字母进行排序, a 比 b 大, 按默认情况下是 "a" 小于 "b" 的, 但
#    由于要使用最小堆实现 Top k 的逻辑, 应该保存 Top k 大的元素, 且题目要求次数相同时, 按
#    字母排序, 即小的字符更应该被保留下来, 因此要确保次数相同时小的字符开头的单词不要被置
#    于堆顶(最小堆的堆顶值为最小值), 因此字符序号小的在比较大小时应该比字符序号大的大;
print(a > b, " ===== ", "a" > "b")
# jy: 会按 Word 类的排序规则由小到大进行排序, 结果为: ['d', 'c', 'b', 'a']
sorted_res = sorted([b, a, c, d])
print([i.word for i in sorted_res])

print("class Word 测试-End\n")

class Solution:
    """
解法1: 和 347_Top-K-Frequent-Elements.py 基本一样, 不同的是: 如果两个单词出现次数相同, 则字母顺序靠前的单词
排在前面, 所以在构建完桶后, 增加一步对桶中的所有元素进行排序; 也正因为增加了一步排序, 使得算法时间复杂度增长到
了 O(nlogn), 不符合 Follow up 中的要求;
    """
    def topKFrequent_v1(self, words: List[str], k: int) -> List[str]:
        # jy: 创建一个桶, 桶下标即为某单词出现的次数, 由于可能所有元素都相同, 因此最大下标
        #    可能是 len(words), 因此创建桶时桶的最大下标要为 len(words);
        bucket = [[] for _ in range(len(words) + 1)]
        # jy: 统计各单词出现的次数, 放入 collections 包中的字典;
        frequencies = collections.Counter(words)
        # jy: 遍历单词, 以及单词出现的次数, 并以出现次数为下标放入相应编号的桶中(这样下标为 0 的
        #    桶总是空的, 其实可以优化: 出现次数为 n 的放入下标为 n-1 的桶中, 这样桶的长度也可以
        #    少一位, 即等于单词列表的长度);
        for word, frequency in frequencies.items():
            bucket[frequency].append(word)
        # jy: 再次对桶中的元素进行排序(如果桶不为空的话), 其实就是按桶中元素字母先后顺序进行排序;
        for w in bucket:
            if w:
                w.sort()
        # jy: 存放前 k 个元素的列表;
        top_k = []
        # jy: 反向遍历桶的编号,
        for i in range(len(words), -1, -1):
            left_size = k - len(top_k)

            if left_size <= 0:
                break
            # jy: 如果该编号(出现次数)的桶存在, 则将其加入到 top_k 列表中, 添加时用 left_size 控制
            #    不要超出 k 个;
            if bucket[i]:
                top_k += bucket[i][:min(len(bucket[i]), left_size)]

        return top_k

    """
解法2: Follow up 中要求算法的时间复杂度为 O(nlogk), Top k 的问题通常也可以使用大顶堆/小顶堆来实现;

首先同样时使用 Map 保存所有单词的出现次数, 遍历 Map, 将单词和其出现次数放入一个小顶堆中;
如果堆的大小超过 k, 则弹出堆顶的元素; 最后依次弹出小顶堆的元素即可;
    """
    def topKFrequent_v2(self, words: List[str], k: int) -> List[str]:
        # jy: 使用 Map 保存所有单词出现的次数;
        frequencies = collections.Counter(words)
        heap = []
        # jy: 遍历单词及其出现的次数, 将其
        for word, frequency in frequencies.items():
            # jy: Word 类实现优先按 frequency 排序(出现次数多的大于出现次数少的, 因此出现次数少的会
            #    被置于堆顶), 如果出现次数相同, 则按单词首字母排序, 如 "a" > "b" (由于小的字符更
            #    应该被保留下来, 因此要确保次数相同时小的字符开头的单词不要被置于堆顶(最小堆的堆顶
            #    值为最小值), 因此字符序号小的在比较大小时应该比字符序号大的大)
            heapq.heappush(heap, Word(word, frequency))
            # jy: 如果堆大小大于 k, 则从堆顶(最小值)出一个元素, 使得每轮循环后堆中都能保存 Top-k 个
            #    元素;
            if len(heap) > k:
                heapq.heappop(heap)

        top_k = []
        # jy: 得到 Top-k 构成的堆后, 不断从堆顶出元素, 放入 top_k 列表中, 因此该列表中的元素是由小到
        #    大排序的, 返回时要倒序返回;
        for _ in range(k):
            top_k.append(heapq.heappop(heap).word)

        return top_k[::-1]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
# Output: ["i", "love"]
res = Solution().topKFrequent_v1(words, k)
print(res)


words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
# Output: ["the", "is", "sunny", "day"]
res = Solution().topKFrequent_v2(words, k)
print(res)


