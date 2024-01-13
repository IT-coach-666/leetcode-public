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
title_jy = "Same-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 栈/队列 + 循环"


"""
Given the roots of two binary trees `p` and `q`, write a function to check if
they are the same or not. Two binary trees are considered the same if they are
structurally identical, and the nodes have the same value.


Example 1:
Input: p = [1, 2, 3], q = [1, 2, 3]
Output: true

Example 2:
Input: p = [1, 2], q = [1, null, 2]
Output: false

Example 3:
Input: p = [1, 2, 1], q = [1, 1, 2]
Output: false


Constraints:
1) The number of nodes in both trees is in the range [0, 100].
2) -10^4 <= Node.val <= 10^4
"""


from collections import deque
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree


class Solution:
    """
解法 1: 递归求解
    """
    def isSameTree_v1(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif p and q:
            return p.val == q.val and self.isSameTree_v1(p.left, q.left) \
                   and self.isSameTree_v1(p.right, q.right)
        else:
            return False


    """
解法 2: 队列 + 循环

使用一个队列保存两个树对应的节点, 依次出队, 判断两节点是否相等
    """
    def isSameTree_v2(self, p: TreeNode, q: TreeNode) -> bool:
        # jy: 将两树的当前节点组成一个元组放入队列中, 后续队列不空则
        #     不断出队, 并同时将出队的节点的左或右节点入队 (入队时同
        #     时左或右, 保持一致)
        queue = deque([(p, q)])
        while queue:
            a, b = queue.popleft()
            # jy: 如果节点均不为空, 则判断节点值是否相等, 并对后续子
            #     节点入队
            if a and b:
                if a.val != b.val:
                    return False
                queue.append((a.left, b.left))
                queue.append((a.right, b.right))
            # jy: 如果树节点均不存在, 则跳过, 继续从队列中出队 (此时
            #     的队列不一定已空)
            elif not a and not b:
                continue
            # jy: 如果只有一个树节点存在 (即另一个树节点为 None), 则
            #     直接返回 False
            else:
                return False
        return True


p = [1, 2, 3]
q = [1, 2, 3]
root_p = build_binary_tree(p)
root_q = build_binary_tree(q)
res = Solution().isSameTree_v1(root_p, root_q)
# jy: true
print(res)


p = [1, 2]
q = [1, None, 2]
root_p = build_binary_tree(p)
root_q = build_binary_tree(q)
res = Solution().isSameTree_v2(root_p, root_q)
# jy: false
print(res)


p = [1, 2, 1]
q = [1, 1, 2]
root_p = build_binary_tree(p)
root_q = build_binary_tree(q)
res = Solution().isSameTree_v2(root_p, root_q)
# jy: false
print(res)




