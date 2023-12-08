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
title_jy = "Word-Break(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.



Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


from typing import List, Set
from collections import deque


class Solution:
    """
解法1(超时): 首先将所有的单词保存在 Set 中, 然后遍历字符串, 如果当前的字符串在 Set 中,
则对剩下的字符串递归调用判断, 否则继续遍历字符串;
    """
    def wordBreak_v1(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        return self._search_v1(s, 0, words)

    def _search_v1(self, s: str, i: int, words: Set[str]) -> bool:
        """
        从字符串 s 的下标 i 开始判断字符串是否能被 words 集合中的单词组成
        """
        # jy: 如果 i 等于 s 的长度, 表明字符串已经遍历完, 终止递归(由于 i 等于
        #    len(s)-1 时即表示字符串已经遍历完, 此处如果会进一步递归调用, 则表
        #    明上一步中的 word 是在 words 中的, 即最后剩余的子串 word 也包含在
        #    words 中, 表明满足要求【trick】);
        if i == len(s):
            return True

        # jy: 不断遍历字符串, 并将遍历的字符组成子串;
        word = ''
        for j in range(i, len(s)):
            word += s[j]
            # jy: 如果子串在 words 词典中, 则递归查找后续未遍历的字符, 判断其是否也
            #    能由 words 集合中的单词组成, 如果可以则返回 True;
            if word in words and self._search_v1(s, j+1, words):
                return True
        return False


    """
解法2: 在解法 1 的基础上进行优化, 使用额外的记忆数组 memo:
1) 初始化为字符串长度的列表, 初始值均为 None
2) memo[i] 为 False 则表 s[i:] (即下标为 i 的字符到结尾)不能拆分成由 words 中的单词组成;
   反之为 True 则表明可由 words 中的单词组成;

JY: 性能较解法 1 大大提升;
    """
    def wordBreak_v2(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        # jy: 新增记忆数组 memo, 长度为字符串 s 的长度(空间换时间)
        memo = [None] * len(s)
        # jy: 将记忆数组 memo 传入递归过程;
        return self._search_v2(s, 0, words, memo)

    def _search_v2(self, s: str, i: int, words: Set[str], memo: List[bool]) -> bool:
        """
        从字符串 s 的下标 i 开始判断字符串是否能被 words 集合中的单词组成
        """
        # jy: 如果 i 等于 s 的长度, 表明字符串已经遍历完, 终止递归(由于 i 等于
        #    len(s)-1 时即表示字符串已经遍历完, 此处如果会进一步递归调用, 则表
        #    明上一步中的 word 是在 words 中的, 即最后剩余的子串 word 也包含在
        #    words 中, 表明满足要求);
        if i == len(s):
            return True
        # jy: 如果 memo[i] 不为 None (则其值为 True 或 False, 当值为 True 时, 表明字符
        #    串 s[i:] 可由 words 集合中的单词组成; 为 False 则表明不能由 words 中的单
        #    词组成), 直接返回 memo[i] 即可;
        if memo[i] is not None:
            return memo[i]
        word = ''
        # jy: i 最初为 0, 即表示遍历整个字符串进行判断,
        for j in range(i, len(s)):
            word += s[j]
            # jy: 如果 s[i:j+1] 对应的字符串能被 words 中的单词组成, 则进一步判断 s[j+1:] 后
            #    的字符串是否能被 words 中的单词组成, 如果递归过程中判断 s[j+1: m] 对应的单
            #    词可以由 words 组成, 则会进一步递归判断 s[m:] 后的字符是否能被 words 中的单
            #    词组成, 如果 s[m:n] 对应的单词能被 words 中的单词组成, 但 s[n:] 不能由 words
            #    中的单词组成, 则此时 memo[n] 为 False (如果 s[m:] 对应的字符不能由 words 中
            #    的单词组成, 则 memo[m] 也会被设置为 False); 此时的 m 或 n 是大于 i/j 的数值,
            #    已经被提前判断, 则后续 for 循环中的 j 变大时, 可能会
            if word in words and self._search_v2(s, j+1, words, memo):
                # jy: 如果以上 if 成立, 表明 s[i: ] (即 s 的下标为 i 之后的字符组成的子串能拆分
                #    成由 words 中的单词构成);
                # jy: 以下的 memo[i] = True 注释掉也不影响结果(也不会超时);
                memo[i] = True
                return True
        # jy: 表明 s[i:] 不能被拆分成由 words 组成的子串(此处的 memo[i] = False 如果去掉, 则相当
        #    于解法 1, 会超时);
        memo[i] = False
        return False


    """
解法3: 动态规划: 记 dp[i] 表示 s 的前 i 个字符(即 s[:i])是否可由字典中的单词组成, dp[0] 表
示空串, 设置为 true; 目标即求解 dp[len(s)], 即 dp[-1];

遍历 dp, 如果 dp[j] 为 true (表示 s[:j], 即 s[0] 到 s[j-1] 组成的子串, 可由字典中的单词组
成), 且 s[j:i] 在 Set 中, 则表示 s 的前 i 个字符可由字典中的单词组成, dp[i] 为 True;
    """
    def wordBreak_v3(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        # jy: dp[i] 表示 s 的前 i 个字符是否可由字典中的单词组成, dp[0] 表示空串;
        #    故需要 len(s)+1 个元素, dp[-1] 即 dp[len(s)], 表示 s[:len(s)] 能否由
        #    words 中的单词组成;
        dp = [False] * (len(s)+1)
        dp[0] = True
        # jy: 循环判断前 i 个字符是否可由字典中的单词组成, 可以的话, dp[i] 为 True;
        #    通过该循环, dp[i] 的值将不断从 i 为 1 更新到 i 为 len(dp)-1 (即 len(s))
        #    最后得到目标值 dp[len(s)], 返回即可;
        for i in range(1, len(dp)):
            for j in range(i):
                # jy: 如果 dp[j] 为 True(表明 s[:j], 即 s 的前 j 个字符能由字典中的
                #    单词组成), 且 s[j:i] 在 words 中, 则 dp[i] 为 True (s 的前 i 个
                #    字符能由字典中的单词组成);
                if dp[j] and s[j:i] in words:
                    #print("dp[%d]_origin: " % i, dp[i])
                    dp[i] = True
                    print("dp[%d]: " % i, dp[i])
                    # jy: 此处的 break 减少不必要的循环步骤, 由于当前循环到 j 即已经知道前 i 个字符能由
                    #    字典中的单词组成, 则不再需要循环判断截止到 j 与 i 之间的位置是否能被字典中的单
                    #    词组成; 因为最开始总是先找到长度最短且在字典中存在的单词, 在此基础上再进一步循
                    #    环判断(跳出内部 for 循环, 直接进行下一步外部 for 循环, 下一个外部 for 循环则将
                    #    从 i+1 开始)【trick】;
                    break
        return dp[-1]



    """
解法4: 同样也可以使用广度优先求解, 使用一个队列保存 s 中可以拆分的位置, 遍历队列;
    """
    def wordBreak_v4(self, s: str, wordDict: List[str]) -> bool:
        # jy: 如果为空字符串, 直接返回 False;
        if not s:
            return False

        # jy: 单词集合
        words = set(wordDict)
        # jy: 初始化一个列表, 长度等同于字符串长度, 用于记录字符串指定位置是否被访问;
        visited = [False for _ in range(len(s))]
        # jy: 初始化一个队列用于记录字符串 s 中在 words 中的单词的末尾下标的下一个下
        #     标值(即新单词的起始下标), 初始值为 s 中的首个新单词的起始下标 0; 如果队
        #     列不为空, 则不断循环左侧出队, 出队元素即新单词的起始下标 start, 找出使
        #     得 s[start, end] 是在 words 中的子串, 并将该 end 值加入到队列中, 供后续
        #     循环查找下一个新子串的 end, 如果能找到某个 s[start, end] 在 words 集合中.
        #     且 end 值等于 s 的长度(表明 end-1 是 s 的最后一个字符下标), 则直接返回 True;
        queue = deque([0])
        while queue:
            # jy: 从队列中出队一个元素 (最开始为字符串的第一个元素)
            start = queue.popleft()
            # jy: 如果该元素没有被访问, 则依次迭代, 将该元素的下一个元素开始到字符末尾当做子串的末尾, 找出
            #    所有 end 使得对应子串 s[start: end] 是在词典中的, 并将该 end 入队(入队后的元素将在下一次
            #    while 循环中出队, 作为新的 start, 因为该 end 之前的元素已经判定可由词典中的单词组成了);
            #    在该过程中, 如果总碰到新的满足要求的 end, 则不断入队(且 end 如果是字符串最后一个字符了, 则
            #    表明字符串能被词典中的词组成); 当没有满足要求的 end 时, 也就不再入队了, 此时每次 while 都
            #    会出队一个元素, 如果直到队列为空还没找到将字符串末尾元素作为 end 的情况, 表明该字符串不能
            #    由字典中的单词组成, 最终返回 False;
            print("start=======", start)
            if not visited[start]:
                for end in range(start + 1, len(s) + 1):
                    # jy: 如果 s[start: end] 子串在词典中, 且 end 已经是字符串末尾了, 则表明字符串能由字典
                    #    中的单词拼接组成;
                    if s[start:end] in words:
                        if end == len(s):
                            return True
                        queue.append(end)

            # jy: visited 逻辑去除后会超时; 以上 start 至 end 的各种可能已经遍历过, 表明以 start 为起始下
            #    标的所有在 words 中的单词中的最后一个字符在 s 字符串中的末尾下标的下一个值(即下一个单词
            #    的 start)均已经被放入到队列中了, 后续如果还碰到以该下标为起点的字符则不需要再次判断, 跳
            #    过即可(由于队列中的下标值并非是严格升序的, 后一个出队的元素可能等于前一个值, 也可能是小
            #    于前一个值的, 故还是有可能碰到当前要判断的 start 之前已经被判断过了的情况);
            # visited[start] = True

        return False



s = "leetcode"
wordDict = ["leet", "code"]
# Output: true
res = Solution().wordBreak_v1(s, wordDict)
print(res)


s = "applepenapple"
wordDict = ["apple", "pen"]
# Output: true
res = Solution().wordBreak_v2(s, wordDict)
print(res)


s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
res = Solution().wordBreak_v3(s, wordDict)
print(res)

res = Solution().wordBreak_v4(s, wordDict)
print(res)


"""
import time
t1 = time.time()
# jy: 解法 4 中 visited[start] 去除会超时的例子(解法 1 中也会超时);
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
s = "aaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# res = Solution().wordBreak_v4(s, wordDict)
res = Solution().wordBreak_v1(s, wordDict)
print(res)
print(time.time() - t1)
"""



