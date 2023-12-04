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
title_jy = "wildcard-matching(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



'''
Given an input string ``s`` and a pattern ``p``, implement wildcard pattern matching
with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:
``s`` could be empty and contains only lowercase letters a-z.
``p`` could be empty and contains only lowercase letters a-z, and characters like "?" or "*".


Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''


class Solution:
    """
该题与 010_regular-expression-matching.py 类似, 只是匹配规则略有不同;

010_regular-expression-matching.py 中规则:
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
   ("*" 匹配该字符之前的字符 0 次或多次)

本题中的规则(注意, 其中的 "*" 也与 010_regular-expression-matching.py 中的不同):
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
   ("*" 匹配任意 0 个或多个字符)

动态规划; 定义 dp[i][j] = True 表示 s 的前 i 个字符(即 s[:i])和 p 的前 j 个字符(即 s[:j])匹配;
    """
    def isMatch_v1(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m+1)]
        dp[0][0] = True

        for j in range(1, n+1):
            # jy: 如果 p 的第 j 个字符 (即 p[j-1]) 为 "*", 则 s 的前 0 个字符(即空字符)与 p 的前 j
            #     个字符的匹配情况等同于 s 的前 0 个字符(即空字符)与 p 的前 j-1 个字符的匹配情况;
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        # jy: 遍历 s 的第一到最后一个字符(i 代表第 i 个, 对应下标为 i-1 的字符)
        for i in range(1, m+1):
            # jy: 遍历 p 的第一个到最后一个字符(j 代表第 j 个, 对应下标为 j-1 的字符)
            for j in range(1, n+1):
                # jy: 如果 p 的第 j 个字符 (即 p[j-1]) 为 "*", 则以下条件满足其一即可表示 s 的前 i 个
                #     字符与 p 的前 j 个字符匹配:
                #     1) s 的前 i-1 与 p 的前 j 个的匹配(即 dp[i-1][j] 为 True); 因为当 s 的前 i-1 个
                #        字符都与 p 的前 j 个字符匹配了, s 的第 i 个字符也同样可以被 p 的第 j 个字符 "*"
                #        匹配到(因为 "*" 可匹配 0 个或多个任意字符, s 的第 i 个字符肯定可以被其匹配)
                #     2) s 的前 i 个字符与 p 的前 j-1 个字符匹配(即 dp[i][j-1] 为 True); 因为当 s 的前
                #        i 个字符与 p 的前 j-1 个字符匹配了, 且此时 p 的第 j 个字符为 "*", 由于其可以匹
                #        配 0 个字符, 故此时也能确认 s 的前 i 个字符与 p 的前 j 个字符匹配;
                if p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                # jy: 如果 p 的第 j 个字符 (即 p[j-1]) 不为 "*", 则 s 的前 i 个字符与 p 的前 j 个字符只
                #     有同时满足以下两个条件时才算匹配:
                #     1) s 的前 i-1 个字符与 p 的前 j-1 个字符匹配;
                #     2) s 的第 i 个字符与 p 的第 j 个字符相等(即 s[i-1] == p[j-1]), 或者 p 的第 j 个字符
                #        (即 p[j-1]) 为 "?" (此时不管 s 的第 i 个字符是什么, "?" 都可以与之匹配)
                else:
                    dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == '?') and dp[i-1][j-1]
        return dp[m][n]

    """
解法2: 参考  https://leetcode-cn.com/problems/wildcard-matching/solution/yi-ge-qi-pan-kan-dong-dong-tai-gui-hua-dpsi-lu-by-/
    """
    def isMatch_v2(self, s: str, p: str) -> bool:
        if set(p) == {"*"}: return True
        # s横，p纵
        # 土味拼音变量名
        zong = len(p) + 1  # 纵轴长度
        heng = len(s) + 1  # 横轴长度

        table = [[False] * heng for i in range(zong)]
        table[0][0] = True

        if p.startswith("*"):
            table[1] = [True] * heng

        for m in range(1, zong):
            # 是否可以在该行使用 * 的特技
            path = False
            for n in range(1, heng):
                if p[m-1] == "*":
                    if table[m-1][0]:
                        table[m] = [True] * heng
                        # jy: 此处补充 break 优化性能;
                        break
                    # 只要顶上有了 True, 就可以开通 * 接下来的所有道路
                    if table[m-1][n]:
                        path = True
                    if path:
                        table[m][n] = True
                # 先判断字母是否符合
                elif p[m-1] == "?" or p[m-1] == s[n-1]:
                    # 再看左上方格子是不是 T
                    table[m][n] = table[m-1][n-1]

        return table[zong - 1][heng - 1]

    """
解法3: 双指针法, 性能极佳;
因为 '*' 能匹配任意字符 0 至 n 次, 因此我们用 tmp = (i, j) 记录当碰到 "*" 时, 用 "*"
匹配 s 中的字符 n 次 (n 可以为 0) 后, 下一个需要对 s 和 p 进行匹配的位置下标 (tmp[0]
记录 s 的位置下标, tmp[1] 记录 p 的位置下标;
    """
    def isMatch_v3(self, s: str, p: str) -> bool:
        # jy: 双指针, i 和 j 分别指向 s 和 p 的位置, 初始化为第一个位置下标 0;
        i, j = 0, 0
        # jy: flag 记录截止目前为止是否碰到了 "*" 字符
        flag = False
        # jy: tmp 用于记录当 p 中碰到 "*" 时, 用 "*" 匹配 n 次(n 可以为 0) s 中的字符
        #     后, 下一个 s 和 p 要进行匹配的下标位置(tmp[0] 记录 s 的下标, tmp[1] 记录
        #     p 的下标); 此处初始化主要是为了规范变量定义, 注释掉逻辑也正常;
        tmp = (None, None)
        while i < len(s):
            # jy: 1) 优先精确匹配, 如果 s[i] == p[j], 或者 p[j] 为 "?", 则表示截止当
            #        前位置, s[i] 和 p[j] 均能相互匹配, 此时 i 和 j 均进 1;
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            # jy: 2) 如果 s[i] 和 p[j] 不能精确匹配, 则判断是否 p 是否有 "*" 可以与 s[i]
            #        匹配; 当 p 的当前位置 j 对应的字符为 "*" 时, 表示可以与 s[i] 匹配, 先
            #        尝试用 "*" 匹配 0 个字符(即当前 p[j] 对应的 "*" 先不匹配 s[i]), 尝试
            #        让 j 的下一个字符(即 j 加 1) 与 s[i] 匹配, 并记录 flag 为 True;
            elif j < len(p) and p[j] == '*':
                flag = True
                # jy: 如果当前字符 p[j] 为 "*", 则让其优先匹配 0 个 s 中的字符(即当前的 "*"
                #     先不与 s[i] 匹配, 尝试用 p 的后一个位置 (即 j+1) 的字符与 s[i] 进行匹
                #     配, 故 j 加 1, i 保持不变, 并将后续要匹配的位置记录到 tmp 变量;
                j += 1
                tmp = (i, j)
            # jy: 3) 当 "*" 匹配 0 个字符后, 如果 s[i] 和 p[j] 不能匹配, 则再尝试用 "*" 匹
            #        配 s 中的 1 个字符, 则 i 在 tmp[0] 的基础上进 1, j 保持为原来的 tmp[1],
            #        并将 tmp 更新为最新的 (i, j), 即后续需要对该下标对应的字符进行匹配; 如果
            #        "*" 匹配 s 中的 1 个字符后, 还是不能使得后续的 i 和 j 相互匹配, 则继续用
            #        "*" 匹配 s 中的 2 个, 3 个, ... (即 i 不断在原 tmp[0] 基础上进 1) 直到
            #        把 s 中的所有字符都匹配完为止(如果 s 都被匹配完, 而 p 还有剩余字符, 则当
            #        剩余字符中有非 "*" 字符时, 则可说明 s 和 p 不能匹配);
            elif flag:
                i = tmp[0] + 1
                j = tmp[1]
                tmp = (i, j)
            # jy: 4) 当 p 中的字符遍历完, 但 s 中还有剩余时, 会执行到此处, 表明 s 和 p 不能匹配;
            else:
                return False
        # jy: 5) 当 s 中的字符遍历完, 但 p 中还有字符时, 如果 p 中还有非 "*" 字符, 表明 s 和 p 不能匹配;
        while j < len(p):
            if p[j] != '*':
                return False
            j += 1
        return True


s = "aa"
p = "a"
res = Solution().isMatch_v1(s, p)
print(s, " === ", p, " === ", res)

s = "aa"
p = "*"
res = Solution().isMatch_v1(s, p)
print(s, " === ", p, " === ", res)

s = "cb"
p = "?a"
res = Solution().isMatch_v2(s, p)
print(s, " === ", p, " === ", res)

s = "adceb"
p = "*a*b"
res = Solution().isMatch_v3(s, p)
print(s, " === ", p, " === ", res)

s = "acdcb"
p = "a*c?b"
res = Solution().isMatch_v3(s, p)
print(s, " === ", p, " === ", res)



