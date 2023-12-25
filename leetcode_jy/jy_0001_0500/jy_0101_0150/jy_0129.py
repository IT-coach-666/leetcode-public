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
title_jy = "Sum-Root-to-Leaf-Numbers(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1: 图示参考: https://www.yuque.com/it-coach/leetcode/mt7zlzghu07sgpn2
Input: root = [1, 2, 3]
Output: 25
Explanation: The root-to-leaf path 1->2 represents the number 12.
             The root-to-leaf path 1->3 represents the number 13.
             Therefore, sum = 12 + 13 = 25.

Example 2: 图示参考: https://www.yuque.com/it-coach/leetcode/mt7zlzghu07sgpn2
Input: root = [4, 9, 0, 5, 1]
Output: 1026
Explanation: The root-to-leaf path 4->9->5 represents the number 495.
             The root-to-leaf path 4->9->1 represents the number 491.
             The root-to-leaf path 4->0 represents the number 40.
             Therefore, sum = 495 + 491 + 40 = 1026.
 

Constraints:
1) The number of nodes in the tree is in the range [1, 1000].
2) 0 <= Node.val <= 9
3) The depth of the tree will not exceed 10.
"""


class Solution:
    """
解法 1: https://leetcode.cn/problems/sum-root-to-leaf-numbers/solutions/464953/129-qiu-gen-dao-xie-zi-jie-dian-shu-zi-zhi-he-di-4/
    """
    def sumNumbers_v1(self, root: TreeNode) -> int:
        res = 0
        path = []
        def backtrace(root):
            nonlocal res
            if not root: return # 节点空则返回
            path.append(root.val)
            if not root.left and not root.right: # 遇到了叶子节点
                res += get_sum(path)
            if root.left: # 左子树不空
                backtrace(root.left)
            if root.right: # 右子树不空
                backtrace(root.right)
            path.pop()

        def get_sum(arr):
            s = 0
            for i in range(len(arr)):
                s = s * 10 + arr[i]
            return s

        backtrace(root)
        return res

    
root = [1, 2, 3]
res = Solution().sumNumbers_v1(root)
# jy: 25
print(res)


root = [4, 9, 0, 5, 1]
res = Solution().sumNumbers_v1(root)
# jy: 1026
print(res)
