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
title_jy = "Symmetric-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 栈/队列 + 循环"


"""
Given the root of a binary tree, check whether it is a mirror of itself 
(i.e. symmetric around its center).


Example 1: 图示参考: https://www.yuque.com/it-coach/leetcode/pgvb5ui8ag9vuzxo
Input: root = [1, 2, 2, 3, 4, 4, 3]
Output: true

Example 2:
Input: root = [1, 2, 2, null, 3, null, 3]
Output: false


Constraints:
1) The number of nodes in the tree is in the range [1, 1000].
2) -100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?
"""


from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from collections import deque


class Solution:
    """
解法 1: 递归

对左右子树分别以 "根节点-左节点-右节点" 和 "根节点-右节点-左节点" 的顺序进行
遍历, 最后判断两个子树遍历后对数组是否相等
    """
    def isSymmetric_v1(self, root: TreeNode) -> bool:
        ls_left = []
        ls_right = []
        # jy: 对左子树按 "根节点-左节点-右节点" 的顺序递归遍历
        self._root_left_right(root.left, ls_left)
        # jy: 对右子树按 "根节点-右节点-左节点" 的顺序递归遍历
        self._root_right_left(root.right, ls_right)

        # jy: 得到的节点列表不相同, 则表明非对称
        if ls_left != ls_right:
            return False

        return True

    def _root_left_right(self, root, ls_):
        # jy: 注意: 遍历时如果节点为空, 也要往列表中加入 None 值,
        #     因为遍历时总是先遍历根节点, 再遍历子节点, 如果子节点
        #     为 None 时不加入列表结果中 (_root_right_left 遍历方
        #     式也保持同步, 即为 None 时也不加入列表结果), 则如果
        #     左右子树对应的子树如果节点均在同一侧节点(不对称), 但
        #     由于没有 None 作为占位符, 无法判断其真正对称与否
        if not root:
            ls_.append(None)
            return

        ls_.append(root.val)
        self._root_left_right(root.left, ls_)
        self._root_left_right(root.right, ls_)

    def _root_right_left(self, root, ls_):
        if not root:
            ls_.append(None)
            return
        ls_.append(root.val)
        self._root_right_left(root.right, ls_)
        self._root_right_left(root.left, ls_)


    """
解法 2: 非递归实现解法 1 的逻辑 (广度优先搜索, 基于队列)
    """
    def isSymmetric_v2(self, root: TreeNode) -> bool:
        if not root:
            return True

        # jy: 先将左右子树的根节点加入队列中
        q_root_left_right = deque([root.left])
        q_root_right_left = deque([root.right])

        # jy: 如果两个队列均不为空 (每次循环均会确保两个队列的长度相等,
        #     因此实际上判断其中一个队列不为空即可)
        while q_root_left_right and q_root_right_left:
            # jy: 两个队列均左侧出队元素 (确保总是先进先出)
            left = q_root_left_right.popleft()
            right = q_root_right_left.popleft()
            # jy: 如果两个队列出队的元素均为 None, 则跳过直接进行下一轮出队
            if left is None and right is None:
                continue
            # jy: 如果两个队列出队的元素均不为 None, 则判断节点值是否相等,
            #     不相等则返回 False, 否则将 left 节点的左子节点和右子节点
            #     依次入 q_root_left_right 队列; 将 right 节点的右子节点和
            #     左子节点依次入队
            elif left and right:
                if left.val != right.val:
                    return False
                # jy: 注意: 入队的是节点, 而不是节点值, 因为后续还需要依据
                #     出队节点继续遍历相应的子节点
                q_root_left_right.append(left.left)
                q_root_left_right.append(left.right)
                q_root_right_left.append(right.right)
                q_root_right_left.append(right.left)
            # jy: 如果出队节点值有一个为 None 而另一个不为 None, 则返回 False
            else:
                return False

        return True


    """
解法 3: 递归判断左子树是否和右子树镜像
    """
    def isSymmetric_v3(self, root: TreeNode) -> bool:
        return not root or self._is_symmetric(root.left, root.right)

    def _is_symmetric(self, left, right):
        # jy: 如果有一个节点为 None, 则只有两个均为 None 时才返
        #     回的是 True
        if left is None or right is None:
            return left is None and right is None

        # jy: 如果两个节点均非 None, 则节点值不等时直接返回 False
        if left.val != right.val:
            return False

        return self._is_symmetric(left.left, right.right) and \
               self._is_symmetric(left.right, right.left)


    """
解法 4: 类似解法 2 (基于栈实现深度优先搜索, 不要求先进先出, 而是后进先出)
    """
    def isSymmetric_v4(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack1 = [root.left]
        stack2 = [root.right]

        while stack1 and stack2:
            left = stack1.pop()
            right = stack2.pop()

            if left is None and right is None:
                continue
            elif left and right:
                if left.val != right.val:
                    return False

                stack1.append(left.left)
                stack1.append(left.right)
                stack2.append(right.right)
                stack2.append(right.left)
            else:
                return False

        return True


ls_ = [1, 2, 2, 3, 4, 4, 3]
root = build_binary_tree(ls_)
res = Solution().isSymmetric_v1(root)
# jy: true
print(res)


ls_ = [1, 2, 2, None, 3, None, 3]
root = build_binary_tree(ls_)
res = Solution().isSymmetric_v2(root)
# jy: false
print(res)


ls_ = [1, 2, 2, 3, 4, 4, 3]
root = build_binary_tree(ls_)
res = Solution().isSymmetric_v3(root)
# jy: true
print(res)


ls_ = [1, 2, 2, None, 3, None, 3]
root = build_binary_tree(ls_)
res = Solution().isSymmetric_v4(root)
# jy: false
print(res)


