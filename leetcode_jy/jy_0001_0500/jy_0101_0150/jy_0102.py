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
title_jy = "Binary-Tree-Level-Order-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3, 9, 20, null, null, 15, 7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[ [3],
  [9,20],
  [15,7]]
"""


from collections import deque
from typing import List
from about_TreeNode import *


class Solution:
    """
解法1: 广度优先搜索; 需要知道哪些结点在同一层, 可以新建两个队列 queue1 和 queue2, queue1 存储
当前层的结点, queue2 存储下一层的结点, queue1 不断出队, 同时将下一层的结点加入 queue2, 并收集
当前层结点的值, 当 queue1 为空时, 交换 queue1 和 queue2, 并将收集至今的当前层结点值的数组加入
最终结果中, 然后继续对下一层执行出队和入队操作;
    """
    def levelOrder_v1(self, root: TreeNode) -> List[List[int]]:
        # jy: deque 是为了高效实现插入和删除操作的双向列表, 适合用于队列和栈;
        queue1 = deque([root]) if root else deque()
        queue2 = deque()
        level = []
        levels = []
        while queue1:
            # jy: 从 queue1 的左边出一个元素, 放入 level 列表(表示同一层, 最开始只有一个元素);
            #    queue1 中出对的节点均为同一层的节点;
            node = queue1.popleft()
            level.append(node.val)
            # jy: 将下一层节点入队; 由于 queue1 中出对的节点均为同一层的节点, 其 left 和 right
            #    则均为下一层节点;
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
            # jy: 如果 queue1 已空, 即表明属于同一层的节点已经出栈完成(均放置到 level 列表中), 且
            #    其下一层的节点也均已加入 queue2 中, 此时将 level 加入 levels 中, 并重新设置 level
            #    为空列表, 用于存放下一层元素; 同时将 queue2 赋值给 queue1, 并将 queue2 置空, 进
            #    行下一层遍历;
            if not queue1:
                queue1, queue2 = queue2, queue1
                levels.append(level)
                level = []
        return levels

    """
解法2: 解法 1 的两个队列可以优化为一个队列; 遍历队列时, 先记录队列的长度 n, 然后执行 n 次出队
操作, 则这 n 次出队的结点都是同一层的结点;
    """
    def levelOrder_v2(self, root: TreeNode) -> List[List[int]]:
        queue = deque([root]) if root else deque()
        levels = []
        while queue:
            level = []
            # jy: 第一轮遍历时, 根节点一层只有一个元素, 循环一次: 出队一个元素, 并将其左右子节点
            #    入队(入队过程中不会影响当前的 len(queue), 需等原先 for 循环结束后该值再做更新);
            #    经过一轮循环后, queue 的长度即下一层元素的个数;
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return levels

    """
解法3: 深度优先搜索; 首先初始化一个数组 result, 用于深度优先搜索时往里面加入各层结点的值; 深
度优先搜索时记录当前的层数, 如果 result 的长度小于层数, 说明该层是第一次进入, 则在 result 中
加入一个新数组, 接着将结点的值加入到对应层的 result 数组中;
    """
    def levelOrder_v3(self, root: TreeNode) -> List[List[int]]:
        result = []
        # jy: 1 表示当前的层数(如果 root 为空, 则 _dfs 会直接返回, 不会在 result 中加入数值);
        self._dfs(root, 1, result)
        return result

    def _dfs(self, root: TreeNode, level: int, result: List[List[int]]) -> None:
        # jy: 如果 root 不存在, 则 return 终止;
        if not root:
            return
        # jy: 如果当前层数大于 result 的长度, 表示当前层初次进入 result, 应往 result 中加入 [],
        #    用以保存当前层元素;
        if level > len(result):
            result.append([])
        # jy: 将当前层元素加入 result 对应的层中(第 n 层在 result 中对应的下标为 n-1);
        result[level - 1].append(root.val)
        self._dfs(root.left, level + 1, result)
        self._dfs(root.right, level + 1, result)


ls_ = [3, 9, 20, None, None, 15, 7]
root = build_binary_tree(ls_)

res = Solution().levelOrder_v1(root)
print(res)

res = Solution().levelOrder_v2(root)
print(res)

res = Solution().levelOrder_v3(root)
print(res)


from collections import deque
def test(root):
    res = []
    queue_ = deque([root])
    while queue_:
        len_ = len(queue_)
        cur_level = []
        for _ in range(len_):
            cur_node = queue_.popleft()
            cur_level.append(cur_node.val)
            if cur_node.left:
                queue_.append(cur_node.left)
            if cur_node.right:
                queue_.append(cur_node.right)
        res.append(cur_level)
    print(res)
ls_ = [3, 9, 20, None, None, 15, 7]
root = build_binary_tree(ls_)
test(root)


