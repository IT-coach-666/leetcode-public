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
title_jy = "Lowest-Common-Ancestor-of-Deepest-Leaves(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:
1) The node of a binary tree is a leaf if and only if it has no children
2) The depth of the root of the tree is 0. if the depth of a node is d, the depth of 
   each of its children is d + 1.
3) The lowest common ancestor of a set S of nodes, is the node A with the largest depth 
   such that every node in S is in the subtree with root A.

Note:This question is the same as 865: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/



Example 1:   https://www.yuque.com/frederick/dtwi9g/dr61ia
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
             The nodes coloured in blue are the deepest leaf-nodes of the tree.
             Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of 
             them is 2, but the depth of nodes 7 and 4 is 3.

Example 2:
Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree, and it's the LCA of itself.

Example 3:
Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest leaf node in the tree is 2, the LCA of one node is itself.



Constraints:
The number of nodes in the tree will be in the range [1, 1000].
0 <= Node.val <= 1000
The values of the nodes in the tree are unique.
"""


from about_TreeNode import *


class Solution:
    """
对左右子树深度优先搜索, 找到左右子树的最近公共祖先和对应树的深度:
1) 如果左右子树返回的深度相同, 则根节点为局部最近公共祖先
2) 如果左子树返回的深度大于右子树, 则以左子树返回的最近公共祖先为先, 反之以右子树返回的最近公共祖先为先;
    """
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self._dfs(root)[1]

    def _dfs(self, root):
        if not root:
            return 0, None
        # jy: 获取左子树的深度和最小公共祖先(lca)
        h1, lca1 = self._dfs(root.left)
        # jy: 获取右子树的深度和最小公共祖先(lca)
        h2, lca2 = self._dfs(root.right)
        # jy: 如果左子树返回的深度大于右子树, 则以左子树返回的最近公共祖先为先;
        if h1 > h2:
            return h1 + 1, lca1
        # jy: 如果右子树返回的深度大于左子树, 则以右子树返回的最近公共祖先为先;
        elif h1 < h2:
            return h2 + 1, lca2
        # jy: 如果左右子树返回的深度相同(h1 == h2), 则根节点为局部最近公共祖先;
        else:
            return h1 + 1, root



ls_ = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
# Output: [2,7,4]
root = build_binary_tree(ls_)
res = Solution().lcaDeepestLeaves(root)
print(serialize(res))


ls_ = [1]
# Output: [1]
root = build_binary_tree(ls_)
res = Solution().lcaDeepestLeaves(root)
print(serialize(res))


ls_ = [0, 1, 3, None, 2]
# Output: [2]
root = build_binary_tree(ls_)
res = Solution().lcaDeepestLeaves(root)
print(serialize(res))



