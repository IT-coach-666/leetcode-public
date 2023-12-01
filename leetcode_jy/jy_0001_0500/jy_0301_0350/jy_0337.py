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
title_jy = "House-Robber-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
The thief has found himself a new place for his thievery again. There is only one
entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the
smart thief realized that all houses in this place form a binary tree. It will
automatically contact the police if two directly-linked houses were broken into on
the same night.


Given the root of the binary tree, return the maximum amount of money the thief can
rob without alerting the police.



图见: https://www.yuque.com/frederick/dtwi9g/otpg45

Example 1:
Input: root = [3, 2, 3, null, 3, null, 1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: root = [3, 4, 5, 1, 3, null, 1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.



Constraints:
The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 104
"""



from typing import List
from about_TreeNode import *


class Solution:
    """
从根节点看, 分两种情况:
1) 抢劫根节点, 总收益为: 抢劫根节点收益 + 不抢劫左子树根节点收益 + 不抢劫右子树根节点收益
2) 不抢劫根节点, 总收益为: 抢劫左子树收益 + 抢劫右子树收益
    """
    def rob(self, root: TreeNode) -> int:
        return max(self._rob(root))


    def _rob(self, root: TreeNode) -> List[int]:
        if not root:
            return [0, 0]

        # jy: 对左子树进行抢劫, 得到的 left 为一个列表, left[0] 表示抢劫左子树根节点得
        #    到的收益, left[1] 表示不抢劫左子树根节点, 而是从其它节点开始抢劫得到的收
        #    益;
        left = self._rob(root.left)
        # jy: 同理以上 left;
        right = self._rob(root.right)
        # jy: 抢劫根节点, 总收益为: 抢劫根节点收益 + 不抢劫左子树根节点收益 + 不抢劫右子树根节点收益
        rob = root.val + left[1] + right[1]
        # jy: 不抢劫根节点, 总收益为: 抢劫左子树收益 + 抢劫右子树收益
        not_rob = max(left[0], left[1]) + max(right[0], right[1])

        # jy: 该方法返回一个列表, 第一个值表示抢劫当前 root 节点得到的收益, 第二个表示
        #    不抢劫当前节点得到的收益;
        return [rob, not_rob]



ls_ = [3, 2, 3, None, 3, None, 1]
root = build_binary_tree(ls_)
# Output: 7
res = Solution().rob(root)
print(res)


ls_ = [3, 4, 5, 1, 3, None, 1]
root = build_binary_tree(ls_)
# Output: 9
res = Solution().rob(root)
print(res)


