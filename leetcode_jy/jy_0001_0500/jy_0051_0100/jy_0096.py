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
title_jy = "Unique-Binary-Search-Trees(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer n, return the number of structurally unique BST's (binary search
trees) which has exactly n nodes of unique values from 1 to n.


Example 1:   https://www.yuque.com/frederick/dtwi9g/gubupy
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1


Constraints:
1 <= n <= 19
"""


class Solution:
    """
取 k (1 <= k <= n) 为根节点时, 根据二叉搜索树的性质, [1, k-1] 范围内的节点只能作为
左子树, [k+1, n] 范围内的节点只能作为右子树;

记 f(a, b) 表示 [a, b] 范围内的组成二叉搜索树的个数(当 a > b 时不能组成二叉搜索树);
记 g(x) 表示以 x 为根节点的组合个数;
则:  g(x) = f(1, x-1) * f(x+1, n), 
所以 [1, n] 为根节点可以构成的树的个数和为: g(1) + ... + g(n)

然而 f(a, b) 这样的函数不方便计算, 如果能转化为只有一个变量就好了; 

因为这道题求的是树的个数, 而不是具体树的形式, 而 [1, 4] 组成的树的个数和 [5, 8] 组
成的树的个数是相同的, 都是求 4 个数组成树可以有几种组合方式; 所以, 可以将 f(a, b) 转
化为求解 (b - a + 1) 个数(值为 1 到 n, 互不相同)能组成的不同形状二叉搜索树的个数, 从
而可以转为动态规划求解;

记 dp[i] 表示 i 个数字可以组成不同形状二叉搜索树的个数, 则 dp[0] 和 dp[1] 都是 1, dp[n] 的值为:

for i in range(1, n+1):
    # jy: 以 i 为根节点, 则 dp[i-1] 代表从 1 到 i-1 这 i-1 个数可以组成不同形状二叉搜索树的个数;
    #    dp[n-i] 代表从 i+1 到 n 这 n-i 个数可以组成不同形状二叉搜索树的个数;
    dp[n] += dp[i-1] * dp[n-i]

但是我们不能一步求解 dp[n-i], 所以从 2 开始依次计算 k 个数组成树有几种组合方式来得到后续的值


JY: 也可以在 095_Unique-Binary-Search-Trees-II.py 的基础上直接返回结果的长度求解(更具体)
    """
    def numTrees(self, n: int) -> int:
        # jy: dp[i] 表示 i 个数字可以组成不同形状二叉搜索树的个数, 则 dp[0] 和 dp[1] 都是 1;
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        # jy: dp[n] 的值为:
        '''
        # jy: 即表示总共有 n 个数, 根节点能有 n 种情况, for 循环遍历 1 到 n 的值, 将每种情况都
        #    视为根节点求其所有可能构成不同形状二叉树搜索树的个数; 当以 i 为根节点后, 左子树的
        #    节点值范围是 [1, i-1], 共 i-1 个值, 则可使用 dp[i-1] 表示 i-1 个值能组成的二叉搜
        #    索树的个数; 同理右子树的节点值范围是 [i+1, n], 共 n-i 个值, 可用 dp[n-i] 表示 n-i 
        #    个值能构成的二叉搜索树的个数; 两者相乘即为以当前 i 值为根节点的所有二叉搜索树的个
        #    数, 而根节点有多个情况, 则每个情况下都相乘后累加, 最终得到的就是以 n 个数(1 到 n)
        #    能构成的所有不同类型的二叉搜索树的个数, 用 dp[n] 表示;
        for i in range(1, n+1):
            dp[n] += dp[i-1] * dp[n-i]
        '''
        # jy: dp[0] 和 dp[1] 已知, 目标是求 dp[n], 该值需要不断求解 dp[2] 到 dp[n-1], 最后才能算
        #    出 dp[n];  故 i 从 2 开始遍历到 n, 不断依据前面已有的结果计算 dp[i], 最终即可求得
        #    dp[n] 的值;
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]

        return dp[n]


n = 3
# Output: 5
res = Solution().numTrees(n)
print(res)


n = 1
# Output: 1
res = Solution().numTrees(n)
print(res)



