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
title_jy = "Interleaving-String(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "动态规划 | 递归 + 缓存 | 循环 + 队列"


"""
Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an
interleaving of `s1` and `s2`.

An interleaving (interleave: 插入，夹进) of two strings `s` and `t` is a
configuration where `s` and `t` are divided into `n` and `m` substrings
respectively, such that:
1) s = s1 + s2 + ... + sn
2) t = t1 + t2 + ... + tm
3) |n - m| <= 1
4) The interleaving is (`a + b` is the concatenation of strings `a` and `b`): 
   s1 + t1 + s2 + t2 + s3 + t3 + ... 
   or 
   t1 + s1 + t2 + s2 + t3 + s3 + ...

 
Example 1: 图示参考: https://www.yuque.com/it-coach/leetcode/pgvb5ui8ag9vuzxo
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
1) Split `s1` into: "aa" + "bc" + "c", and `s2` into: "dbbc" + "a"
2) Interleaving the two splits, we get:
   "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac"
3) Since `s3` can be obtained by interleaving `s1` and `s2`, we return true.

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave `s2` with any other
             string to obtain `s3`.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:
1) 0 <= s1.length, s2.length <= 100
2) 0 <= s3.length <= 200
3) `s1`, `s2`, and `s3` consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?
"""


class Solution:
    """
解法 1: 动态规划

dp[i][j] 表示 s1 的前 i 个字符和 s2 的前 j 个字符是否能构成 s3 的前 i+j 个字符

dp[0][0] 一定是 True
    """
    def isInterleave_v1(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        # jy: 如果字符串长度不符合要求, 则直接返回 False
        if(len1 + len2 != len3):
            return False

        # jy: 初始化 dp, 最大可取下标为 dp[len1][len2]
        dp = [[False] * (len2 + 1) for i in range(len1 + 1)]
        dp[0][0] = True

        # jy: 初始化 dp[i][0], 即 s1 的前 i 个字符是否能构成 s3 的前 i 个字符
        for i in range(1, len1 + 1):
            # jy: 当 s1 的前 i-1 个字符能构成 s3 的前 i-1 个字符 (即 dp[i-1][0]
            #     为 True), 且 s1 的第 i 个字符等于 s3 的第 i 个字符时, 表明
            #     s1 的前 i 个字符能构成 s3 的前 i 个字符
            dp[i][0] = (dp[i-1][0] and s1[i-1] == s3[i-1])
 
        # jy: 初始化 dp[0][i], 同理如上
        for i in range(1, len2 + 1):
            dp[0][i] = (dp[0][i-1] and s2[i-1] == s3[i-1])

        # jy: i 和 j 均从 1 开始遍历, 逐步求解 dp[i][j] (从上到下, 从左往右求解)
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # jy: 判断 s1 的前 i 个字符与 s2 的前 j 个字符能否构成 s3 的
                #     前 i+j 个字符:
                #     1) 当 s1 的前 i 个字符与 s2 的前 j-1 个字符可以构成 s3
                #        的前 i+j-1 个字符时, 如果此时 s2 的第 j 个字符与 s3
                #        的第 i+j 个字符相等, 则表明 s1 的前 i 个字符和 s2 的
                #        前 j 个字符可以构成 s3 的前 i+j 个字符
                #     2) 当 s1 的前 i-1 个字符与 s2 的前 j 个字符可以构成 s3
                #        的前 i+j-1 个字符时, 如果此时 s1 的第 i 个字符与 s3
                #        的第 i+j 个字符相等, 则表明 s1 的前 i 个字符和 s2 的
                #        前 j 个字符可以过程 s3 的前 i+j 个字符
                dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or \
                           (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        return dp[-1][-1]


    """
解法 2: 递归 + 缓存
    """
    def isInterleave_v2(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        # jy: 如果字符串长度不符合要求, 则直接返回 False
        if(len1 + len2 != len3):
            return False

        import functools
        @functools.lru_cache(None)
        def helper(i, j, k):
            """
            判断 s1[i:] 能否与 s2[j:] 交错构成 s3[k:]
            """
            # jy: 如果所有下标均到最后一个下标之后了, 表明满足要求 (或
            #     理解为: 两个空字符交错可构成第三个空字符)
            if i == len1 and j == len2 and k == len3:
                return True

            if k < len3:
                # jy: 如果 s1 的第 i 个字符等于 s3 的第 k 个字符, 则判
                #     断 s1[i:] 能否与 s2[j:] 交错构成 s3[k:] 等价于判
                #     断 s[i+1:] 能否与 s2[j:] 交错构成 s3[k+1:]
                if i < len1 and s1[i] == s3[k] and helper(i+1, j, k+1):
                    return True

                # jy: 如果 s2 的第 j 个字符等于 s3 的第 k 个字符, 则判
                #     断 s1[i:] 能否与 s2[j:] 交错构成 s3[k:] 等价于判
                #     断 s[i:] 能否与 s2[j+1:] 交错构成 s3[k+1:]
                if j < len2 and s2[j] == s3[k] and helper(i, j+1, k+1):
                    return True

            return False
        return helper(0, 0, 0)


    """
解法 3: 循环 (基于双向队列)
    """
    def isInterleave_v3(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len1 + len2 != len3:
            return False

        from collections import deque
        queue = deque()
        # jy: 队列中的元组记录下标位置: (s1 的下标位置, s2 的下标位置)
        #     其中 (i, j) 的含义为: s1 的前 i 个元素与 s2 的前 j 个元素
        #     能相互交叉得到 s3 的前 i+j 个元素
        queue.appendleft((0, 0))
        visited = set()
        while queue:
            # jy: 出队一个下标位置 (i, j), 表示 s1 的前 i 个元素与 s2 的
            #     前 j 个元素能相互交叉得到 s3 的前 i+j 个元素
            i, j = queue.pop()

            # jy: 如果已经遍历到 s1 和 s2 的所有元素, 则返回 True
            if i == len1 and j == len2:
                return True

            # jy: 如果 s1 的第 i+1 个元素等于 s3 的第 i+j+1 个元素, 表明
            #     s1 的前 i+1 个元素与 s2 的前 j 个元素能相互交叉得到 s3
            #     的前 i+j+1 个元素, 因此将 (i+1, j) 入队 (左侧或右侧均可)
            if i < len1 and s1[i] == s3[i + j] and (i+1, j) not in visited:
                visited.add((i+1, j))
                #queue.appendleft((i+1, j))
                queue.append((i+1, j))

            # jy: 如果 s2 的第 j+1 个元素等于 s3 的第 i+j+1 个元素, 表明
            #     s1 的前 i 个元素与 s2 的前 j+1 个元素能相互交叉得到 s3
            #     的前 i+j+1 个元素, 因此将 (i, j+1) 入队 (左侧或右侧均可)
            if j < len2 and s2[j] == s3[i + j] and (i, j+1) not in visited:
                visited.add((i, j+1))
                #queue.appendleft((i, j+1))
                queue.append((i, j+1))
        return False



s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
res = Solution().isInterleave_v1(s1, s2, s3)
# jy: true
print(res)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
res = Solution().isInterleave_v2(s1, s2, s3)
# jy: false
print(res)


s1 = ""
s2 = ""
s3 = ""
res = Solution().isInterleave_v3(s1, s2, s3)
# jy: true
print(res)

