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
title_jy = "Decoded-String-at-Index(string)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
An encoded string ``S`` is given.  To find and write the decoded string to a tape, the
encoded string is read one character at a time and the following steps are taken:
1) If the character read is a letter, that letter is written onto the tape.
2) If the character read is a digit (say ``d``), the entire current tape is repeatedly
   written ``d-1`` more times in total.

Now for some encoded string ``S``, and an index ``K``, find and return the K-th letter
(1 indexed) in the decoded string.


Example 1:
Input: S = "leet2code3", K = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
             The 10th letter in the string is "o".

Example 2:
Input: S = "ha22", K = 5
Output: "h"
Explanation: The decoded string is "hahahaha".  The 5th letter is "h".

Example 3:
Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".


Constraints:
2 <= S.length <= 100
S will only contain lowercase letters and digits 2 through 9.
S starts with a letter.
1 <= K <= 10^9
It's guaranteed that K is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 2^63 letters.
"""



class Solution:
    """
解法1(超时): 先解码字符串, 然后返回第 K 个字符;
    """
    def decodeAtIndex_v1(self, S: str, K: int) -> str:
        return self._decode_string(S)[K-1]

    def _decode_string(self, s: str) -> str:
        text = ''

        for i, c in enumerate(s):
            if c.isdigit():
                text *= int(c)
            else:
                text += c

        return text


    """
解法2: 我们并不需要将字符串完全解码;
遍历字符串, 计算至今的字符串解码后的长度, 如果遇到数字且当前字符串长度乘以该数字后
大于 K, 说明第 K 个字符落在当前解码的字符串的某个重复序列中, 记当前解码的字符串的长
度为 L, 则 L * d + m = K, d 为当前的数字减 1, 由于重复序列的存在, 第 K 个字符实际等
同于求当前解码的字符串中的第 m 个字符, 即 m = K mod L;

如 abcd2efg3 要求的 k 是 7, 则我们遍历到 2 时即可退出了, 因为下标 7 所在的字符一定不
在 2 之后; 遍历到数值 2 时, 当前解码的字符串为 abcd, 长度为 4, 而结合当前数值 2 进行
解码后长度将为 8, 要求的是第 7 个字符, 即第 7 个字符在 abcd 的重复序列里, 其位置为 m,
 m = 7 mod 4 = 3, 即为 c;

注意如果 m 等于 0, 则等同于求第 L 个字符, 此时缩小了范围使用递归求解;
    """
    def decodeAtIndex_v2(self, S: str, K: int) -> str:
        total_length = 0
        # jy: 遍历字符串, 计算至今的字符串解码后的长度(total_length);
        for i, c in enumerate(S):
            # jy: 如果当前字符为数值, 则计算当前字符串长度乘以该数值后的结果(即对当前数值之前的
            #    解码结果进一步解码后的结果长度):
            #    1) 如果结果大于 K, 表明第 K 个字符落在当前解码字符串(长度为 total_length 的字
            #       符串, 即对 S[0:i] 的解码结果)的某个重复序列中, K 与 total_length 取余数即为
            #       其最终在 S[0:i] 的解码结果中的位置(注意, 如果余数是 0, 表明是 S[0:i] 解码后
            #       的最后一个位置);
            if c.isdigit():
                if total_length * int(c) >= K:
                    position = total_length if K % total_length == 0 else K % total_length

                    return self.decodeAtIndex_v2(S[0:i], position)

                total_length *= int(c)
            # jy: 如果当前字符非数值, 则 total_length 加 1, 如果 total_length 等于 K, 则直接
            #    返回当前字符即可;
            else:
                total_length += 1
                if total_length == K:
                    return c


    """
