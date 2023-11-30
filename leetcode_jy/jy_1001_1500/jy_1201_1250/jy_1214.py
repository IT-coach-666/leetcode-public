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
title_jy = "Two-Sum-BSTs(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Given two binary search trees, return True if and only if there is a node in the first 
tree and a node in the second tree whose values sum up to a given integer target.


Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false


Constraints:    
Each tree has at most 5000 nodes.
-10^9 <= target, node.val <= 10^9
"""



from typing import Set
from about_TreeNode import *


class Solution:
    """
这道题可以看作是 653_Two-Sum-IV_Input-is-a-BST.py 的扩展, 核心思想依然是遍历其
中一棵二叉搜索树, 对于树中的每一个元素 n, 判断 target - n 是否在另一棵树中;

不同的是, 在遍历之前, 要先将某棵树的所有的结点的值处理到一个 Set 中, 方便判断
target - n 是否在这棵树中;
    """
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        nums = set()
        # jy: 将树节点值存放到 nums 集合中;
        self._traverse(root1, nums)
        return self._find(root2, target, nums)

    def _traverse(self, root: TreeNode, nums: Set[int]):
        """将树节点值存放到 nums 集合中"""
        if not root:
            return
        nums.add(root.val)
        self._traverse(root.left, nums)
        self._traverse(root.right, nums)


    def _find(self, root: TreeNode, k: int, visited: Set[int]) -> bool:
        if not root:
            return False

        if k - root.val in visited:
            return True

        return self._find(root.left, k, visited) or self._find(root.right, k, visited)


ls_1 = [2,1,4]
ls_2 = [1,0,3]
root1 = build_binary_tree(ls_1)
root2 = build_binary_tree(ls_2)
target = 5
# Output: true
res = Solution().twoSumBSTs(root1, root2, target)
print(res)


ls_1 = [0,-10,10]
ls_2 = [5,1,7,0,2]
root1 = build_binary_tree(ls_1)
root2 = build_binary_tree(ls_2)
target = 18
# Output: false
res = Solution().twoSumBSTs(root1, root2, target)
print(res)



