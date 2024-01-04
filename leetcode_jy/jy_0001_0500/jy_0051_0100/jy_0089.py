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
title_jy = "Gray-Code(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "格雷编码 | 递归 | 找规律 | IMP"


"""
An n-bit gray code (格雷编码) sequence is a sequence of 2^n integers where:
1) Every integer is in the inclusive range [0, 2^n - 1],
2) The first integer is 0,
3) An integer appears no more than once in the sequence,
4) The binary representation of every pair of adjacent integers differs by
   exactly one bit, and
5) The binary representation of the first and last integers differs by
   exactly one bit.

Given an integer `n`, return any valid n-bit gray code sequence.


Example 1:
Input: n = 2
Output: [0, 1, 3, 2]
Explanation: The binary representation of [0, 1, 3, 2] is [00, 01, 11, 10].
               - 00 and 01 differ by one bit
               - 01 and 11 differ by one bit
               - 11 and 10 differ by one bit
               - 10 and 00 differ by one bit
             [0, 2, 3, 1] is also a valid gray code sequence, whose binary 
             representation is [00, 10, 11, 01].
               - 00 and 10 differ by one bit
               - 10 and 11 differ by one bit
               - 11 and 01 differ by one bit
               - 01 and 00 differ by one bit

Example 2:
Input: n = 1
Output: [0, 1]
 

Constraints:
1 <= n <= 16
"""

