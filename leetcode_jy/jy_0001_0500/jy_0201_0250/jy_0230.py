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
title_jy = "Kth-Smallest-Element-in-a-BST(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary search tree(BST), write a function kthSmallest to find the kth
smallest element in it. You may assume k is always valid, 1 ≤ k ≤ BST's total
elements.


Example 1:
Input: root = [3, 1, 4, null, 2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1


Example 2:
Input: root = [5, 3, 6, 2, 4, null, null, 1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3


Follow up: What if the BST is modified (insert/delete operations) often and you need to
           find the kth smallest frequently?
           How would you optimize the  kthSmallest routine?
"""


from about_TreeNode import *


class Solution:
    """
解法1: 将二叉搜索树转化为一个有序数组, 然后数组的第 k 个元素就是第 k 小的数;
    """
    def kthSmallest_v1(self, root: TreeNode, k: int) -> int:
        nodes = self._traverse(root)
        return nodes[k-1].val


    def _traverse(self, root: TreeNode):
        if not root:
            return []
        # jy: 二叉搜索树中序遍历(二叉搜索树的中序遍历即已经是升序结果), 将遍历结
        #    果放入数组中, 最后返回;
        return self._traverse(root.left) + [root] + self._traverse(root.right)



    """
解法2: 创建一个栈, 然后将所有左结点都压入栈, 这样栈顶所在的元素是最小的, 然后每次出栈
一个结点, 同时 k 减 1, 如果 k 为 0, 则当前出栈的结点为第 k 小的结点, 否则将当前结点的
右结点压入栈, 继续循环;
    """
    def kthSmallest_v2(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root

        while True:
            while current:
                # jy: 最开始是将根节点入栈, 随后不断将其左子节点入栈, 直到最后 current 为
                #    None 时, 栈顶元素即为最左侧最小的元素值;
                stack.append(current)
                current = current.left
            # jy: 将最小的元素出栈, 同时 k 减 1;
            current = stack.pop()
            k -= 1
            # jy: 如果 k 正好等于 0, 即表明当前出栈元素为第 k 小的值;
            if k == 0:
                return current.val
            # jy: 再将该出栈元素的右子节点入栈(如果右子节点存在的话), 此右节点的父节点已经
            #    出栈(确保每个出栈的元素都会是栈中最小的);
            current = current.right


ls_ = [3, 1, 4, None, 2]
k = 1
# Output: 1
root = build_binary_tree(ls_)
res = Solution().kthSmallest_v1(root, k)
print(res)

ls_ = [5, 3, 6, 2, 4, None, None, 1]
k = 3
# Output: 3
root = build_binary_tree(ls_)
res = Solution().kthSmallest_v1(root, k)
print(res)


