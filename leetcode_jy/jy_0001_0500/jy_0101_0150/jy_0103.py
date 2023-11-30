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
tag_jy = ""


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



from typing import List
from collections import deque
from about_TreeNode import *


class Solution:
    """
解法1: 使用两个双向队列 A (代表奇数层) 和 B (代表偶数层), 队列 A 从队首出队并将子结
点从左往右放入队列 B 尾端, 队列 B 从队尾出队并将子节点从右往左放入队列 A 头部;
    """
    def zigzagLevelOrder_v1(self, root: TreeNode) -> List[List[int]]:
        # jy: 统计当前层;
        depth = 0
        levels = []
        # jy: 存放奇数层对应的节点值;
        queue1 = deque([root]) if root else deque()
        # jy: 存放偶数层对应的节点值;
        queue2 = deque()
        # jy: 当两个双向队列均为空时, 遍历结束, 退出循环;
        while queue1 or queue2:
            # jy: 进行第一轮循环时, depth 为 1, 表示当前为第 1 层;
            depth += 1
            level = []
            # jy: 判断当前是否是奇数层;
            is_odd = depth & 1 == 1
            # jy: 如果是奇数层, 则遍历 queue1 队列, 该队列的长度即该奇数层的元素个数;
            if is_odd:
                for _ in range(len(queue1)):
                    # jy: 奇数层时, 从 queue1 队列左侧出元素;
                    node = queue1.popleft()
                    level.append(node.val)
                    # jy: 奇数层时, 将该层节点的左右子节点(属于偶数层)加入 queue2 队列末
                    #    尾(先加左子节点, 再加右子节点);
                    if node.left:
                        queue2.append(node.left)
                    if node.right:
                        queue2.append(node.right)
            # jy: 如果是偶数层, 则遍历 queue2 队列, 该队列的长度即该偶数层元素的个数;
            else:
                for _ in range(len(queue2)):
                    # jy: 偶数层时, 从 queue2 队列右侧出元素(由于入队列时是加入队列末尾, 且
                    #    是先加入左节点, 后加入右节点, 则右侧出元素时即原树结构中对应层的从
                    #    右到左元素值);
                    node = queue2.pop()
                    level.append(node.val)
                    # jy: 此时再将当前节点的左右子节点(属于奇数层)加入 queue1 队列头(即队列
                    #    左侧, 先加右节点, 再加左节点); 由于 queue2 遍历时对应偶数层的右节点
                    #    到左节点的遍历, 此时往 queue1 中先加右子节点再加左子节点时, 即可使
                    #    得加到最后, queue1 的最左侧为其对应的树结构的奇数层的左边第一个节点;
                    #    当从 queue1 左侧不断出元素时, 即树结构中奇数层的从左到右的结果;
                    if node.right:
                        queue1.appendleft(node.right)
                    if node.left:
                        queue1.appendleft(node.left)
            levels.append(level)
        return levels



    """
解法2: 将解法 1 简化为使用一个双端队列;

在 102_Binary-Tree-Level-Order-Traversal.py 中的解法 2 的基础上增加一个统计层次的变
量, 当为基数层时, 队列左侧出, 右侧进(先左节点后右节点); 当为偶数层时, 队列右侧出, 左
侧进(先右节点后左节点);
    """
    def zigzagLevelOrder_v2(self, root: TreeNode) -> List[List[int]]:
        # jy: 定义一个变量统计当前层数;
        depth = 0
        levels = []
        queue = deque([root]) if root else deque()
        while queue:
            # jy: 第一遍循环即 depth 为 1, 表示第一层;
            depth += 1
            level = []
            # jy: 判断该层是否为基数层;
            is_odd = depth & 1 == 1
            # jy: 一次 for 循环即遍历 queue 中的一层(每次开始 for 循环时, queue 中保留了当前
            #    层的所有元素, 循环过程中会不断从队列中出元素, 并同时在队列中加入元素, 该过
            #    程不影响当前 for 循环的次数, 即不影响 len(queue), 只有当当前循环结束后, 该
            #    值才会得到更新, 即更新为下一层的元素个数);
            for _ in range(len(queue)):
                # jy: 如果为奇数层, 则从队列左侧出元素(以下奇数层时从队列右侧先加左节点再加右
                #    节点, 结合此处左侧出元素即可使得对应层的元素是原先树结构对应层中的从左到
                #    右节点的值); 否则从队列右侧出元素(以下偶数层时从队列左侧先加右节点再加左
                #    节点, 结合此处右侧出元素即可使得对应层的元素是原先树结构对应层中的从右到
                #    左节点的值)【trick】;
                node = queue.popleft() if is_odd else queue.pop()
                # jy: 将从队列中出来的元素放入到当前层中;
                level.append(node.val)
                # jy: 如果是奇数层, 则队尾(队列右侧)中先加入左节点, 后加入右节点, 使得当从左
                #    侧出元素时, 对应层的元素是原先树结构对应层中的从左到右节点的值;
                if is_odd:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                # jy: 如果是偶数层, 则在队头(队列左侧)中先加入右节点, 后加入左节点, 使得当从
                #    右侧出元素时, 对应层的元素是原先树结构对应层中的从右到左节点的值;
                else:
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
            # jy: 一次 for 循环结束后, level 中的值即为当前层的结果, 将其加入 levels 中;
            levels.append(level)
        return levels


    """
解法3: 遍历每一层的结点时, 事先初始化一个数组, 如果是从左往右遍历, 则从数组头开
始向右加入元素, 反之则从数组尾向左加入元素;
    """
    def zigzagLevelOrder_v3(self, root: TreeNode) -> List[List[int]]:
        queue = deque([root]) if root else deque()
        levels = []
        # jy: 统计当前的层数;
        depth = 0
        while queue:
            depth += 1
            # jy: 判断是否是奇数层;
            is_odd = depth & 1 == 1
            # jy: 统计当前层有多少个元素
            length = len(queue)
            # jy: 先初始化当前层的所有元素值为 0;
            level = [0] * length
            for i in range(length):
                # jy: 从队列左侧出元素;
                node = queue.popleft()
                # jy: 如果是奇数层, 将该层的元素(已为树结构的对应层的从左到右遍历结果)从前往后填
                #    充到 level 中;
                if is_odd:
                    level[i] = node.val
                # jy: 如果是偶数层, 将该层的元素(已为树结构的对应层的从左到右遍历结果)从后往前填
                #    充到 level 中;
                else:
                    level[length - i-1] = node.val
                # jy: 随后将当前节点的左右子节点添加到 queue 中, 即将进入下一轮 while 循环;
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # jy: 一轮 for 循环完成后, 即一层遍历完成, 将其添加到 levels 中;
            levels.append(level)
        return levels


    """
解法4: 深度优先搜索, 在 102_Binary-Tree-Level-Order-Traversal.py 的解法 3 的基础上
判断当前层的是奇数层还是偶数层, 如果是奇数层, 则从层数组的末尾插入, 否则从层数组头插入;
    """
    def zigzagLevelOrder_v4(self, root: TreeNode) -> List[List[int]]:
        result = []
        self._dfs(root, 1, result)
        return result

    def _dfs(self, root: TreeNode, level: int, result: List[List[int]]) -> None:
        if not root:
            return

        if level > len(result):
            result.append([])
        # jy: 如果是基数层, 则从数组尾插入; 否则从数组头插入;
        if level & 1 == 1:
            result[level-1].append(root.val)
        else:
            result[level-1].insert(0, root.val)

        self._dfs(root.left, level + 1, result)
        self._dfs(root.right, level + 1, result)


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


