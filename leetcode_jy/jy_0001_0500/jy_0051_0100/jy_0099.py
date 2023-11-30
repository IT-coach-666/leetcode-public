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
title_jy = "Recover-Binary-Search-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes
of the tree were swapped by mistake. Recover the tree without changing its structure.


Example 1:   https://www.yuque.com/frederick/dtwi9g/rwtw2g
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.


Constraints:
The number of nodes in the tree is in the range [2, 1000].
-2^31 <= Node.val <= 2^31 - 1


Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
"""


from typing import Optional
from about_TreeNode import *


class Solution:
    """
解法1: 首先中序遍历二叉树, 对于正确的二叉搜索树, 其中序遍历的结果应该是有序数组, 遍历数组找到第一
个不有序的节点, 然后向后遍历数组找到该节点应该插入的位置, 交换两个节点的值
    """
    def recoverTree_v1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        # jy: 中序遍历二叉树, 如果是真正的二叉搜索树, 则中序遍历结果是有序的;
        self._inorder(root, nodes)
        # jy: 遍历 nodes 列表;
        for i in range(len(nodes) - 1):
            # jy: 找出错放的位置下标 i (nodes[i] > nodes[i+1] 时, 下标 i 即为错放的位置下标)
            if nodes[i].val <= nodes[i+1].val:
                continue

            # jy: 找出该错放的位置下标 i 应被放置到的位置 j (即 nodes[j] > nodes[i] 的对应下标位置 j);
            #    找到后将 i 和 j 对应的下标位置节点值进行互换; 由于题目中明确原本二叉搜索树中只有一对
            #    节点颠倒错放, 则互换 i 和 j 位置后的结果肯定是符合二叉搜索树的; 由于 i+1 的情况已经判
            #    断过, 此处可以直接 i+2 开始;
            j = i + 2
            # j = i + 1
            while j < len(nodes) and nodes[i].val > nodes[j].val:
                j += 1

            nodes[i].val, nodes[j-1].val = nodes[j-1].val, nodes[i].val

            break


    def _inorder(self, root, nodes):
        if not root:
            return
        self._inorder(root.left, nodes)
        nodes.append(root)
        self._inorder(root.right, nodes)


    """
解法2: 递归判断左右子树是否符合二叉搜索树的性质, 如果根节点的值小于左子树中的最小值, 或根节点的
值大于右子树中的最大值, 则交换两者;

JY: LeetCode 上的执行效率和内存占用均不比解法 1 好;
    """
    def recoverTree_v2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while self._dfs(root, None, None):
            pass

    def _dfs(self, root, min_node, max_node):
        """
        root 代表根节点
        min_node 代表以 root 为根节点的树的所有节点不能小于该节点值(如果节点值存在的话)
        max_node 代表以 root 为根节点的树的所有节点不能大于该节点值(如果节点值存在的话);
        """
        if not root:
            return False
        # jy: 如果根节点的值小于记录的最小节点值(阈值, 不能小于), 或根节点的值大于记录的最
        #    大节点值(阈值, 不能超过), 则交换两者;
        if min_node and root.val < min_node.val:
            root.val, min_node.val = min_node.val, root.val
            return True

        if max_node and root.val > max_node.val:
            root.val, max_node.val = max_node.val, root.val
            return True
        # jy: 递归遍历, 要求根节点的左子树的所有节点不能大于根节点(即 max_node 传入 root 节点)
        #    要求根节点的右子树的所有节点不能小于根节点(即 min_node 传入 root 节点)
        return self._dfs(root.left, min_node, root) or self._dfs(root.right, root, max_node)


ls_ = [1, 3, None, None, 2]
root = build_binary_tree(ls_)
print("before=============: ", serialize(root))
# Output: [3,1,null,null,2]
Solution().recoverTree_v1(root)
print(serialize(root))


ls_ = [3, 1, 4, None, None, 2]
root = build_binary_tree(ls_)
print("before=============: ", serialize(root))
# Output: [2,1,4,null,null,3]
Solution().recoverTree_v2(root)
print(serialize(root))



