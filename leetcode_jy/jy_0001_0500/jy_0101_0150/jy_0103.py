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
title_jy = "Binary-Tree-Zigzag-Level-Order-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = "循环/迭代 + 层级遍历 | 递归"


"""
Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).


For example:
Given binary tree [3, 9, 20, null, null, 15, 7],
    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:
[ [3],
  [20,9],
  [15,7]]
"""

from collections import deque
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree


class Solution:
    """
解法 1: 两个双向队列 (虽然是队列, 但使用时均是后进先出的逻辑)

queue1 存放奇数层节点, queue2 存放偶数层节点, 并确保两个队列中从左到右的
节点均为树中奇数层或偶数层中从左到右的节点

当为奇数层时, 从 queue1 左侧不断出队, 并将出队节点的左右子节点依次右侧加
入 queue2 队列; 使得 queue2 队列中从左到右存储的为下一层偶数层节点的从左
到右的节点

当为偶数层时, 从 queue2 右侧不断出队, 并将出队节点的右子节点和左子节点依
次左侧加入 queue1 队列; 使得 queue1 队列中从左到右存储的为下一层奇数层节
点的从左到右的节点


注意: 两个队列均为后进先出, 因此均可替换为栈
    """
    def zigzagLevelOrder_v1(self, root: TreeNode) -> List[List[int]]:
        # jy: 统计当前层为第几层
        depth = 0
        ls_level = []

        # jy: 存放奇数层的节点值 (奇数层从左到右存放)
        queue1 = deque([root]) if root else deque()
        # jy: 存放偶数层的节点值 (偶数层从右到左存放)
        queue2 = deque()

        # jy: 当两个双向队列均为空时, 遍历结束, 退出循环
        while queue1 or queue2:
            # jy: depth 表示当前为第几层
            depth += 1
            ls_level_i = []
            # jy: 记录当前是否是奇数层
            is_odd = depth & 1 == 1
            # jy: 如果是奇数层, 此时 queue1 队列的长度即为奇数层的元素个数,
            #     则遍历 queue1 队列, 从队列左侧出元素 (后续往 queue1 中加
            #     入节点时, 也会确保加入到队列后, 队列中从左到右为树中奇数
            #     层从左到右的节点), 并依次将出队节点的左右子节点依次从
            #     queue2 右侧 (即队尾) 入队, 因此奇数层节点遍历完后, queue2
            #     队列中的节点从左到右即为下一层偶数层从左到右的节点
            if is_odd:
                for _ in range(len(queue1)):
                    node = queue1.popleft()
                    ls_level_i.append(node.val)
                    if node.left:
                        queue2.append(node.left)
                    if node.right:
                        queue2.append(node.right)
            # jy: 如果是偶数层, 此时 queue2 队列的长度即为偶数层的元素个数,
            #     则遍历 queue2 队列, 从队列右侧逐个出元素, 使得偶数层出队
            #     顺序是从右往左, 并将出队节点的右子节点和左子节点依次从左
            #     侧入 queue1 队列, 使得遍历完成后, queue1 队列中的节点从
            #     左到右即为下一层奇数层中的从左到右的节点
            else:
                for _ in range(len(queue2)):
                    node = queue2.pop()
                    ls_level_i.append(node.val)
                    if node.right:
                        queue1.appendleft(node.right)
                    if node.left:
                        queue1.appendleft(node.left)
            ls_level.append(ls_level_i)
        return ls_level


    """
解法 2: 将解法 1 中的队列改为栈, 逻辑不变
    """
    def zigzagLevelOrder_v2(self, root: Optional[TreeNode]) -> List[List[int]]:
        depth = 0
        ls_level = []
        stack1 = [root] if root else []
        stack2 = []
        while stack1 or stack2:
            depth += 1
            ls_level_i = []
            is_odd = depth & 1 == 1
            if is_odd:
                for _ in range(len(stack1)):
                    node = stack1.pop()
                    ls_level_i.append(node.val)
                    if node.left:
                        stack2.append(node.left)
                    if node.right:
                        stack2.append(node.right)
            else:
                for _ in range(len(stack2)):
                    node = stack2.pop()
                    ls_level_i.append(node.val)
                    if node.right:
                        stack1.append(node.right)
                    if node.left:
                        stack1.append(node.left)
            ls_level.append(ls_level_i)
        return ls_level


    """
解法 3: 将解法 1 简化为使用一个双端队列

在 0102 (Binary-Tree-Level-Order-Traversal) 中的解法 2 的基础上增加一个变量
记录当前层数:
1) 当为奇数层时, 从队列左侧出队, 并将出队节点的左子节点和右子节点依次右侧入队
2) 当为偶数层时, 从队列右侧出队, 并将出队节点的右子节点和左子节点依次左侧入队

每次遍历队列元素时, 队列中从左到右的元素均为树中当前层从左到右的元素
    """
    def zigzagLevelOrder_v3(self, root: TreeNode) -> List[List[int]]:
        # jy: 统计当前层数
        depth = 0
        ls_level = []
        queue = deque([root]) if root else deque()
        while queue:
            # jy: 第一遍循环即 depth 为 1, 表示第一层
            depth += 1
            ls_level_i = []
            # jy: 判断该层是否为奇数层
            is_odd = depth & 1 == 1
            # jy: 每次开始 for 循环时, queue 中保留了当前层的所有元素, 循环
            #     过程中会不断从队列中出元素, 并同时在队列中加入元素
            len_q = len(queue)
            for _ in range(len_q):
                # jy: 如果为奇数层, 则从队列左侧出队, 并将出队节点的左子节
                #     点和右子节点依次右侧入队
                if is_odd:
                    node = queue.popleft()
                    ls_level_i.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                # jy: 如果为偶数层时, 从队列右侧出队, 并将出队节点的右子节
                #     点和左子节点依次左侧入队
                else:
                    node = queue.pop()
                    ls_level_i.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
            # jy: 一次 for 循环结束后, ls_level_i 中的值即为当前层的结果
            ls_level.append(ls_level_i)
        return ls_level


    """
解法 4: 队列 (先进先出), 即基于层级遍历, 并用一个变量统计层数, 同时初始化
当前层存放节点的列表, 并基于层的奇偶性判断是从前往后加入, 还是从后往前加入
    """
    def zigzagLevelOrder_v4(self, root: TreeNode) -> List[List[int]]:
        queue = deque([root]) if root else deque()
        ls_level = []
        depth = 0
        while queue:
            depth += 1
            is_odd = depth & 1 == 1
            length = len(queue)
            # jy: 先初始化当前层的所有元素值为 0
            ls_level_i = [0] * length
            for i in range(length):

                node = queue.popleft()
                # jy: 如果是奇数层, 将该层的元素 (已为树结构的对应层的从左到
                #     右遍历结果) 从前往后填充到 ls_level_i 中
                if is_odd:
                    ls_level_i[i] = node.val
                # jy: 如果是偶数层, 将该层的元素 (已为树结构的对应层的从左到
                #     右遍历结果) 从后往前填充到 ls_level_i 中
                else:
                    ls_level_i[length - i-1] = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ls_level.append(ls_level_i)
        return ls_level


    """
解法 5: 深度优先搜索, 在 0102 (Binary-Tree-Level-Order-Traversal) 的解法 3 的
基础上判断当前层的是奇数层还是偶数层, 如果是奇数层, 则从层数组的末尾插入, 否
则从层数组头插入
    """
    def zigzagLevelOrder_v5(self, root: TreeNode) -> List[List[int]]:
        ls_level = []
        self._dfs(root, 1, ls_level)
        return ls_level

    def _dfs(self, root: TreeNode, ls_level: int, result: List[List[int]]) -> None:
        if not root:
            return

        if ls_level > len(result):
            result.append([])
        # jy: 如果是基数层, 则从数组尾插入; 否则从数组头插入 (从列表头插入的
        #     时间复杂度为 0(n) )
        if ls_level & 1 == 1:
            result[ls_level - 1].append(root.val)
        else:
            result[ls_level - 1].insert(0, root.val)

        self._dfs(root.left, ls_level + 1, result)
        self._dfs(root.right, ls_level + 1, result)


ls_ = [3, 9, 20, None, None, 15, 7]
root = build_binary_tree(ls_)

res = Solution().zigzagLevelOrder_v1(root)
print(res)

res = Solution().zigzagLevelOrder_v2(root)
print(res)

res = Solution().zigzagLevelOrder_v3(root)
print(res)

res = Solution().zigzagLevelOrder_v4(root)
print(res)

res = Solution().zigzagLevelOrder_v5(root)
print(res)

