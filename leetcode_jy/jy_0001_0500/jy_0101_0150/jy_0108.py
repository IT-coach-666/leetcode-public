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
title_jy = "Convert-Sorted-Array-to-Binary-Search-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | IMP"


"""
Given an integer array `nums` where the elements are sorted in ascending
order, convert it to a height-balanced binary search tree.


Example 1:
Input: nums = [-10, -3, 0, 5, 9]
Output: [0, -3, 9, -10, null, 5]
Explanation: [0, -10, 5, null, -3, null, 9] is also accepted:
      0            0
     / \          / \
   -3   9       -10  5
   /   /          \   \
 -10  5           -3   9

Example 2:
Input: nums = [1, 3]
Output: [3, 1]
Explanation: [1, null, 3] and [3, 1] are both height-balanced BSTs.
   3     1
  /       \
 1         3


Constraints:
1) 1 <= nums.length <= 10^4
2) -10^4 <= nums[i] <= 10^4
3) `nums` is sorted in a strictly increasing order.
"""


from typing import List
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import serialize


class Solution:
    """
解法 1: 递归; 时间复杂度 O(n), 空间复杂度 O(n)

将数组的中间元素作为根节点, 中间元素的左侧元素构建左子树, 中间元素的右
侧元素构建右子树, 两边的高度差不超过 1 (左右子树均进行同样的递归调用)
    """
    def sortedArrayToBST_v1(self, nums: List[int]) -> TreeNode:
        return self._build_tree(nums, 0, len(nums)-1)

    def _build_tree(self, nums: List[int], low: int, high: int) -> TreeNode:
        """
        基于 nums 中的 [low, high] 下标范围构建平衡二叉搜索树
        """
        if low > high:
            return None

        # jy: 将数组中的中间元素作为根节点
        #middle = (low + high) // 2
        middle = low + (high - low) // 2
        root = TreeNode(nums[middle])

        # jy: 用数组中间元素的左边元素构建左子树
        root.left = self._build_tree(nums, low, middle-1)

        # jy: 用数组中间元素的右边元素构建右子树
        root.right = self._build_tree(nums, middle+1, high)
        return root


    """
解法 2: 递归的另一种写法
    """
    def sortedArrayToBST_v2(self, nums: List[int]) -> TreeNode:
        if not nums:
            return 

        mid = len(nums) // 2
        return TreeNode(nums[mid],
                        self.sortedArrayToBST(nums[ :mid]),
                        self.sortedArrayToBST(nums[mid + 1: ]))



nums = [-10, -3, 0, 5, 9]
res = Solution().sortedArrayToBST_v1(nums)
# jy: [0, -10, 5, None, -3, None, 9]
print(serialize(res))


nums = [1, 3]
res = Solution().sortedArrayToBST_v2(nums)
# jy: [1, None, 3]
print(serialize(res))

