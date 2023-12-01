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
title_jy = "Inorder-Successor-in-BST(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary search tree and a node p in it, return the in-order
successor of that node in the BST. If the given node has no in-order successor
in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.



图见: https://www.yuque.com/frederick/dtwi9g/boxw8t

Example 1:
Input: root = [2, 1, 3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2.
             Note that both p and the return value is of TreeNode type.

Example 2:
Input: root = [5, 3, 6, 2, 4, null, null, 1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.



Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^5<= Node.val <= 10^5
All Nodes will have unique values.
"""




import sys
from about_TreeNode import *



class Solution:
    """
解法1: 二叉搜索树的中序遍历的结果为有序数组, 求 p 的中序遍历的后继元素即第一个比 p 大
的元素; 遍历二叉搜索树, 记录比 p 大的元素中的最小值;

jy: 该方法中的最终 least_value_greater_than_p 值和 target_node 节点值是相同的, 此处可
以优化为一个变量表示, 直接将 target_node 初始化为 TreeNode(sys.maxsize), 并将代码中后
续的 if 判断中的 least_value_greater_than_p 替换为 target_node.val, 并将其初始化语句和
赋值语句全删除;
    """
    def inorderSuccessor_v1(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        # jy: 记录比 p 大的元素中的最小值
        least_value_greater_than_p = sys.maxsize
        target_node = None
        current = root

        while current:
            # jy: 如果当前节点值比 p.val 大, 且比原有 least_value_greater_than_p 小, 则更新
            #    least_value_greater_than_p 以及 target_node, 并从当前节点的左子树中继续找;
            #    由于左子树节点的值是小于当前节点值的, 故下一轮循环找到的比 p 大的节点会更
            #    接近目标求解节点;
            if p.val < current.val < least_value_greater_than_p:
                target_node = current
                least_value_greater_than_p = current.val
                current = current.left
            elif current.val <= p.val:
                current = current.right

        return target_node


    """
解法2: 对解法 1 稍作修改: 并不需要额外的变量去保存至今比 p 大的最小值, 因为遍历时如果
当前节点的值比 p 大, 则将当前节点作为一个可能的答案, 每次当前节点比 p 大都等价于在缩
小这个可能的答案的范围, 一旦下一个左节点的值比 p 小, 那么上一个节点就是要找的后继节点;
    """
    def inorderSuccessor_v2(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        target_node = None
        current = root

        while current:
            # jy: 如果当前节点比 p 大, 则暂定 target_node 为当前节点, 并从当前节点的左
            #    子树进一步遍历(左子树的节点不会大于当前节点, 如果从左子树中再次找到比
            #    p 大的节点, 则其更接近要找的目标节点, 再次将 target_node 赋予该节点)
            #    不断循环直到当前节点小于或等于 p 节点, 则之前最后一次赋予的 target_node
            #    即为目标节点;
            if current.val > p.val:
                target_node = current
                current = current.left
            elif current.val <= p.val:
                current = current.right

        return target_node


    """
jy: 即结合二叉搜索树的中序遍历思路, 先遍历当前节点左子树, 再遍历当前节点(由于不需要使用
到, 故代码中去除对当前节点值的利用), 最后遍历当前节点的右子树, 直到找到第一个非 None 的
比 p.val 大的节点;
    """
    def inorderSuccessor_jy(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        if root.val > p.val:
            return root

        return inorderSuccessor_jy(root.left, p) or inorderSuccessor_jy(root.right, p)



ls_ = [2, 1, 3]
root = build_binary_tree(ls_)
p = 1
# Output: 2
res = Solution().inorderSuccessor_v1(root, root.left)
print(res.val)

ls_ = [5, 3, 6, 2, 4, None, None, 1]
root = build_binary_tree(ls_)
p = 6
# Output: null
res = Solution().inorderSuccessor_v1(root, root.right)
print(res)