class Solution:
    """
解法 1: 根据格雷码数学公式

数学归纳法证明格雷码公式: G(n) = n ^ (n >> 1)

注意: python 中 ^ 表示异或运算, ** 才表示平方
n >> x: n 的二进制编码右移 x 位, 相当于 n // 2 ** x
n << x: n 的二进制编码左移 x 位, 相当于 n * 2 ** x

用 G(L)(n) 表示长度为 L 的第 n 个格雷码, 0 <= n < 2 ** L  (2 的 L 次方)

以 L = 3 为例 (以下省略了 L):
G(0) = 000 = 0 ==> 0 ^ (0 >> 1) = 0
G(1) = 001 = 1 ==> 1 ^ (1 >> 1) = 1
G(2) = 011 = 3 ==> 2 ^ (2 >> 1) = 3
G(3) = 010 = 2 ==> 3 ^ (3 >> 1) = 2
G(4) = 110 = 6 ==> 4 ^ (4 >> 1) = 6
G(5) = 111 = 7 ==> 5 ^ (5 >> 1) = 7
G(6) = 101 = 5 ==> 6 ^ (6 >> 1) = 5
G(7) = 100 = 4 ==> 7 ^ (7 >> 1) = 4

在推导这个公式之前, 先了解格雷码的一个特点:
1) 当 L = k+1 时, 前 2 ** k 个格雷码和后 2 ** k 个格雷码除最高位外是对称的
2) 前 2 ** k 个格雷码的最高位为 0, 后 2 ** k 个格雷码的最高位为 1

用公式表示即: G(k+1)(x) ^ (1 << k) = G(k+1)(y) 
1) 0 <= x < 2 ** k
   2 ** k <= y < 2 ** (k + 1)
2) ^(1 << k) 操作其实就是最高位变 1, 用 + 取代 ^ 也是一样的效果, 但为了
   后面推导方便还是 ^ 更好
3) x, y 下标对称, 即 x + y = 2 ** (k+1) - 1
   如 L = 3 时, k = 2, x + y = 7, 当 x = 0 时, y = 7, 对应的编码除了最高位
   外的其它位均相同


归纳法推导:
1) 显然, 当 L = 1 时, G(1)(n) = n^(n >> 1) 成立
2) 假设, 当 L = k 时, G(k)(n) = n^(n >> 1) 成立
3) 当 L = k+1 时, 令 x ∈ [0, 2 ** k + 1): 
   a) 当 x ∈ [0, 2 ** k) 时, G(k+1)(x) 的最高位是 0, 所以有:
      G(k+1)(x) = G(k)(x) = x^(x >> 1)
   b) 当 x ∈ [2 ** k, 2 ** k + 1) 时, 坐标 x 与 坐标 (2 ** (k+1) - 1 - x) 对称
      1) 2 ** (k+1) - 1 对应的二进制 k+1 位都为 1, 所以:
         (2 ** (k+1) - 1 - x) === ~x (x 取反)
      2) 因为对称所以 ~x ∈ [0, 2 ** k + 1), 故:
         G(k+1)(~x) = G(k)(~x) = (~x)^(~x >> 1)
      3) 再由前面对称的规律可知: 
         G(k+1)(x) = G(k)(~x)^(1 << k) = (~x)^(~x >> 1)^(1 << k)
      4) 故要证 G(k+1)(x) = x^(x >> 1) 等同于证:
         (~x)^(~x >> 1)^(1 << k) = x^(x >> 1)

      等式转化:
      # 左右两边异或 (x >> 1), a^a = 0, b^0 = b
      (~x)^(~x >> 1)^(1 << k)^(x >> 1) = x^(x >> 1)^(x >> 1)

      # 结合律: a^b^c = a^(b^c)
      (~x)^{(~x >> 1)^(x >> 1)}^(1 << k) = x

      # x 是 k+1 位, 故: (~x ^ x) >> 1 == 2 ** k - 1 
      (~x)^{(~x ^ x) >> 1}^(1 << k) = x

      (~x)^{(2 ** k - 1)^(1 << k)} = x

      # a 异或另一个位数相同, 且每一位为 1 的数, 相当于取反
      (~x) ^ (2 ** (k+1) - 1) = x     

      # 显然成立, 征毕
      x = x             

   c) 综上当 L = k+1 时, 任意 x ∈ [0, 2 ** (k+1)) 时, G(k+1)(x) = x^(x>>1) 成立

4) 由归纳法可知, 对于任意 k ∈ [0，+∞）, G(k)(x) = x^(x >> 1) 成立
    """
    def grayCode_v1(self, n: int) -> List[int]:
        ls_res = []
        # jy: 1 << n 即 2 ** n 
        for i in range(1 << n):
            # jy: 基于格雷编码公式算第 i 个格雷编码, 随后加入结果列表
            ls_res.append(i ^ (i >> 1))
        return ls_res


    """
解法 2: 根据对称 (镜像) 规律

图解参考: https://www.yuque.com/it-coach/leetcode/sqcydxl0sr3y4gqe

设 n 阶格雷码集合为 G(n), 则 n+1 阶格雷码集合 G(n+1) 可以通过以下三步得到:
1) 给 G(n) 阶格雷码每个元素二进制形式前面添加 0, 得到 G'(n)
2) 设 G(n) 集合倒序 (镜像) 为 R(n), 给 R(n) 每个元素二进制形式前面添加 1,
   得到 R'(n)
3) G(n+1) = G'(n) ∪ R'(n), 拼接两个集合即可得到下一阶格雷码

根据以上规律, 可从 0 阶格雷码推导致任何阶格雷码


由于最高位前默认为 0, 因此 G'(n) = G(n), 只需在 ls_res (即 G(n) ) 后添加 R'(n) 即可
计算 R'(n): 执行 head = 1 << i 计算出对应位数, 以给 R(n) 前添加 1 得到对应 R'(n)
倒序遍历 ls_res (即 G(n) ): 依次求得 R'(n) 各元素添加至 ls_res 尾端, 遍历完成后 ls_res 即 G(n+1)


假设 L = k 时, 已经把所有数据放入 ls_res 数组中, 则当 L = k+1 时, 剩下的一半的数据等同于 ls_res 里的数据都在首位补上 1 后逆序放入数组
    """
    def grayCode_v2(self, n: int) -> List[int]:
        ls_res = [0]
        for i in range(n):
            for j in range(len(ls_res) - 1, -1, -1):
                ls_res.append(ls_res[j] ^ (1 << i))
        return ls_res


    """
解法 3: 递归求解
    """
    def grayCode_v3(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]

        left = self.grayCode_v3(n-1)
        right = left.copy()
        right.reverse()
        right = [x + (1 << (n-1)) for x in right]
        return left + right


    """
解法 4: 递归改写
    """
    def grayCode_v4(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        res = []
        def back(now, x):
            if len(now) == n:
                res.append(int(now, 2))
            elif x == 0:
                back(now + '0', 0)
                back(now + '1', 1)
            else:
                back(now + '1', 0)
                back(now + '0', 1)
        
        back('', 0)
        return res


    """
解法 5: 直接排列

以二进制为 0 值的格雷码为第零项, 第一项改变最右边的位元, 第二项改变右起第一
个为 1 的位元的左边位元; 第三、四项方法同第一、二项, 如此反复即可排列出 n 个
位元的格雷码
    """
    def grayCode_v5(self, n: int) -> List[int]:
        num = "0" * n
        res = [0]
        c = 2 ** n
        while len(res) < c:
            if num[-1] == "0":
                num = num[:-1] + "1"
                res.append(int(num, 2))
            else:
                num = num[:-1] + "0"
                res.append(int(num, 2))
            # print(num)

            if len(res) == c:
                break
            idx = num.rfind("1")
            if num[idx - 1] == "0":
                num = num[:idx - 1] + "1" + num[idx:]
            else:
                num = num[:idx - 1] + "0" + num[idx:]
            # print(num)
            res.append(int(num, 2))

        return res


    """
解法 6: 找迭代规律

1) n = 0 时, g(n) = [0]
2) n > 1 时, g(n) = g(n−1) * 2 + reverse(g(n−1) * 2 + 1)
主要是注意到在原有数字的二进制后面 +0 等价于 *2, +1 等价于 *2 + 1
反转第二段再连接是因为这样连接处的两个数字二进制位只相差 1 (原来相同一个加 1 一个加 0)
可以通过例子的二进制表示说明:
g(1) = [0, 1]
g(2) = [00, 10] + reverse([01, 11]) = [00, 10, 11, 01] = [0, 2, 3, 1]
    """
    def grayCode_v6(self, n):
        if n == 0:
            return [0]
        ls_res = [0]
        for i in range(1, n+1):
            ls_res = [2 * k for k in ls_res] + [2 * k + 1 for k in ls_res[::-1]]
        return ls_res


    """
解法 7: 递归 

比如 n = 2 时给他们添加 0, 形成三位的二进制数 4 个: 000 010 110 100, 它们符合
格雷编码的特点, 相邻两个只有一位不同; 添加 1 也是如此: 001 011 111 101

关键是如何把添加 0 和添加 1 之后的 8 个数接起来; 观察到同一个 2 位的 2 进制数
添加 0、添加 1, 可以作为两个相邻的数, 所以想到把 100 和 101 接起来
    """
    def grayCode_v7(self, n: int) -> List[int]:
        def gray(n):
            if n == 0:
                return ["0"]
            if n == 1:
                return ["0", "1"]
            n_1 = gray(n-1)
            n_1_reverse = n_1[::-1]
            return [x + "0" for x in n_1] + [x + "1" for x in n_1_reverse]
        
        return [int(x, 2) for x in gray(n)]



n = 2
res = Solution().grayCode_v1(n)
# jy: [0, 1, 3, 2]
print(res)


n = 1
res = Solution().grayCode_v2(n)
# jy: [0, 1]
print(res)


