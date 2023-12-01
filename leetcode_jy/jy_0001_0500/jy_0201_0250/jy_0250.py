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
title_jy = "Count-Univalue-Subtrees(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary tree, count the number of uni-value subtrees.
A Uni-value subtree means all nodes of the subtree have the same value.


Example:
Input:  root = [5, 1, 5, 5, 5, null, 5]
            5
           / \
          1   5
         / \   \
        5   5   5
Output: 4
"""


from about_TreeNode import *


class Solution:
    def __init__(self):
        self.count = 0

    """
递归求解, 分别对左右子树判断是否是 uni-value, 如果是则 count 加 1;
    """
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self._is_uni(root)

        return self.count


    def _is_uni(self, root):
        """判断 root 是否为 uni-value tree"""
        # jy: 递归终止条件, 返回 True 只代表当前 root (递归时可能对应的是左或右子
        #    树) 为 uni-value tree, 并不会改变 uni-value tree 的数量; 因为判断是
        #    否是 uni-value tree 是以包括当前节点在内的进行判断, 判断完后会进一步
        #    递归到左子树和右子树(即包括左子树在内的剩余子树); 经过层层递归后所有
        #    的子树也都将得到判断;
        if not root:
            return True

        is_left_uni = not root.left or (self._is_uni(root.left) and root.val == root.left.val)
        is_right_uni = not root.right or (self._is_uni(root.right) and root.val == root.right.val)
        # jy: 如果左右子树均与当前节点构成 uni-value tree, 则 self.count 加 1, 并返回 True;
        if is_left_uni and is_right_uni:
            self.count += 1
            return True
        else:
            return False



ls_ = [5, 1, 5, 5, 5, None, 5]
root = build_binary_tree(ls_)
# Output: 4
res = Solution().countUnivalSubtrees(root)
print(res)


