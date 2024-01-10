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
title_jy = "Construct-Binary-Tree-from-Inorder-and-Postorder-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 相似题: 0105 | IMP2"


"""
Given two integer arrays `inorder` and `postorder` where `inorder` is the
inorder traversal of a binary tree and `postorder` is the postorder traversal
of the same tree, construct and return the binary tree.


Example 1:
    3
   / \
  9  20
    /  \
   15   7
Input: inorder = [9, 3, 15, 20, 7], postorder = [9, 15, 7, 20, 3]
Output: [3, 9, 20, null, null, 15, 7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]


Constraints:
1) 1 <= inorder.length <= 3000
2) postorder.length == inorder.length
3) -3000 <= inorder[i], postorder[i] <= 3000
4) `inorder` and `postorder` consist of unique values.
5) Each value of postorder also appears in inorder.
6) inorder/postorder is guaranteed to be the inorder/postorder traversal of
   the tree.
"""


from typing import List
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import serialize


class Solution:
    """
解法 1: 递归

后序遍历的最后一个元素是树的根节点, 由于题目中明确了节点值不会重复, 因此在中
序遍历中寻找该根节点值, 假设下标位置为 i, 则中序遍历中 i 下标的左侧、右侧分别
为左子树、右子树的中序遍历结果, 根据左子树、右子树的元素个数, 即可在后续遍历
中获取对应的左子树、右子树的后续遍历结果, 因此可递归依据左/右子树的中序遍历结
果和后续遍历结果构造二叉树
    """
    def buildTree_v1(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self._build_tree(inorder, 0, len(inorder) - 1,
                                postorder, 0, len(postorder) - 1)

    def _build_tree(self, inorder, i_start, i_end,
                          postorder, p_start, p_end):
        """
        基于以下中序遍历和后序遍历的下标范围 (两端的边界下标均包含在内) 构
        建二叉树:
        inorder 中的下标范围 [i_start, i_end]
        postorder 中的下标范围 [p_start, p_end]
        """
        # jy: 如果起始下标大于终止下标, 则返回 None, 终止递归
        if i_start > i_end or p_start > p_end:
            return None

        # jy: 后续遍历的最后一个节点即为当前树的根节点
        root_value = postorder[p_end]
        root = TreeNode(root_value)

        # jy: 找出中序遍历中该根节点的下标
        i = -1
        for idx in range(i_start, i_end + 1):
            if inorder[idx] == root_value:
                i = idx
                break

        # jy: 计算当前根节点的左子树的节点数
        left_tree_size = i - i_start
        # jy: 基于以下中序遍历和后续遍历结果 (两端的边界下标均包含在内), 递
        #     归构建左子树:
        #     inorder 中的下标范围 [i_start: i-1]
        #     postorder 中的下标范围 [p_start: p_start + left_tree_size - 1]
        root.left = self._build_tree(inorder, i_start, i - 1,
                                     postorder, p_start, p_start + left_tree_size - 1)
        # jy: 基于以下中序遍历和后续遍历结果 (两端的边界下标均包含在内), 递
        #     归构造右子树:
        #     inorder 中的下标范围 [i + 1: i_end]
        #     postorder 中的下标范围 [p_start + left_tree_size: p_end - 1]
        root.right = self._build_tree(inorder, i + 1, i_end,
                                      postorder, p_start + left_tree_size, p_end - 1)
        return root


    """
解法 2: 递归的另一种写法
    """
    def buildTree_v2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])

        i = inorder.index(postorder[-1])
        root.left = self.buildTree_v2(inorder[: i], postorder[: i])
        root.right = self.buildTree_v2(inorder[i+1: ], postorder[i: -1])

        return root
 

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
res = Solution().buildTree_v1(inorder, postorder)
# jy: [3, 9, 20, None, None, 15, 7]
print(serialize(res))


inorder = [-1]
postorder = [-1]
res = Solution().buildTree_v1(inorder, postorder)
# jy: [-1]
print(serialize(res))


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
res = Solution().buildTree_v2(inorder, postorder)
# jy: [3, 9, 20, None, None, 15, 7]
print(serialize(res))

