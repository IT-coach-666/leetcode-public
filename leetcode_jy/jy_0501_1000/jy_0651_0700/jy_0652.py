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
title_jy = "Find-Duplicate-Subtrees(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, return all duplicate subtrees. For each kind of duplicate
subtrees, you only need to return the root node of any one of them. Two trees are duplicate
if they have the same structure with the same node values.


Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]


Constraints:
The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
"""


from typing import List
from about_TreeNode import *


class Solution:
    """
深度优先遍历计算树的路径, 使用 Map 保存路径相同的子树, 最后遍历 Map 返回重复的子树的根节点;
    """
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        paths = {}
        duplicates = []
        # jy: 深度遍历计算树的路径, 使用 Map 保存路径相同的子树, 保存方式: {路径字符串: 树/子树的根节点列表, ...}
        self._get_path(root, paths)
        # jy: 遍历 paths, 如果对应的 value (即树的根节点列表) 含有的根节点大于 1 个, 表明有
        #    相同路径的子树, 将该子树的根节点存入结果列表(存入一个即可);
        for nodes in paths.values():
            if len(nodes) > 1:
                duplicates.append(nodes[0])

        return duplicates


    def _get_path(self, root, paths):
        """
        深度遍历计算树的路径, 使用 Map 保存路径相同的子树, 保存方式: {路径字符串: 树/子树的根节点列表, ...}
        """
        if not root:
            return ''
        # jy: 递归获取左子树的全节点路径表示(字符串形式);
        left_path = self._get_path(root.left, paths)
        # jy: 递归获取右子树的全节点路径表示;
        right_path = self._get_path(root.right, paths)
        # jy: 构造以当前节点为根节点的树的全节点路径表示;
        full_path = 'l' + left_path + 'c' + str(root.val) + 'r' + right_path
        # jy: 如果某子树的全节点路径字符串已经在 paths 中, 表明该子树与原先子树
        #    路径相同, 是相同结构类型的子树, 将其加入到对应的列表中;
        if full_path in paths:
            paths[full_path].append(root)
        # jy: 如果某子树的全节点路径字符串还不在 paths 中, 将该子树的全节点路径字符串
        #    加入 paths 字典, 并设置对应的 value 为一个含该子树根节点的列表;
        else:
            paths[full_path] = [root]

        return full_path


# ls_ = [1, 2, 3, 4, None, 2, 4, None, None, 4]
ls_ = [1, 2, 3, 4, None, 2, 4, None, None, None, None, 4]
# Output: [[2,4],[4]]
root = build_binary_tree(ls_)
res = Solution().findDuplicateSubtrees(root)
print(res)
for i in res:
    print(i.val)


ls_ = [2, 1, 1]
# Output: [[1]]
root = build_binary_tree(ls_)
res = Solution().findDuplicateSubtrees(root)
print(res)
for i in res:
    print(i.val)


ls_ = [2, 2, 2, 3, None, 3, None]
# Output: [[2,3],[3]]
root = build_binary_tree(ls_)
res = Solution().findDuplicateSubtrees(root)
print(res)
for i in res:
    print(i.val)


