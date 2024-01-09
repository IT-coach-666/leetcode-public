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
tag_jy = "二叉树中序遍历 | 递归 IMP2"



"""
You are given the `root` of a binary search tree (BST), where the values 
of exactly two nodes of the tree were swapped by mistake. Recover the tree 
without changing its structure.


Example 1: 图示参考: https://www.yuque.com/it-coach/leetcode/fx1qwgxt1soqsrbi
Input: root = [1, 3, null, null, 2]
Output: [3, 1, null, null, 2]
Explanation: 3 cannot be a left child of 1 because 3 > 1.
             Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3, 1, 4, null, null, 2]
Output: [2, 1, 4, null, null, 3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3.
             Swapping 2 and 3 makes the BST valid.


Constraints:
1) The number of nodes in the tree is in the range [2, 1000].
2) -2^31 <= Node.val <= 2^31 - 1


Follow up: A solution using O(n) space is pretty straight-forward. Could you
devise a constant O(1) space solution?
"""


from typing import Optional
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import inorderTraversal, serialize


class Solution:
    """
解法 1: 基于中序遍历

中序遍历二叉树 (二叉搜索树的中序遍历结果是升序数组), 遍历数组找到第一个
非升序的节点, 然后向后遍历数组找到该节点应插入的位置, 交换两个节点的值
    """
    def recoverTree_v1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ls_res = []
        # jy: 中序遍历二叉树, 如果是真正的二叉搜索树, 则中序遍历结果升序
        #     (注意: ls_res 中存放的元素是树节点, 而非节点值)
        ls_res = self._inorder(root, ls_res)
        for i in range(len(ls_res) - 1):
            # jy: 找出错放的位置下标 i (ls_res[i] > ls_res[i+1] 时, 下标
            #     i 即为错放的位置下标)
            if ls_res[i].val <= ls_res[i+1].val:
                continue

            # jy: 以上找到的下标位置 i 使得 ls_res[i] > ls_res[i+1], 接
            #     下来需找到其错放的位置 j (可从 i+2 位置开始判断), (即:
            #     ls_res[i] > ls_res[j] 的对应下标位置 j); 找到后将 i 和
            #     j 对应的下标位置节点值进行互换 (节点值互换即可达到节点
            #     互换的效果); 题目中明确原本二叉搜索树中只有一对节点颠倒
            #     错放, 因此互换 i 和 j 后的结果即为二叉搜索树
            j = i + 2
            while j < len(ls_res) and ls_res[i].val > ls_res[j].val:
                j += 1

            ls_res[i].val, ls_res[j-1].val = ls_res[j-1].val, ls_res[i].val
            break

    def _inorder(self, root, ls_node):
        if not root:
            return
        self._inorder(root.left, ls_node)
        ls_node.append(root)
        self._inorder(root.right, ls_node)


    """
解法 2: 递归

递归判断左右子树是否符合二叉搜索树的性质, 如果根节点的值小于左子树中的最
小值, 或根节点的值大于右子树中的最大值, 则交换两者
    """
    def recoverTree_v2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while self._dfs(root, None, None):
            pass

    def _dfs(self, root, min_node, max_node):
        """
        root: 根节点
        min_node: 以 root 节点为根节点的树中, 所有节点的值不能小于该节点值
        max_node: 以 root 节点为根节点的树中, 所有节点的值不能大于该节点值
        """
        if not root:
            return False

        # jy: 如果 root 节点的值小于最小节点值, 或大于最大节点值, 则交换两者
        if min_node and root.val < min_node.val:
            root.val, min_node.val = min_node.val, root.val
            return True

        if max_node and root.val > max_node.val:
            root.val, max_node.val = max_node.val, root.val
            return True


        # jy: 递归遍历, 要求根节点的左子树的所有节点不能大于根节点
        #     (即 max_node 传入 root 节点); 根节点的右子树的所有节
        #     点不能小于根节点 (即 min_node 传入 root 节点)
        return self._dfs(root.left, min_node, root) or self._dfs(root.right, root, max_node)


    """
解法 3: 中序遍历 (栈 + 循环/迭代)

该题的难点是找到那两个交换节点, 把它交换过来

二叉树搜索树中序遍历的结果是递增的, 如果中序遍历顺序是 [4, 2, 3, 1], 只要找
到节点 4 和节点 1 交换顺序即可; 有个规律发现这两个节点:
1) 第一个节点是第一个按照中序遍历时前一个节点大于后一个节点时, 取前一个节点
   (此处指节点 4)
2) 第二个节点是在第一个节点找到之后, 后面出现前一个节点大于后一个节点时, 取
   后一个节点 (此处指节点 1)
    """
    def recoverTree_v3(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        firstNode = None
        secondNode = None
        pre = TreeNode(float("-inf"))

        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            
            if not firstNode and pre.val > p.val:
                    firstNode = pre
            if firstNode and pre.val > p.val:
                #print(firstNode.val,pre.val, p.val)
                secondNode = p
            pre = p
            p = p.right
        firstNode.val, secondNode.val = secondNode.val, firstNode.val


    """
解法 4: 

    """
    def recoverTree_v4(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.firstNode = None
        self.secondNode = None
        self.preNode = TreeNode(float("-inf"))

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            if self.firstNode == None and self.preNode.val >= root.val:
                self.firstNode = self.preNode
            if self.firstNode and self.preNode.val >= root.val:
                self.secondNode = root
            self.preNode = root
            in_order(root.right)

        in_order(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val



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

