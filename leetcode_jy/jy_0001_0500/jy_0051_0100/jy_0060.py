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
tag_jy = ""


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
1 <= n <= 9
1 <= k <= n!
"""


class Solution:
    """
解法 1:
n = 4， 参与排列的数字「1， 2， 3， 4」

列出所有的排列

1 + (permutations of 2, 3, 4)

2 + (permutations of 1, 3, 4)

3 + (permutations of 1, 2, 4)

4 + (permutations of 1, 2, 3)

n个数字的排列数为n!,那么3个数的排列数为6。假如k=14，那么第14个排列落在

3 + (permutations of 1, 2, 4)

令k=14-1(减去1是因为程序中索引从0开始), k/(n-1)!= 13/(4-1)! = 2, 在数列「1， 2， 3， 4」中索引为2的数字为3，所以第一个数字为3。

那么问题进一步缩小为「1， 2， 4」数字的排列，求第 k= k%(n-1)!=13%(4-1)=1 个排列：

1 + (permutations of 2, 4)

2 + (permutations of 1, 4)

4 + (permutations of 1, 2)

在这一步中，2个数字排列有2!， 总共有3*2!=6个，我们寻找第一个排列，那么落在

1 + (permutations of 2, 4)

此时 k/(n-2)! = 1/(4-2)! = 0, 即「1， 2， 4」中索引0的数字1。目前我们知道前面两个数字3，1。剩下的数字依次类推。

「2, 4」

k = k % (n-2)! = 1%(4-2)! = 1，第三个数字在「2， 4」中的索引为 k/(n-3)!= 1/(4-3)! = 1，所以第三个数字为4

「2」

k = k % (n-3)! = 1%(4-3)! = 0，第四个数字在「2」中的索引为 k/(n-4)!= 0/(4-4)! = 0，所以第四个数字为2
    """
    def getPermutation_v1(self, n: int, k: int) -> str:
        import math
        tokens = [str(i) for i in range(1, n+1)]
        res = ''
        k = k-1
        while n > 0:
            n -= 1
            a, k = divmod(k, math.factorial(n))
            res += tokens.pop(a)
        return res


n = 3
k = 3
res = Solution().getPermutation_v1(n, k)
# jy: "213"
print(res)


n = 4
k = 9
res = Solution().getPermutation_v1(n, k)
# jy: "2314"
print(res)


n = 3
k = 1
res = Solution().getPermutation_v1(n, k)
# jy: "123"
print(res)




