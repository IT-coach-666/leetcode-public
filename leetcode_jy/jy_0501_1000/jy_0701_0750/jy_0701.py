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
title_jy = "Insert-into-a-Binary-Search-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return
the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the
original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after
insertion. You can return any of them.


Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is: [5, 2, 7, 1, 3, None, None, None, 4]

Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]


Constraints:
The number of nodes in the tree will be in the range [0, 10^4].
-10^8<= Node.val <= 10^8
All the values Node.val are unique.
-10^8<= val <= 10^8
It's guaranteed that val does not exist in the original BST.
"""


from about_TreeNode import *


class Solution:
    """
解法1: 递归求解, 如果当前节点的值小于 val, 则将其插入右子树, 否则插入左子树;
    """
    def insertIntoBST_v1(self, root: TreeNode, val: int) -> TreeNode:
        # jy: 如果当前节点为空, 则用待插入的节点替换当前的空节点即可;;
        if not root:
            return TreeNode(val)
        # jy: 如果待插入的节点值大于当前节点值, 表明需要在当前节点值的右子树中插入, 插入
        #    后的右子树会更新多一个元素, 且插入该方法会将该右子节点返回, 就如同最外层方
        #    法会返回第一个 root 根节点一样; 此时当前节点的右子节点(即右子树)直接指向插
        #    入后返回的节点, 即完成了相应值的插入(如果右子节点为空, 则插入后会返回插入后
        #    的节点, 则相当于当前节点的右子节点重新赋值为了新插入的节点);
        if root.val < val:
            root.right = self.insertIntoBST_v1(root.right, val)
        # jy: 如果待插入的节点值小于当前节点值, 则表明应该在左子树中插入, 逻辑类似于右子树
        #    中的插入逻辑;
        else:
            root.left = self.insertIntoBST_v1(root.left, val)

        return root

    """
解法2: 非递归版本;
    """
    def insertIntoBST_v2(self, root: TreeNode, val: int) -> TreeNode:
        # jy: 如果当前树为空, 则插入一个节点后该节点即为根节点, 直接返回即可;
        if not root:
            return TreeNode(val)
        # jy: 设置当前节点为根节点, prev 保留前一个节点, 初始值为 None;
        prev, current = None, root
        # jy: 如果当前节点不为空, 则不断循环遍历其子节点(依据 val 值判断是左子节点还
        #    是右子节点), 并用 prev 保留其上一个节点(即下一轮 current 的父节点)
        while current:
            # jy: 将前一个节点设置为当前节点
            prev = current
            # jy: 如果待插入的值大于当前节点值, 则应该在当前节点的右子树中插入, 将当
            #    前节点更新为其右子节点;
            if current.val < val:
                current = current.right
            # jy: 如果待插入的值小于当前节点, 则应该在左子树中插入, 将当前节点更新为
            #    左子节点;
            else:
                current = current.left
        # jy: 经过以上循环后, current 为 None, prev 保留了 current 的父节点(即 val 值对
        #    应的节点可插入到 prev 节点的子节点中, prev 为叶子节点); 如果 prev 节点值大
        #    于 val, 则将 val 对应的节点插入 prev 节点的左侧即可构成新的二叉搜索树; 同
        #    理如果 prev 节点值小于 val, 则插入右子节点;
        if prev.val > val:
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)

        return root


ls_ = [4, 2, 7, 1, 3]
val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is: [5, 2, 7, 1, 3, None, None, None, 4]
root = build_binary_tree(ls_)
res = Solution().insertIntoBST_v1(root, val)
print("pre_order: ", pre_order(res))


ls_ = [40, 20, 60, 10, 30, 50, 70]
val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]   或   [40, 20, 10, 30, 25, 60, 50, 70]
root1 = build_binary_tree(ls_)
res1 = Solution().insertIntoBST_v1(root1, val)
print("pre_order: ", pre_order(res1))
print("in_order: ", in_order(res1))


ls_ = [40, 20, 60, 10, 30, 50, 70]
val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]   或   [40, 20, 10, 30, 25, 60, 50, 70]
root1 = build_binary_tree(ls_)
res1 = Solution().insertIntoBST_v2(root1, val)
print("pre_order: ", pre_order(res1))
print("in_order: ", in_order(res1))


ls_ = [4, 2, 7, 1, 3, None, None, None, None, None, None]
val = 5
# Output: [4,2,7,1,3,5]
root2 = build_binary_tree(ls_)
res2 = Solution().insertIntoBST_v1(root2, val)
print("pre_order: ", pre_order(res2))


