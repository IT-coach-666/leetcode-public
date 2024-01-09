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
title_jy = "Unique-Binary-Search-Trees-II(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 相似题: 0096"


"""
Given an integer `n`, return all the structurally unique BST's (binary search
trees), which has exactly `n` nodes of unique values from 1 to `n`. Return the
answer in any order.


Example 1: 图示参考: https://www.yuque.com/it-coach/leetcode/de4wtbwr9dzkhqlx
Input: n = 3
Output: [[1, null, 2, null, 3], [1, null, 3, 2], [2, 1, 3],
         [3, 1, null, null, 2], [3, 2, null, 1]]

Example 2:
Input: n = 1
Output: [[1]]


Constraints:
1 <= n <= 8
"""


from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import serialize


class Solution:
    """
解法 1: 递归

在 0096 (Unique-Binary-Search-Trees) 的思想上, 分别递归求解左右子树的组合
方式, 然后根据左右子树的乘积构造整个树的组合方式
    """
    def generateTrees_v1(self, n: int) -> List[TreeNode]:
        return self._generate_trees(1, n)

    def _generate_trees(self, low, high):
        """
        生成节点值为 low 到 high 的结构不同的所有二叉搜索树

        返回一个列表, 列表中存放所有满足要求的 BST 树的根节点
        """
        # jy: 如果 low 大于 high, 则终止递归; 由于递归函数返回的是所有满足
        #     要求的 BST 树的跟节点, 即返回一个列表, 列表中存放所有 BST 的
        #     根节点, 当 low 大于 high 时, 为空树, 即根节点为空节点, 因此
        #     返回 [None]
        if low > high:
            return [None]

        # jy: ls_tree 列表用于存放每棵有效 BST 树的根节点
        ls_tree = []
        # jy: 从 low 到 high 遍历, 将每次遍历的值 i 当做当前树的根节点
        #     值, 并依据 [low, i-1] 构造所有的左子树 (二叉搜索树), 依据
        #     [i+1, high] 构造所有右子树, 得到存放所有左/右子树的根节点
        #     的列表; 随便遍历列表中的左/右子树的头节点, 基于当前 i 值
        #     构造根节点, 并将左/右子树的根节点赋值给当前根节点
        # jy: 注意, 如果递归调用时传入的 low 等于 high, 表明当前树只有
        #     一个节点, 此时得到的 ls_left_nodes 和 ls_right_nodes 均为
        #     [None], 表示当前根节点的左右子树均只有一种, 为空结果
        for i in range(low, high + 1):
            ls_left_nodes = self._generate_trees(low, i-1)
            ls_right_nodes = self._generate_trees(i+1, high)

            for left in ls_left_nodes:
                for right in ls_right_nodes:
                    # jy: 基于当前 i 值构造树节点 (即根节点), 并为该树节
                    #     点的左子树和右子树赋值, 形成一颗完整的 BST 树并
                    #     加入到结果列表
                    root = TreeNode(i, left, right)
                    ls_tree.append(root)

        return ls_tree


    """
解法 2: 递归改写 (含缓存)
    """
    def generateTrees_v2(self, n: int) -> List[TreeNode]:
        import functools
        @functools.lru_cache(None)
        def dfs(low, high):
            if low > high:
                return [None]

            ls_res = []
            for i in range(low, high + 1):
                for left_node in dfs(low, i - 1):
                    for right_node in dfs(i + 1, high):
                        root = TreeNode(i)
                        root.left, root.right = left_node, right_node
                        ls_res.append(root)
            return ls_res
        return dfs(1, n)



n = 3
res = Solution().generateTrees_v1(n)
for tree_i in res:
    print(serialize(tree_i))
"""
[1, None, 2, None, None, None, 3]
[1, None, 3, None, None, 2]
[2, 1, 3]
[3, 1, None, None, 2]
[3, 2, None, 1]
"""


n = 1
res = Solution().generateTrees_v2(n)
for tree_i in res:
    print(serialize(tree_i))
"""
[[1]]
"""

