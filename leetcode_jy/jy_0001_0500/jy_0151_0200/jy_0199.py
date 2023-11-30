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
title_jy = "Binary-Tree-Right-Side-View(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree, imagine yourself standing on the right side of
it, return the values of the nodes you can see ordered from top to bottom.


Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


import collections
from collections import deque
from typing import Optional, List
from about_TreeNode import *


class Solution:
    """
解法1: 队列 + 广度优先搜索: 队列中保存: (结点所在层级, 结点), 每次先将右结点放入队
列, 这样右结点就能先被访问到, 同时使用变量 next_level 标记下一个即将被访问的层级;

JY: 注意, 队列中保存的是节点, 不是节点对应的数值, 因为后续还需要获取节点的子节点;
    """
    def rightSideView_v1(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        order = []
        # jy: 根节点作为第 1 层入队;
        queue = collections.deque([(1, root)])
        # jy: 下一个即将被访问的层级为 1 (并非根据每层操作后队列的长度来
        #     确定每层元素的个数)
        next_level = 1
        while queue:
            # jy: 左侧出队元素(先进先出);
            level, node = queue.popleft()
            # jy: 如果当前元素的层级为下一个要被访问的层级, 表明当前元素已经是下一个目标
            #     层级的第一个元素, 即是每层的最右侧元素 (由于入队总是先将右子节点入队, 再
            #     将左子节点入队), 获取该元素后, 下一个即将被访问的层级为当前层级加 1 (因
            #     为每个层级获取最右侧的一个元素即可);
            if level == next_level:
                order.append(node.val)
                next_level += 1
            # jy: 先将当前节点的右子节点入队, 后将左子节点入队, 使得队列中同一层级的所有节
            #     点中的第一个节点即为二叉树在该层级的最右节点;
            if node.right:
                queue.append((level + 1, node.right))
            if node.left:
                queue.append((level + 1, node.left))

        return order

    """
解法2: 基于每轮循环时当前队列的长度确定当前的层级: 每次开始循环遍历队列时, 当前队列
的长度包含了当前层级的所有结点, 遍历当前层级的所有结点, 并将当前层级节点的子节点(即
下一层级的节点)入队(右子节点或左子节点先入队均可), 因此当当前层级节点全出队后, 当前队列
中的节点就均为下一层级的所有节点;   关于入队顺序:
1) 如果是右子节点先入队, 则每层节点的第一个元素为二叉树的相应层级节点中的最右侧节点;
2) 如果是左子节点先入队, 则每层节点的最后一个元素为二叉树的相应层级节点中的最右侧节点;
    """
    def rightSideView_v2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        order = []
        queue = collections.deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                # jy-version-1-Begin ----------------------------
                '''
                # jy: 右子节点先入队, 则当前层的第一个节点为二叉树对应层的最右节点;
                if i == 0:
                    order.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                '''
                # jy-version-1-End ------------------------------
                # jy-version-2-Begin ----------------------------
                # jy: 左子节点先入队(右子节点后入队), 则当前层的最后一个节点为二叉树对应层的最右节点;
                if i == size - 1:
                    order.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # jy-version-2-End ------------------------------
        return order

    """
解法3: 递归版本;
    """
    def rightSideView_v3(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        self._dfs(root, 1, order)
        return order

    def _dfs(self, root, level, order):
        if not root:
            return
        # jy: 如果列表 order 的长度小于当前层级, 表明当前层级的第一个元素为树的相应层
        #     级的最右侧节点(因为总共是右子节点优先递归搜索), 将其加入到 order 中;
        # jy: 该判断方式必须是优先递归右子节点, 如果优先递归左子节点, 需要额外引入变量
        #     用以记录每一层的所有节点, 随后获取对应层的最后一个节点(如引入字典记录某层
        #     对应的节点), 这样会增加复杂度(空间复杂度增加);
        if len(order) < level:
            order.append(root.val)

        if root.right:
            self._dfs(root.right, level + 1, order)
        # jy: 注意, 尽管以上不断递归遍历节点的右子节点可以获取二叉树的最右侧的右子节点,
        #     但不能不对左子节点进行递归, 因为当最右侧的节点不是右子节点时, 需要用到最右
        #     侧的左子节点;
        if root.left:
            self._dfs(root.left, level + 1, order)

    """
JY: 同理解法 2, 入队顺序有些区别;
    """
    def rightSideView_jy_2021_12_26(self, root):
        if not root:
            return []
        queue_ = deque([root])
        res = []
        while queue_:
            # jy: 由于只需要每一层的最右边一个节点值, 故不需要存储每一层的所有节点
            #     值, 使用一个 rightest 变量记录每层最右侧的值即可;
            # tmp = []
            rightest = None
            len_ = len(queue_)
            for _ in range(len_):
                node = queue_.popleft()
                # tmp.append(node.val)
                rightest = node.val
                if node.left:
                    queue_.append(node.left)
                if node.right:
                    queue_.append(node.right)
            # res.append(tmp[-1])
            res.append(rightest)
        return res


ls_ = [1, 2, 3, None, 5, None, 4]
# Output: [1,3,4]
root = build_binary_tree(ls_)
res = Solution().rightSideView_v1(root)
print(res)


ls_ = [1, None, 3]
# Output: [1,3]
root = build_binary_tree(ls_)
res = Solution().rightSideView_v1(root)
print(res)


ls_ = []
# Output: []
root = build_binary_tree(ls_)
res = Solution().rightSideView_v1(root)
print(res)


ls_ = [1, None, 3]
# Output: [1,3]
root = build_binary_tree(ls_)
res = Solution().rightSideView_jy_2021_12_26(root)
print(res)


