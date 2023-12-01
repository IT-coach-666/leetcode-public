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
title_jy = "Maximum-Depth-of-N-ary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a n-ary tree, find its maximum depth. The maximum depth is the number of nodes
along the longest path from the root node down to the farthest leaf node. N-ary-Tree
input serialization is represented in their level order traversal, each group of
children is separated by the null value (See examples).


Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5


Constraints:
The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 10^4].
"""


from about_TreeNode import *
from collections import deque


class Solution:
    """
解法1: 递归求解;
    """
    def maxDepth_v1(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max([self.maxDepth_v1(child) for child in root.children])


    """
解法2: 和 104_Maximum-Depth-of-Binary-Tree.py 的解法 2 一样;
    """
    def maxDepth_v2(self, root: 'Node') -> int:
        if not root:
            return 0
        # jy: 初始化深度为 0, 并将根节点入队;
        depth = 0
        queue = deque([root])
        # jy: 如果队不为空, 则遍历: 用 size 记录树的当前层的节点数, 然后循环遍历 size 次,
        #    每次都出队一个元素, 将当前层的元素都出队, 并将其下一层的元素都入队, 此时 depth
        #    加 1 (遍历完一层就加 1, 代表深度; 以下代码逻辑是先加 1, 后遍历层; 也可以遍历层
        #    后再加 1)
        while queue:
            depth += 1
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                if node.children:
                    for child in node.children:
                        queue.append(child)

        return depth


ls_N_ary = [1, [3, [5, 6], 2, 4]]
root = build_N_ary_tree(ls_N_ary)
# print(show_N_ary_tree(root))
# Output: 3
res = Solution().maxDepth_v1(root)
print(res)


ls_N_ary = [1, [2, 3, [6, 7, [11, [14]]], 4, [8, [12]], 5, [9, [13], 10]]]
root = build_N_ary_tree(ls_N_ary)
# print(show_N_ary_tree(root))
# Output: 5
res = Solution().maxDepth_v1(root)
print(res)


