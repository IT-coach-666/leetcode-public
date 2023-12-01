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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Second-Minimum-Node-In-a-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where
each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then
this node's value is the smaller value among its two sub-nodes. More formally, the property
root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all
the nodes' value in the whole tree. If no such second minimum value exists, output -1 instead.


Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:
Input:
    2
   / \
  2   2
Output: -1


Explanation: The smallest value is 2, but there isn't any second smallest value.
"""


import sys
from about_TreeNode import *


class Solution:
    """
解法1: 由题中可知, 父节点的值是左右结点中值的较小值, 所以根节点的值是所有结点中的最小
值, 所以第二小的结点就是求左子树和右子树中的最小值; 创建一个栈, 然后将结点依次加入栈
中, 循环出栈, 判断结点的值是否不等于根节点的值并且比目前第二小的值小, 如果是, 则更新
第二小的值;
    """
    def findSecondMinimumValue_v1(self, root: TreeNode) -> int:
        # jy: 记录根节点的值;
        min_value = root.val
        # jy: 初始化第 2 小的值;
        second_min_value = sys.maxsize
        # jy: 根节点入栈;
        nodes = [root]
        # jy: 如果栈非空, 则不断出栈判断(会将栈中的节点的左右子节点入栈, 最终遍历树的所有节点);
        while nodes:
            node = nodes.pop()
            # jy: 如果当前节点值不等于最小值(根节点值)且小于第二小值, 则更新第二小值为当前节点值;
            if node.val != min_value and node.val < second_min_value:
                second_min_value = node.val
            # jy: 如果当前节点的左子节点存在(如果存在子节点, 必定是左右都存在, 判断一个即可), 则
            #    将左右子节点入栈;
            if node.left:
                nodes.append(node.left)
                nodes.append(node.right)
        # jy: 最终返回第二小节点值
        return second_min_value if second_min_value != sys.maxsize else -1


    """
解法2: 递归求解, 递归分别求得左子树和右子树中不等于根结点的最小值, 然后返回两者的较小值即可;
    """
    def findSecondMinimumValue_v2(self, root: TreeNode) -> int:
        return self._find_min(root, root.val)

    def _find_min(self, root: TreeNode, root_value: int) -> int:
        # jy: 如果当前节点值大于根节点值(即最小值), 则直接返回当前节点值;
        if root.val > root_value:
            return root.val
        # jy: 如果当前节点的左子节点存在(如果存在子节点, 必定是左右都存在, 判断一个即可), 则
        #    递归遍历左右子树, 找出左右子树中不等于根结点的最小值, 返回两者的较小值即可;
        if root.left:
            left_min = self._find_min(root.left, root_value)
            right_min = self._find_min(root.right, root_value)

            return self._min(left_min, right_min)

        return -1

    def _min(self, a: int, b: int) -> int:
        # jy: 如果 a 为 -1, 即左子树没找到合适的值, 则返回 b (不管 b 是否是 -1, 直接返回即是正确的返回结果)
        if a == -1:
            return b
        # jy: 如果 b 为 -1, 即右子树没找到合适的值, 直接返回 a (不管 a 是否是 -1, 直接返回即是正确的结果)
        elif b == -1:
            return a
        # jy: 如果 a 和 b 均不为 -1, 表明左右子树均有合适的值, 返回其中的较小值即可;
        else:
            return min(a, b)


ls_ = [2, 2, 5, None, None, 5, 7]
root = build_binary_tree(ls_)
res = Solution().findSecondMinimumValue_v1(root)
print(res)


ls_ = [2, 2, 2]
root = build_binary_tree(ls_)
res = Solution().findSecondMinimumValue_v1(root)
print(res)


