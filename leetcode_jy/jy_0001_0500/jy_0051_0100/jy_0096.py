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
tag_jy = "动态规划 | 递归 + 缓存 IMP | 相似题: 0095"


"""
Given an integer `n`, return the number of structurally unique BST's (binary
search trees) which has exactly `n` nodes of unique values from 1 to `n`.


Example 1: 示例图: https://www.yuque.com/it-coach/leetcode/xdh9rgdd5sxon8ll
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
解法 1: 动态规划

如果二叉搜索树中 k (1 <= k <= n) 为根节点, 则 [1, k-1] 范围内的节点只能作为
左子树, [k+1, n] 范围内的节点只能作为右子树

记 f(a, b) 表示 [a, b] 范围内组成二叉搜索树的个数 (a > b 时不能组成二叉搜索树)
记 g(x) 表示以 x 为根节点的组合个数

则有:  g(x) = f(1, x-1) * f(x+1, n)

所以 [1, n] 为根节点可以构成的 BST 树的个数为: g(1) + ... + g(n)

然而 f(a, b) 这样的函数不方便计算, 如果能转化为只有一个变量就好了 

此题求的是树的个数, 而不是具体树的形式, 而 [1, 4] 组成的树的个数和 [5, 8]
组成的树的个数是相同的, 都是求 4 个数组成树可以有几种组合方式; 因此可以将
f(a, b) 转化为求解值为 1 到 (b - a + 1) 的数能组成的不同形状二叉搜索树的
个数, 从而可以转为动态规划求解

记 dp[i] 表示 i 个数字可以组成不同二叉搜索树的个数, 则 dp[0] 和 dp[1] 都
是 1, dp[n] 的值为:

for i in range(1, n+1):
    # jy: 以 i 为根节点, 则:
    #     dp[i-1] 代表从 1 到 i-1 这 i-1 个数可以组成不同形状二叉搜索树的个数
    #     dp[n-i] 代表从 i+1 到 n 这 n-i 个数可以组成不同形状二叉搜索树的个数
    dp[n] += dp[i-1] * dp[n-i]

但不能一步求解 dp[n-i], 所以在外侧再嵌套一层循环, 让 k 从 2 开始依次遍历值 n,
计算 k 个数组成 BST 树有几种组合方式, 使得后续求解过程中的依赖值随着 k 的遍历
被不断逐一求解


也可以在 0095 (Unique-Binary-Search-Trees-II) 的基础上直接返回结果的长度
    """
    def numTrees_v1(self, n: int) -> int:
        # jy: dp[i] 表示 i 个数字可以组成不同形状二叉搜索树的个数, 
        #     dp[0] 和 dp[1] 都是 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        # jy: dp[0] 和 dp[1] 已知, 目标是求 dp[n], 该值的求解需不断求解 dp[2]
        #     到 dp[n-1], 最后才能算出 dp[n];  故 i 从 2 开始遍历到 n, 不断依
        #     据前面已有的结果计算 dp[i], 最终即可求得 dp[n] 的值
        for k in range(2, n+1):
            for i in range(1, k+1):
                dp[k] += dp[i-1] * dp[k-i]

        return dp[n]


    """
解法 2: 递归 + 缓存 (去除缓存会超时); 时间复杂度为 O(n^2), 空间复杂度
为 O(n), cache 最大为 n
    """
    from functools import cache
    @cache
    def numTrees_v2(self, n: int) -> int:
        """
        求数值 [1, n] 范围内的 n 个数可构建多少个二叉搜索树
        """
        # jy: 1 个数值只能构造 1 个二叉搜索树; 0 个数值也只能构造 1 个二
        #     叉搜索树 (即空树)
        if n <= 1:
            return 1

        ans = 0
        # jy: i 从 1 到 n 逐个遍历, 尝试将 i 值作为根节点, 剩余的值用于
        #     构造左右子树, 求所有的构造方法
        for i in range(1, n+1):
            # jy: 以当前 i 值为根节点, 则左子树的数值范围为 [1, i-1], 共
            #     i-1 个数值; 右子树的数值范围为 [i+1, n], 共 n-i 个数值
            ans += self.numTrees_v2(i-1) * self.numTrees_v2(n - i)
        return ans


    """
解法 3: 数学解法 (卡特兰数)

上面的公式可以通过数学方法进行化简为: f(n) = (4n - 2) / (n + 1) * f(n − 1)
这在数学上称为卡特兰数 (不是做研究的没必要深究怎么得到的, 记住即可)

f(n) 只与 f(n−1) 有关, 所以可以采用滚动数组的方式将空间复杂度降低到 O(1)

注意: 乘法会导致 int 类型溢出, 但又不能先做除法再做乘法 (有舍入误差), 所以
要用 long 类型, 不过答案刚好不超过 int 的范围 (用例最大是 19, 从 20 开始就
超出 int 取值范围了, 不过这种情况一般会对 1e9+7 取余)
    """
    def numTrees_v3(self, n: int) -> int:
        ans = 1
        for i in range(1, n+1):
            ans = ans * (4 * i - 2) // (i+1)
        return ans


    
n = 3
res = Solution().numTrees_v1(n)
# jy: 5
print(res)


n = 1
res = Solution().numTrees_v2(n)
# jy: 1
print(res)


n = 3
res = Solution().numTrees_v3(n)
# jy: 5
print(res)

