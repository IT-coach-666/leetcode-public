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
title_jy = "Path-Sum-III(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the root of a binary tree and an integer ``targetSum``, return the number of paths
where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards
(i.e., traveling only from parent nodes to child nodes).


Example 1:   https://www.yuque.com/frederick/dtwi9g/qydsz8
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3


Constraints:
The number of nodes in the tree is in the range [0, 1000].
-10^9 <= Node.val <= 10^9
-1000 <= targetSum <= 1000
"""


from about_TreeNode import *


class Solution:
    """
类似 001_Two-Sum.py, 使用 Map 保存树遍历过程中至今的数字之和及其出现的次数的映射, 当遇到
某个节点时, 如果至今的和减去 targetSum 在 Map 中, 说明在根节点和当前节点之间存在某个节点,
该节点到当前节点的和等于 targetSum; 同时递归判断左右子树中是否存在满足条件的路径, 最后的
总路径数等于以下路径之和:
1) 以当前节点结尾的路径
2) 左子树下的路径
3) 右子树下的路径
    """
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # jy: 初始化至今的树节点和为 0 的个数为 1, 使得当后续计算至今树节点的和减去 targetSum 为
        #    0 时, 在 Map 中找到其对应的出现次数为至少是 1 (如果后续遍历中有其它至今为止的树节
        #    点和为 0, 则该值大于 1), 即这种情况下至少根节点到当前节点的路径和是满足条件的(根节
        #    点到当前节点的路径之和减去 targetSum 为 0)
        sums = {0: 1}

        return self._dfs(root, 0, targetSum, sums)


    def _dfs(self, root, sum_so_far, target, sums):
        if not root:
            return 0
        # jy: 统计截止当前节点为止的路径和;
        sum_so_far += root.val

        # jy: 获取根节点到当前节点的和减去 targetSum 的值在 sums 中出现的次数;
        count_ended_at_root = sums.get(sum_so_far - target, 0)
        # jy: 更新截止当前节点为止的路径和的出现次数;
        sums[sum_so_far] = sums.get(sum_so_far, 0) + 1

        count_in_left = self._dfs(root.left, sum_so_far, target, sums)
        # print("sum_so_far-left ==== ", sum_so_far, " === ", count_in_left, " ==== sums: ", sums)
        count_in_right = self._dfs(root.right, sum_so_far, target, sums)
        # print("sum_so_far-right ==== ", sum_so_far, " === ", count_in_right, " ==== sums: ", sums)
        # jy: 该回溯操作对当前最外层的计算没有影响, 其主要作用是隔离左右子树的影响, 如用以下树举例:
        #    当递归完左子树时, sums 为: {0: 1, 1: 1, -1: 1}, 此时的 {-1: 1} 是在左子树中产生, 该值
        #    不能直接应用于右子树中查询, 因为左右子树不在一个路径上; 如果少了以下回溯操作, 则右子树
        #    中也能使用该条件, 当右子树遍历到 -3 时, 截止当前值为 -2, 减去目标值 -1 后为 -1, 在 sums
        #    中查找 {-1: 1}, 然而其不是右子树路径产生的;
        '''
        root:      targetSum = -1
            1
           / \
         -2   -3
        '''
        sums[sum_so_far] = sums[sum_so_far] - 1

        return count_ended_at_root + count_in_left + count_in_right


"""   """
ls_ = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
root = build_binary_tree(ls_)
targetSum = 8
# Output: 3
res = Solution().pathSum(root, targetSum)
print(res)


ls_ = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
root = build_binary_tree(ls_)
targetSum = 22
# Output: 3
res = Solution().pathSum(root, targetSum)
print(res)


ls_ = [1, -2, -3]
root = build_binary_tree(ls_)
targetSum = -1
# Output: 1
res = Solution().pathSum(root, targetSum)
print(res)


