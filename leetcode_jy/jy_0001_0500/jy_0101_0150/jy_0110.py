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
from typing import List, Dict, Optional
# jy: 记录该题的难度系数
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Balanced-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 + 优化技巧 | IMP"


"""
Given a binary tree, determine if it is height-balanced.


Example 1:
Input: root = [3, 9, 20, null, null, 15, 7]
               3
              / \
             9   20
                /  \
               15  17
Output: true

Example 2:
Input: root = [1, 2, 2, 3, 3, null, null, 4, 4]
               1
              / \
             2   2
            / \ 
           3   3 
          / \
         4   4
Output: false

Example 3:
Input: root = []
Output: true


Constraints:
1) The number of nodes in the tree is in the range [0, 5000].
2) -10^4 <= Node.val <= 10^4
"""


from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree


class Solution:
    """
解法 1: 递归遍历每个节点判断左右子树的高度差是否不超过 1

时间复杂度 O(N log⁡): 最差情况下 (为 "满二叉树" 时), 遍历树所有节点, 判断每
个节点的深度 (高度) 需遍历各子树的所有节点
1) 满二叉树高度的复杂度 O(logN), 将满二叉树按层分为 log(N+1) 层
2) 通过调用 _get_height(root), 判断二叉树各层的节点的对应子树的深度, 需遍
   历节点数量为 N * 1, (N - 1) / 2 * 2, (N - 3) / 4 * 4, (N - 7) / 8 * 8, ..., 1 * (N + 1) / 2
   因此各层执行 _get_height(root) 的时间复杂度为 O(N) (每层开始, 最多遍
   历 N 个节点, 最少遍历 (N + 1) / 2 个节点

   (N - 3) / 4 * 4 代表从此层开始总共需遍历 N - 3 个节点, 此层共有 4 个节
   点, 因此每个子树需遍历 (N - 3) / 4 个节点

   因此, 总体时间复杂度 = 每层执行复杂度 * 层数复杂度 = O(N * log⁡)

空间复杂度 O(N): 最差情况下 (树退化为链表时), 系统递归需要使用 O(N) 的栈空间
    """
    def isBalanced_v1(self, root: TreeNode) -> bool:
        """
        判断以 root 为根节点的树是否是平衡的二叉树
        """
        # jy: 如果当前节点为空 (表明能走到当前空节点, 且之前的节点均是满足
        #     平衡要求的), 直接返回 True
        if not root:
            return True

        # jy: 获取左右子树的高度
        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)
        # jy: 如果左右子树的高度差不大于 1, 且递归判断左子树和右子树也是平
        #     衡的二叉树, 则返回 True
        return abs(left_height - right_height) <= 1 and \
               self.isBalanced_v1(root.left) and \
               self.isBalanced_v1(root.right)

    def _get_height(self, root):
        """
        获取以 root 为根节点的树的高度 (递归实现)
        """
        if not root:
            return 0
        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)
        return max(left_height, right_height) + 1


    """
解法 2: 优化解法 1

解法 1 判断每个子树的高度时存在重复计算, 可以在递归判断树高度的同时判断是
否平衡, 因为计算树的高度为深度优先搜索, 可同时判断局部二叉树是否平衡, 只
要出现不平衡, 则无需再计算子树的高度
    """
    def isBalanced_v2(self, root: TreeNode) -> bool:
        return self._is_balanced(root)[1]

    def _is_balanced(self, root):
        """
        判断以 root 为根节点的树是否是平衡二叉树, 并返回该树的高度
        """
        if not root:
            return 0, True

        # jy: 递归判断左子树是否是平衡二叉树; 当子树为非平衡二叉树时, 会直
        #     接返回 False, 经过层层递归返回, 该 False 即为最终返回结果
        left_height, balanced = self._is_balanced(root.left)
        if not balanced:
            # jy: 左子树高度的返回仅仅是为了确保该递归函数完整, 当 balanced
            #     为 False 时, 返回的 left_height 数值是多少已经不重要, 因为
            #     后续不会再用到了, 因此返回的高度可替换为任意数值
            #return left_height, balanced
            return -1, False

        # jy: 递归判断右子树是否是平衡二叉树; 当子树为非平衡二叉树时, 会直
        #     接返回 False, 经过层层递归返回, 该 False 即为最终返回结果
        right_height, balanced = self._is_balanced(root.right)
        if not balanced:
            #return right_height, balanced
            return -1, False

        # jy: 执行到此处时, 表明 root 的左子树和右子树均为平衡二叉树, 但并
        #     不代表以 root 为根节点的树为平衡二叉树: 当左子树和右子树的高
        #     度差大于 1 时表明以 root 为根节点的树不是平衡二叉树, 直接返
        #     回 False (返回的高度值随意设定即可, 因为后续不会再使用到)
        if abs(left_height - right_height) > 1:
            return -1, False

        # jy: 执行到此处时, 表明以 root 为根节点的树为平衡二叉树, 计算该树
        #     的高度后返回
        height = max(left_height, right_height) + 1
        return height, True


    """
解法 3: 递归 + 剪枝

时间复杂度 O(N): N 为树的节点数; 最差情况下需要递归遍历树的所有节点
空间复杂度 O(N): 最差情况下 (树退化为链表时), 系统递归需要使用 O(N) 的栈空间
    """
    def isBalanced_v3(self, root: Optional[TreeNode]) -> bool:

        def recur(root):
            """
            统计树的高度, 如果发现不是平衡二叉树, 则高度返回 -1, 提前终止
            """
            if not root:
                return 0

            left = recur(root.left)
            if left == -1:
                return -1

            right = recur(root.right)
            if right == -1:
                return -1

            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1



ls_ = [3, 9, 20, None, None, 15, 7]
root = build_binary_tree(ls_)
# Output: true
res = Solution().isBalanced_v1(root)
print(res)


ls_ = [1, 2, 2, 3, 3, None, None, 4, 4]
root = build_binary_tree(ls_)
# Output: false
res = Solution().isBalanced_v2(root)
print(res)


ls_ = []
root = build_binary_tree(ls_)
# Output: true
res = Solution().isBalanced_v1(root)
print(res)


