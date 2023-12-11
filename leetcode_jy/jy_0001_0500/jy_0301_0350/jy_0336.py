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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Palindrome-Pairs(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a list of unique words, return all the pairs of the distinct indices (i, j) in
the given list, so that the concatenation of the two words ``words[i] + words[j]`` is
a palindrome.


Example 1:
Input: words = ["abcd", "dcba", "lls", "s", "sssll"]
Output: [[0, 1], [1, 0], [3, 2], [2, 4]]
Explanation: The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

Example 2:
Input: words = ["bat", "tab", "cat"]
Output: [[0,1], [1,0]]
Explanation: The palindromes are ["battab", "tabbat"]

Example 3:
Input: words = ["a", ""]
Output: [[0, 1], [1, 0]]


Constraints:
1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
"""


from typing import List


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.end_of_word = False
        # jy: index 属性用于记录指定单词的最后一个字符对应的 Trie 节点在原单词列表中
        #     的下标位置; 可通过该属性值是否为 -1 判断对应字符是否是单词末尾(即可以替
        #     代 end_of_word 属性)
        self.index = -1

    def insert(self, word: str, index: int) -> None:
        """
        Inserts a word into the trie tree.
        该函数也可以不定义在 Trie 类中, 可以定义在具体使用到 Trie 的类中, 仅仅是调用方式不同;
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.end_of_word = True
        cur.index = index

    def search(self, word: str) -> int:
        """
        Returns if the word is in the trie tree.
        该函数也可以不定义在 Trie 类中, 可以定义在具体使用到 Trie 的类中, 仅仅是调用方式不同;
        """
        cur = self
        for ch in word:
            if ch not in cur.children:
                return -1
            cur = cur.children[ch]
        return cur.index


class Solution:
    """
解法1: Trie 的应用(超时): 基本等同于基于 ``前缀 + 后缀`` 的暴力搜索, 只是搜索过程中换
为在 Trie 树中进行, 时间复杂度没有得到实质性的优化;
对于字符串 a 和 b, 如果 a + b 为回文, 则 a 的前半部分和 b 的后半部分对称,
记 a 为 a1a2 (其中 a1 或 a2 可能为空字符串), b 为 b1b2 (其中 b1 或 b2 可
能为空字符串), 则 a1 == reverse(b2), 而对于 a2 和 b1, 有:
1) a2 为空, b1 为回文
2) a2 为回文, b1 为空
在 a1a2 和 b1b2 中, a1 和 b2 消去了两者的回文部分, 如果 a2 和 b1 都不为空,
则 a + b 无法组成回文(注意, 此逻辑是假设 a1 与 b2 的长度尽可能长的情况下成
立, 比如 "aabb" 和 "bbaa", 此时 a1 为 "aabb", a2 为 "", b1 为 "", b2 为 "bbaa");

对于数组中的每个单词, 记为 a1a2, 如果能找到满足上述条件的另一个单词 b1b2, 则
两个单词相加为回文;

寻找 a1 的回文部分(即 b2)可以使用 Trie 来实现
    """
    def isPalindrome(self, word: str) -> bool:
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    def insert(self, root: Trie, word: str, index: int) -> None:
        """
        Inserts a word into the trie tree.
        """
        cur = root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.end_of_word = True
        cur.index = index

    def search(self, root: Trie, word: str) -> int:
        """
        Returns if the word is in the trie tree.
        """
        cur = root
        for ch in word:
            if ch not in cur.children:
                return -1
            cur = cur.children[ch]
        return cur.index

    def palindromePairs_v1(self, words: List[str]) -> List[List[int]]:
        root = Trie()
        n = len(words)
        for i in range(n):
            word = words[i]
            # self.insert(root, word, i)
            root.insert(word, i)

        res = []
        for i in range(n):
            word = words[i]
            for j in range(len(word)):
                if self.isPalindrome(word[:j + 1]):
                    temp = word[j + 1:]
                    # index = self.search(root, temp[::-1])
                    index = root.search(temp[::-1])
                    if index != i and index != -1:
                        res.append([index, i])
                        if temp == "":
                            res.append([i, index])
                if self.isPalindrome(word[j + 1:]):
                    temp = word[:j + 1]
                    # index = self.search(root, temp[::-1])
                    index = root.search(temp[::-1])
                    if index != i and index != -1:
                        res.append([i, index])
        return res

    """
解法2 (更高效): 核心思想: 基于 ``前缀 + 后缀`` 进行搜索判断(基于字典进行搜索, 明显提升性能);
如果两个字符串 k1, k2 可以组成一个回文字符串(k1k2 或者 k2k1), 会有两种情况:
1) len(k1) == len(k2), 则需要比较 k1 == k2[::-1]
2) len(k1) < len(k2), 如(len(k1) > len(k2) 时同理):
   a) k1=ac, k2=cabb, 可组成 cabbac (k2k1); 因为 k2 的前缀 ca 的反转结果等于 k1, 且后缀 bb 为回文;
   b) k1=ac, k2=bbca, 可组成 acbbca (k1k2); 因为 k2 的前缀 bb 已经是回文, 且后缀 ca 的反转结果为 k1;
以下示例辅助思考:
示例1: k1 = "aabb", k2 = "bbaa"
示例2: k1 = "aabb", k2 = "baa"

即只要单词 word1 的前缀或后缀的反转结果为另一个单词 word2, 则表明 word1 和 word2 能拼接组成回文;
假设单词 word1 的前缀为 tmp1, 后缀为 tmp2 (即 word1 = tmp1 + tmp2, tmp1 和 tmp2 均可为空字符串):
1) 如果 tmp1 的反转结果为 word2, 则 word1 + word2 构成回文;
2) 如果 tmp2 的反转结果为 word2, 则 word2 + word1 构成回文;
    """
    def palindromePairs_v2(self, words: List[str]) -> List[List[int]]:
        res = []
        # jy: 构建一个字典, key 为 words 列表中的单词, value 为单词在列表中的对应下标:
        worddict = {word: i for i, word in enumerate(words)}
        # jy: 逐个遍历单词列表中的单词, 判断是否存在其它单词与该单词构成回文, 存在则加入候选列表;
        for i, word in enumerate(words):
            # jy: 基于单词下标 j 将单词分为前缀 tmp1 和后缀 tmp2, 只要其中一个的反转结果在 words
            #     中, 且另一个为回文, 就表明当前 word 能与某个单词(即 tmp1 或 tmp2 的反转结果)构
            #     成回文;
            for j in range(len(word) + 1):
                tmp1 = word[:j]
                tmp2 = word[j:]
                # jy: 如果前缀 tmp1 的反转结果在单词列表中出现, 且不是 word 自身(因为同一个单词不
                #     能重复使用), 且后缀 tmp2 为回文, 则表明 ``word + tmp1 的反转结果`` 组成回文;
                #     将相应下标添加到结果列表中;
                # jy: 如果 ``j < len(word)`` 约束添加在当前 if 判断中(下一个 if 判断不再需要添加
                #     ``j > 0`` 约束), 则可去除 ``worddict[tmp1[::-1]] != i`` 约束, 因为当 j 小于
                #     word 的长度时, 得到的 tmp1 肯定不是整个 word, 其反转结果也就不可能是 word;
                if tmp1[::-1] in worddict and worddict[tmp1[::-1]] != i and tmp2 == tmp2[::-1]:
                # if j < len(word) and tmp1[::-1] in worddict and tmp2 == tmp2[::-1]:
                    res.append([i, worddict[tmp1[::-1]]])

                # jy: 如果后缀 tmp2 的反转结果在单词列表中出现, 且不是 word 自身, 同时前缀 tmp1 为回
                #     文, 则表明 ``tmp2 的反转结果 + word`` 组成回文, 将相应下标添加到结果列表中;
                # jy: 此处增加 j > 0 判断是为了防止重复, 因为:
                #     1) j = 0 时, tmp1 为 "", tmp2 为 word
                #     2) j = len(word) 时, tmp1 为 word, tmp2 为 ""
                #     这两种 tmp1 和 tmp2 的组合在逻辑判断后得到的结果是一致的, 故两种不能被重复判断到;
                #     为了避免重复, 可以在以下 if 中补充 ``j > 0`` 的约束, 使得 ``j = 0`` 时不会再执行
                #     以下逻辑判断, 因为以上的 if 判断中当 ``j = len(word)`` 的时候会执行, 该指向结果与
                #     当 ``j = 0`` 时也执行以下 if 判断是一样的; 如果以下的 ``j > 0`` 约束去除, 则需要
                #     在以上的 if 判断中补充 ``j < len(word)`` 约束, 使得以上两种情况下不会被重复执行;
                # jy: 如果 ``j > 0`` 约束添加在当前 if 判断中(上一个 if 判断不再需要添加 ``j < len(word)``
                #     约束), 则可去除 ``worddict[tmp2[::-1]] != i`` 约束, 因为当 j 大于 0 时, 得到的 tmp2
                #     肯定不是整个 word, 其反转结果也就不可能是 word;
                if j > 0 and tmp2[::-1] in worddict and tmp1 == tmp1[::-1]:
                # if tmp2[::-1] in worddict and worddict[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:
                    res.append([worddict[tmp2[::-1]], i])
        return res

    """
解法2: 思路同解法 2
    """
    def palindromePairs_v3(self, words: List[str]) -> List[List[int]]:
        def findWord(dict_words, s: str, left: int, right: int) -> int:
            """
            查找单词 s[left: right+1], 不存在则返回 -1;
            """
            return dict_words.get(s[left:right + 1], -1)

        def isPalindrome(s: str, left: int, right: int) -> bool:
            """
            判断 s[left: right+1] 是否为回文;
            """
            return s[left:right + 1] == s[left:right + 1][::-1]

        # jy: 将单词的反转结果以及其位置下标存储到字典中;
        indices = {word[::-1]: i for i, word in enumerate(words)}

        ls_res = list()
        for i, word in enumerate(words):
            m = len(word)
            # jy: j 的取值范围是 0 至 m (单词 word 的长度)
            for j in range(m+1):
                # jy: 判断 word[j: m] (即后缀)是否为回文, 如果是回文, 则进一步判断 word[:j] (即
                #     前缀)是否存在于单词逆序字典中, 如果存在且不为当前单词, 表明可以组成回文;
                if isPalindrome(word, j, m-1):
                    left_id = findWord(indices, word, 0, j-1)
                    if left_id != -1 and left_id != i:
                        ls_res.append([i, left_id])
                # jy: 判断是否满足: 前缀为回文, 后缀存在于单词逆序字典中;
                if j and isPalindrome(word, 0, j-1):
                    right_id = findWord(indices, word, j, m-1)
                    if right_id != -1 and right_id != i:
                        ls_res.append([right_id, i])
        return ls_res

    """
JY: 字符串两两配对, 并判断组合后是否为回文, 时间复杂度为 O(n^2), LeetCode 上超时;
    """
    def palindromePairs_jy(self, words: List[str]) -> List[List[int]]:
        ls_res = []

        def is_palindrome(str_):
            """
            判断字符串 str_ 是否是回文;
            """
            # jy: 可以通过判断字符串反转后是否相同进行判断;
            # return str_ == str_[::-1]

            low, high = 0, len(str_)-1
            while low < high:
                if str_[low] != str_[high]:
                    return False
                low += 1
                high -= 1
            return True

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if is_palindrome(words[i] + words[j]):
                    ls_res.append([i, j])
                if is_palindrome(words[j] + words[i]):
                    ls_res.append([j, i])
        return ls_res


words = ["abcd", "dcba", "lls", "s", "sssll"]
# Output: [[0, 1], [1, 0], [3, 2], [2, 4]]
res = Solution().palindromePairs_v1(words)
print(res)

words = ["abcd", "dcba", "lls", "s", "sssll"]
# Output: [[0, 1], [1, 0], [3, 2], [2, 4]]
res = Solution().palindromePairs_jy(words)
print(res)


words = ["bat", "tab", "cat"]
# Output: [[0,1], [1,0]]
res = Solution().palindromePairs_v1(words)
print(res)


words = ["a", ""]
# Output: [[0, 1], [1, 0]]
res = Solution().palindromePairs_v1(words)
print(res)


