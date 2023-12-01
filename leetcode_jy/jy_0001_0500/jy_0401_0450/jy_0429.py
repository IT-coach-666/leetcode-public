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
title_jy = "N-ary-Tree-Level-Order-Traversal(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Example 1:   https://www.yuque.com/frederick/dtwi9g/uehsno
Input: root = [1, None, 3, 2, 4, None, 5, 6]
Output: [[1], [3, 2, 4], [5, 6]]

Example 2:
Input: root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]
Output: [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]]

Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
"""


from collections import deque
from typing import List
from about_TreeNode import *



class Solution:
    """
使用队列求解, 首先将根节点加入队列, 遍历队列时首先记录队列的长度, 该长度即当前层的节点
数量, 记为 k, 连续出队 k 次即获得当前层的节点, 出队时同时将节点的子节点加入到队列中(即
将所有下一层的节点加入到队列中);
    """
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        levels = []
        queue = deque([root])

        while queue:
            # jy: 当前层的节点数;
            size = len(queue)
            # jy: 存放当前层节点值的列表;
            level = []
            # jy: 将当前层的节点左侧出队, 加入到 level 列表中, 顺便将其子节点(即所有下一层的
            #    节点加入到队列中)
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.children:
                    for child in node.children:
                        queue.append(child)

            levels.append(level)

        return levels


# root = [1, None, 3, 2, 4, None, 5, 6]
ls_N_ary = [1, [3, [5, 6], 2, 4]]
root = build_N_ary_tree(ls_N_ary)
# Output: [[1], [3, 2, 4], [5, 6]]
res = Solution().levelOrder(root)
print(res)


# root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]
ls_N_ary = [1, [2, 3, [6, 7, [11, [14]]], 4, [8, [12]], 5, [9, [13], 10]]]
root = build_N_ary_tree(ls_N_ary)
# Output: [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]]
res = Solution().levelOrder(root)
print(res)