解法3: 解法 2 的非递归版本
    """
    def decodeAtIndex_v3(self, S: str, K: int) -> str:
        # jy: 记录截止至当前字符为止, 解码后的长度;
        total_length = 0
        i, length = 0, len(S)
        # jy: 遍历字符串, 计算字符串解码后的长度, 当解码后长度大于等于 K 时, 停止解码(此
        #    时的 S[i] 可能是数字, 也可能是字符, 不能确定);
        while i < length:
            c = S[i]
            total_length = total_length * int(c) if c.isdigit() else total_length + 1
            if K <= total_length:
                # jy: 补充以下 if 逻辑优化: 如果此时的 c 是字符, 且 K 与 total_length 相
                #    等, 则可直接返回(注意: 该逻辑会在后续的 for 循环中实现, 此处其实加
                #    与不加没太大影响; 从代码简化角度, 应去除);
                # if K == total_length and not c.isdigit():
                #     return c
                break
            i += 1
        # jy: 从下标为 i 的位置倒序遍历, 遍历到下标为 0 的字符(即第一个字符)
        for j in range(i, -1, -1):
            c = S[j]
            # jy: 1) 如果当前的 c 为字符, 则先判断当前 K 值与解码 total_length 减 1;
            if c.isdigit():
                # jy: 以下 '//' 可以 换成 '/', 因为遇到数字时必定是整除的;
                total_length //= int(c)
                # jy: K 更新为与当前 total_length 的取余结果(K 如果为 0, 表示是解压后的字符最后
                #    一个字符, 相当于是倒序循环遍历的下一个字符; 如果不为 0, 则表示是后续解压
                #    后的第 K 个字符, 继续解压后求解即可);
                K %= total_length
            else:
                if K == total_length or K == 0:
                    return c

                total_length -= 1


    """
JY: 同解法 3 逻辑;

正向去构造字符串都很好理解, 如何逆向, 当字符串 abcde 重复 6 次时, 寻找索引 24 实际上就
是在寻找索引 24 % 5 = 4 对应的字符;

即: 知道当前长度为多少的字符串是重复的, 就可以对其直接取余, 和其重复几次没有关系; 如果当
前没有字符串是重复的, 直接从前往后数就好了;

我们首先计算出整个字符串的长度, 遇到字母时长度加 1, 遇到数字时长度按其数字翻倍, 最后求出
整个字符串的长度;

然后逆向思维求其 k 对应的原字符串下标; 首先要将原字符串逆序, 理由是字符串中越靠后的数字越
使字符串翻倍变长, 我们从后向前慢慢减少字符个数, 才能知道当前位置真正的下标是多少;

k 取余当前字符串长度为 0 时, 说明当前位置就是我们要求的位置, 比如 abc 去寻找 k=3, 则逆向遍
历 c 时, 此时的长度是 3, k % 3 = 0, 表示当前的 c 就是我们要找的字符, 另要加条件, 当前位置不
是数字;

k 取余当前字符串长度不为 0 时, 说明还没有找到应找的下标, 如果当前字符是字母, 则将当前字符串
长度减 1, 如果是数字, 则将当前字符串长度除以当前数字;

在第一步计算整个字符串长度时, 其实有可能会有冗余, 不必完全求出字符串长度, 如 abcd2efg3 要求
的 k 是 7, 则我们遍历到 2 时即可退出了, 因为下标 7 所在的字符一定不在 2 之后, 但要注意. 退出
时需要记录 2 的位置, 下一步逆序时, 从 2 往前逆序即可;
    """
    def decodeAtIndex_v4(self, S: str, K: int) -> str:
        c = 0
        i = 0
        while i < len(S):
            if S[i].isdigit():
                c *= int(S[i])
            else:
                c += 1
            if c >= K:
                break
            i += 1

        for ch in reversed(S[: i+1]):
            K %= c
            if K == 0 and ch.isalpha():
                return ch
            if ch.isdigit():
                c /= int(ch)
            else:
                c -= 1


S = "leet2code3"
K = 10
# Output: "o"
res = Solution().decodeAtIndex_v1(S, K)
print(res)


S = "ha22"
K = 5
# Output: "h"
res = Solution().decodeAtIndex_v2(S, K)
print(res)


S = "a2345678999999999999999"
K = 1
# Output: "a"
res = Solution().decodeAtIndex_v3(S, K)
print(res)

'''
sum_ = 1
for i in "2345678999999999999999":
    sum_ *= int(i)
print(sum_)
'''

S = "leet2code3"
K = 10
# Output: "o"
res = Solution().decodeAtIndex_v4(S, K)
print(res)


