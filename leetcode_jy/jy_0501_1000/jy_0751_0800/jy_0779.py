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
title_jy = "K-th-Symbol-in-Grammar(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in
every subsequent row, we look at the previous row and replace each occurrence of 0
with 01, and each occurrence of 1 with 10. For example, for n = 3, the 1st row is 0,
the 2nd row is 01, and the 3rd row is 0110.

Given two integer n and k, return the k-th (1-indexed) symbol in the n-th row of a table of n rows.


Example 1:
Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0

Example 2:
Input: n = 2, k = 1
Output: 0
Explanation:
row 1: 0
row 2: 01

Example 3:
Input: n = 2, k = 2
Output: 1
Explanation:
row 1: 0
row 2: 01

Example 4:
Input: n = 3, k = 1
Output: 0
Explanation:
row 1: 0
row 2: 01
row 3: 0110


Constraints:
1 <= n <= 30
1 <= k <= 2^n - 1
"""


class Solution:
    """
解法1(超时): 直观的解法是递归求出第 n 行的值, 然后返回第 k 个字符, 不过会超时;
    """
    def kthGrammar_v1(self, n: int, k: int) -> int:
        # jy: 递归求解第 n 行的值(一个由 "0" 或 "1" 组成的字符串)
        row = self._get_nth_row(n)
        # jy: 返回第 k 个字符(即字符串中下标为 k-1 的字符)
        return int(row[k-1])


    def _get_nth_row(self, n):
        # jy: 如果是第 1 行, 则返回 "0"
        if n == 1:
            return '0'
        # jy: 如果非第首行, 则按指定规则不断递归求解所在行: 以前一行为基准, 将前一行
        #    的 "0" 替换为 "01", 将前一行的 "1" 替换为 "10", 最终结果即为当前行的结果;
        return ''.join(['01' if x == '0' else '10' for x in self._get_nth_row(n-1)])


    """
解法2: 其实并不需要求出完整的第 n 行的值, 对于第 n 行第 k 个数来说, 它可以从 第 n-1 行中推断:
1) 当 k 等于 1 时则返回 0, 当 k 等于 2 时则返回 1, 因为不管第几行第一个数字都是 0, 第二个数字都是 1;
2) 当 k 是奇数时, 第 n 行第 k 个数等于第 n-1 行第 (k+1)/2 个数替换后左边的数
3) 当 k 是偶数时, 第 n 行第 k 个数等于第 n-1 行第 k/2 个数替换后右边的数
    """
    def kthGrammar_v2(self, n: int, k: int) -> int:
        """返回结果只有 1 和 0 两种可能"""
        # jy: 1) 当 k 等于 1 时则返回 0, 当 k 等于 2 时则返回 1, 因为不管第几行第一个数字都是 0,
        #       第二个数字都是 1;
        if k == 1:
            return 0
        elif k == 2:
            return 1

        # jy: 判断 k 是否是奇数(k 与 1 按位与运算为 1, 表明 k 为奇数)
        is_odd = k & 1 == 1
        # jy: 根据 k 的奇偶性, 求出上一行的第 k/2 或 (k+1)/2 个字符
        #    1) 当 k 是奇数时, 第 n 行第 k 个数等于第 n-1 行第 (k+1)/2 个数替换后左边的数
        if is_odd:
            # jy: 当 k 为奇数时, (k+1)/2 虽能整除, 但 python3 中是浮点类型(不能按位与运算),
            #    故还是使用 "//"
            prev = self.kthGrammar_v2(n-1, (k+1) // 2)
            return 1 if prev == 1 else 0
        # jy: 2) 当 k 是偶数时, 第 n 行第 k 个数等于第 n-1 行第 k/2 个数(即以上的 prev)替换后
        #       右边的数(如果 prev 是 1, 替换后(即 10)右边的数是 0; 如果 prev 是 0, 替换后(即
        #       01)右边的数为 1)
        else:
            prev = self.kthGrammar_v2(n-1, k // 2)
            return 0 if prev == 1 else 1

    def kthGrammar_v3(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        # jy: 当 k 是奇数时, 第 n 行第 k 个数等于第 n-1 行第 (k+1)/2 个数替换后左边的数;
        #    即等价于第 n-1 行的第 (k+1)/2 个数对应的数值(因为为 0 时替换后左边的数值也
        #    是 0, 为 1 时替换后左边的数也是 1)
        if k % 2:
            return self.kthGrammar_v3(n-1, (k+1)/2)
        # jy: 当 k 是偶数时, 第 n 行第 k 个数等于第 n-1 行第 k/2 个数替换后右边的数;
        #    即当 n-1 行的第 k/2 个数是 0 时, 替换后右边的数是 1, 当 n-1 行的第 k/2
        #    个数是 1 时, 替换后右边的数是 0; 以下方式使用返回值减 1 后的绝对值均可
        #    得到满足要求的结果;
        else:
            return abs(self.kthGrammar_v3(n-1, k/2) - 1)


n = 1
k = 1
# Output: 0
res = Solution().kthGrammar_v1(n, k)
print(res)

n = 2
k = 1
# Output: 0
res = Solution().kthGrammar_v1(n, k)
print(res)

n = 2
k = 2
# Output: 1
res = Solution().kthGrammar_v2(n, k)
print(res)

n = 3
k = 3
# Output: 1
res = Solution().kthGrammar_v2(n, k)
print(res)


