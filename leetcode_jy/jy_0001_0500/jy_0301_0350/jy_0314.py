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
title_jy = "Binary-Tree-Vertical-Order-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, return the vertical order traversal of its nodes'
values. (i.e., from top to bottom, column by column). If two nodes are in the same
row and column, the order should be from left to right.


Example 1:  (图: https://www.yuque.com/frederick/dtwi9g/qgyxhe)
Input: root = [3, 9, 20, null, null, 15, 7]
Output: [[9], [3, 15], [20], [7]]

Example 2:
Input: root = [3, 9, 8, 4, 0, 1, 7]
Output: [[4], [9], [3, 0, 1], [8], [7]]

Example 3:
Input: root = [3, 9, 8, 4, 0, 1, 7, null, null, null, 2, 5]
Output: [[4], [9, 5], [3, 0, 1], [8, 2], [7]]

Example 4:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


import collections
from typing import List

from about_TreeNode import *




class Solution:
    """
使用 Map 保存每一列对应的元素, 使用广度优先搜索遍历树, 首先将根结点加入队列中, 同时指
定根节点所在的列的值为 0, 遍历队列时, 出队一个节点和它所在的列, 将其左右子节点加入到
队列中, 左右子节点的列就是在当前节点的列上加减 1; 最后按照键的大小遍历 Map, 构造结果;
    """
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # jy: 定义一个默认值为 [] 的字典;
        columns = collections.defaultdict(list)
        # jy: 假设根节点所在列的编号为 0, 将根节点以及其对应的编号加入队列(列表)
        queue = [(root, 0)]
        # jy: 循环遍历队列中的节点;
        for node, i in queue:
            # jy: 如果当前节点不为空, 则将当前节点的列编号作为 key, 对应值作为 value 加
            #    入到 columns 字典中; 并将其左右子节点加入到 queue 中, 左子节点对应的列
            #    编号减1, 右子节点对应的列编号加1;
            if node:
                columns[i].append(node.val)
                queue.append((node.left, i-1))
                queue.append((node.right, i+1))

        # jy: 依据列编号进行排序, 然后获取对应列编号的节点数值结果;
        return [columns[i] for i in sorted(columns)]


ls_ = [3, 9, 20, None, None, 15, 7]
root = build_binary_tree(ls_)
# Output: [[9], [3, 15], [20], [7]]
res = Solution().verticalOrder(root)
print(res)


ls_ = [3, 9, 8, 4, 0, 1, 7]
root = build_binary_tree(ls_)
# Output: [[4], [9], [3, 0, 1], [8], [7]]
res = Solution().verticalOrder(root)
print(res)


ls_ = [3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5]
root = build_binary_tree(ls_)
# Output: [[4], [9, 5], [3, 0, 1], [8, 2], [7]]
res = Solution().verticalOrder(root)
print(res)


ls_ = []
root = build_binary_tree(ls_)
# Output: []
res = Solution().verticalOrder(root)
print(res)


