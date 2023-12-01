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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Vertical-Order-Traversal-of-a-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions
(row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each
column index starting from the leftmost column and ending on the rightmost column. There may
be multiple nodes in the same row and same column. In such a case, sort these nodes by their
values. Return the vertical order traversal of the binary tree.



Example 1:  https://www.yuque.com/frederick/dtwi9g/qo86tl
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.

Example 2:
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.

Example 3:
Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.



Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
"""


import collections
from typing import List
from about_TreeNode import *


class Solution:
    """
和 314_Binary-Tree-Vertical-Order-Traversal.py 一样, 只是多了一步处理同一列节点的顺
序, Map 中除了保存节点的值和所在列外, 还需要保存节点所在的行用于后续排序;
    """
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        columns = collections.defaultdict(list)
        queue = [(root, 0, 0)]

        for node, row, column in queue:
            if node:
                columns[column].append((row, node.val))
                queue.append((node.left, row + 1, column - 1))
                queue.append((node.right, row + 1, column + 1))

        return [self._get_sorted_row(columns[row]) for row in sorted(columns)]


    def _get_sorted_row(self, row):
        return [x[1] for x in sorted(row)]


    def verticalTraversal_jy(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return []
        queue = [(root, 0, 0)]

        for node, row, column in queue:
            if node.left:
                queue.append((node.left, row + 1, column - 1))
            if node.right:
                queue.append((node.right, row + 1, column + 1))
        # jy: 先按列进行排序, 再按行进行排序;
        queue.sort(key=lambda x: (x[2], x[1], x[0].val))
        # jy: 将相同列的放置到一个列表中存储;
        tmp_set = set()
        tmp_ls = []
        for node_info in queue:
            if node_info[2] in tmp_set:
                tmp_ls.append(node_info[0].val)
            else:
                if tmp_ls:
                    res.append(tmp_ls)
                tmp_ls = [node_info[0].val]
                tmp_set.add(node_info[2])
        res.append(tmp_ls)
        print(queue)
        return res


ls_ = [3, 9, 20, None, None, 15, 7]
root = build_binary_tree(ls_)
# Output: [[9],[3,15],[20],[7]]
res = Solution().verticalTraversal(root)
print(res)


ls_ = [1, 2, 3, 4, 5, 6, 7]
root = build_binary_tree(ls_)
# Output: [[4],[2],[1,5,6],[3],[7]]
res = Solution().verticalTraversal(root)
print(res)


ls_ = [1, 2, 3, 4, 6, 5, 7]
root = build_binary_tree(ls_)
# Output: [[4],[2],[1,5,6],[3],[7]]
res = Solution().verticalTraversal_jy(root)
print(res)



