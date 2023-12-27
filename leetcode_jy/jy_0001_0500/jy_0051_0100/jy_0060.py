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
title_jy = "Permutation-Sequence(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "排列 | 暴力解法 | 寻找数学规律 | IMP"


"""
The set [1, 2, 3, ..., n] contains a total of `n!` unique permutations.
By listing and labeling all of the permutations in order, we get the 
following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"

Given `n` and `k`, return the k-th permutation sequence.

 
Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Example 3:
Input: n = 3, k = 1
Output: "123"
 

Constraints:
1) 1 <= n <= 9
2) 1 <= k <= n!
"""


class Solution:
    """
解法 1: 以 n = 4, k=14 为例进行讲解

数字 [1, 2, 3, 4] 组成的所有排列:
1 + (permutations of [2, 3, 4])
2 + (permutations of [1, 3, 4])
3 + (permutations of [1, 2, 4])
4 + (permutations of [1, 2, 3])

n 个数字的排列数为 n!, 3 个数字的排列数为 6 (即以上 4 组排列中的每一
组均有 6 个排列结果), 因此第 14 个排列落在:
3 + (permutations of 1, 2, 4)

因为程序中索引从 0 开始, 因此令 k = 14 - 1 = 13, 即找第 13 个排列; 由于:
k // (n-1)! = 13 // (4-1)! = 2
因此第 13 个排列的第一个数字为数列 [1, 2, 3, 4] 中索引为 2 的数字: 3

问题进一步缩小为: 找 [1, 2, 4] 数字排列中的第 k = k % (n-1)! = 13 % (4-1)! = 1 个排列:
1 + (permutations of [2, 4])
2 + (permutations of [1, 4])
4 + (permutations of [1, 2])
2 个数字排列有 2! (即以上 3 组排列中的每一组均有 2 个排列结果), 因此
[1, 2, 4] 数字的所有排列中的第 1 个排列落在:
k // (n-2)! = 1 // (4-2)! = 0
即第 1 个排列的第一个数字落在 [1, 2, 4] 中索引 0 的数字: 1
1 + (permutations of [2, 4])

问题进一步缩小为: 找 [2, 4] 数字排列中的第 k = k % (n-2)! = 1 % (4-2)! = 1 个排列;
2 + (permutations of [4])
4 + (permutations of [2])
1 个数字排列有 1 种, 因此 [2, 4] 数字的所有排列中的第 1 个排列落在:
k = k // (n-3)! = 1 // (4-3)! = 1
即第 1 个排列中的第一个数字落在 [2, 4] 中索引 1 的数字: 4

问题进一步缩小为: 找 [2] 数字排列中的第 k = k % (n-3)! = 1 % (4-3)! = 0 个排列;
2 + (permutations of [])
空数值的排列为空, 因此 [2] 数字的所有排列中的第 0 个排列落在:
k // (n-4)! = 0 / (4-4)! = 0
即第 0 个排列的第一个数字落在 [2] 中索引 0 的数字: 2

因此所求排列为: "3142"
    """
    def getPermutation_v1(self, n: int, k: int) -> str:
        import math
        # jy: 生成数值列表
        ls_num = [str(i) for i in range(1, n+1)]
        res = ""
        k = k-1
        while n > 0:
            n -= 1
            # jy: a = k // n!,  k = k % n!
            a, k = divmod(k, math.factorial(n))
            res += ls_num.pop(a)
        return res


    """
解法 2: 解法 1 的改写
    """
    def getPermutation_v2(self, n: int, k: int) -> str:
        import math

        ls_num = [str(i) for i in range(1, n+1)]
        res = ""
        n -= 1
        while n > -1:
            t = math.factorial(n)
            idx = math.ceil(k / t) - 1
            res += ls_num.pop(idx)
            k %= t
            n -= 1
        return res


    """
解法 3: 暴力解法, 以 n=4, k=4 为例进行思考
    """
    def getPermutation_v3(self, n: int, k: int) -> str:
        # jy: 初始化数值列表
        ls_num = [i for i in range(1, n+1)]
        # jy: 循环调用 permute 共 k-1 次, 以 n=4, k=4 为例, 共需循环 3 次:
        #     第 1 次: ls_num 由 [1, 2, 3, 4] 变为 [1, 2, 4, 3]
        #     第 2 次: ls_num 由 [1, 2, 4, 3] 变为 [1, 3, 2, 4]
        #     第 3 次: ls_num 由 [1, 3, 2, 4] 变为 [1, 3, 4, 2]
        # jy: 为什么是循环 k-1 次? 因为 permute 方法的功能是找出比原排列更
        #     大一级的下一个排列; 如果 k=1, 则为初始化的排列, 无需找下一个
        #     更大一级的, 因此找第 k 个时, 只需调用 permute 方法 k-1 次
        for i in range(k-1):
            #print("round【%s】before: %s" % (i, ls_num))
            self.permute(ls_num)
            #print("round【%s】after: %s" % (i, ls_num))
        return "".join([str(i) for i in ls_num])
    
    def permute(self, ls_num: list) -> None:
        """
        找出比原排列 ls_num 更大一级的下一个排列
        """
        # jy: 倒序遍历 ls_num, 从最后一个位置遍历至第二个位置, 并将当前位置
        #     的数值与前一个位置的数值进行比较, 如果当前位置的数值大于前一个
        #     位置的值, 则从前一位置之后找出一个比其大的数值并相互交换, 并将
        #     当前位置以及之后的数值进行倒序处理 
        for i in range(len(ls_num)-1, 0, -1):
            if ls_num[i] > ls_num[i-1]:
                for j in range(len(ls_num)-1, 0, -1):
                    if ls_num[j] > ls_num[i-1]:
                        ls_num[j], ls_num[i-1] = ls_num[i-1], ls_num[j]
                        ls_num[i:] = ls_num[i:][:: -1]
                        return

    """
解法 4: 基于数学规律
n = 4 时的全排列:
1234 → 1243 → 1324 → 1342 → 1423 → 1432
2134 → 2143 → 2314 → 2341 → 2413 → 2431
3124 → 3142 → 3214 → 3241 → 3412 → 3421
4123 → 4132 → 4213 → 4231 → 4312 → 4321
规律:
1) 前缀 1 出现的次数: (len([1, 2, 3, 4]) - len([1]))! = 3! = 6
2) 前缀 12 出现的次数: (len([1, 2, 3, 4]) - len([1, 2]))! = 2! = 2
   ...
3) 前缀长度为 m 的 n 个数时, 前缀出现的次数为 (n-m)!

比如 k = 9, n = 4:
1) 当前列表为 [1, 2, 3, 4]
2) 全排列前缀为 1 的元素出现 6 次
3) 当前答案的前缀一定为 2, 即 [1, 2, 3, 4][9 // 6]
   a) 剩下 [1, 3, 4]
   b) 当前全排列前缀为 1 的元素出现了 2 次
   c) 当前答案的前缀一定为 3, 即 [1, 3, 4][9 % 6 // 2]
   d) 剩下 [1, 4]
      ...
    """
    def getPermutation_v4(self, n: int, k: int) -> str:
        allFactorial = [1, 1]
        for i in range(2, n+1):
            allFactorial.append(allFactorial[-1] * i)

        s, k, res = list(range(1, n+1)), k-1, ""
        for i in range(len(s)-1, -1, -1):
            res += str(s[k // allFactorial[i]])
            del s[k // allFactorial[i]]
            k %= allFactorial[i]
        return res


    """
解法 5: 同解法 4
    """
    def getPermutation_v5(self, n: int, k: int) -> str:
        from math import factorial
        s, k, res = list(range(1, n+1)), k-1, ""
        for i in range(len(s)-1, -1, -1):
            # jy: 注意, 以下不能分开写
            res, s, k = res + str(s[k // factorial(i)]), s[: k // factorial(i)] + s[k // factorial(i) + 1: ], k % factorial(i)
        return res


    """
解法 6: 逐位确定数字

解析参考: https://www.yuque.com/it-coach/leetcode/hfeetxn2yo9e009o
    """
    def getPermutation_v6(self, n: int, k: int) -> str:
        # jy: 计算阶乘, factor[k] = k!
        nums = [str(i) for i in range(1, n+1)]
        factor = [1, 1]
        for i in range(2, n+1):
            factor.append(factor[-1] * i)

        # jy: 逐次计算每一位的数字
        def dfs(nums, n, k, ans):
            if n == 1:
                return ans + nums[0]
            pos = 1
            # jy: 这里 pos 范围和 k 保持一致, k 也是从 1 开始
            for pos in range(1, n+1):
                if k > factor[n-1] * (pos - 1) and k <= factor[n-1] * pos:
                    break
            ans += nums[pos-1]
            # jy: 注意: nums[0: (pos-1)] + nums[pos:]
            return dfs(nums[0: (pos-1)] + nums[pos:], n-1, k - (pos-1) * factor[n-1], ans)

        ans = ""
        return dfs(nums, n, k, ans)


n = 3
k = 3
res = Solution().getPermutation_v1(n, k)
# jy: "213"
print(res)


n = 4
k = 9
res = Solution().getPermutation_v2(n, k)
# jy: "2314"
print(res)


n = 3
k = 1
res = Solution().getPermutation_v3(n, k)
# jy: "123"
print(res)


n = 4
k = 4
res = Solution().getPermutation_v3(n, k)
# jy: "1342"
print(res)


n = 4
k = 14
res = Solution().getPermutation_v1(n, k)
# jy: "3142"
print(res)


