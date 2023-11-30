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
title_jy = "Unique-Binary-Search-Trees-II(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.


Example 1:   https://www.yuque.com/frederick/dtwi9g/agyptu
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]


Constraints:
1 <= n <= 8
"""


from typing import List
from about_TreeNode import *


class Solution:
    """
在 096_Unique-Binary-Search-Trees.py 的思想上, 分别递归求解左右子树的组合方式, 然后
根据左右子树的乘积构造整个树的组合方式
    """
    def generateTrees(self, n: int) -> List[TreeNode]:
        # jy: 生成节点值为 1 到 n 的结构不同的所有二叉搜索树;
        return self._generate_trees(1, n)

    def _generate_trees(self, low, high):
        # jy: 如果 low 大于 high, 则终止递归, 返回包含一个 None 值的列表(使得后续如果是
        #    左子树得到该值, 则左子树对应的值为 None, 如果是右子树得到该值, 则右子树对
        #    应的值为 None, 且不因为值为 None 而直接忽略另一子树, for 循环中仍会遍历该
        #    None 值);
        if low > high:
            return [None]
        # jy: nodes 列表用于存放每棵树的根节点;
        nodes = []
        # jy: 从 low 到 high 遍历, 将每次遍历结果当做当前树的根节点值; 并依据比当前值 i 小
        #    的值(即 low 到 i-1)构造左子树(二叉搜索树), 将所有不同形状的左子树的根节点均
        #    加入到 left_nodes 列表中; 同理, 依据比当前 i 值大的值(即 i+1 到 high)构造右子
        #    树(二叉搜索树), 将所有不同形状的右子树的根节点均加入到 right_nodes 中; 随后
        #    根据 left_nodes 中的所有左子树根节点和 right_nodes 中的所有右子树根节点构造
        #    已当前 i 节点值为根节点的树, 并加入到 nodes 中, 最终返回;
        # jy: 注意, 如果递归调用当前方法时传入的 low 等于 high, 即表示构造当前树只有一个节
        #    点, 此时得到的 left_nodes 和 right_nodes 均为 [None], 且外循环只会循环一次,
        #    内 for 循环会依据当前的唯一节点构造树, 且其左右子树均为 None, 并将构造的树的
        #    根节点加入到 nodes 中最终返回; 如果递归调用时 low 和 high 范围共有两个值(以
        #    [1, 2] 为例进行思考), 则会求得两个节点所组成的二叉搜索树的所有情况, 并将二叉
        #    搜索树的根节点加入到 nodes 中并返回(外 for 循环共循环两次, 每次循环都至少会构
        #    造出一个二叉搜索树);
        for i in range(low, high + 1):
            left_nodes = self._generate_trees(low, i-1)
            right_nodes = self._generate_trees(i+1, high)

            for left in left_nodes:
                for right in right_nodes:
                    nodes.append(TreeNode(i, left, right))

        return nodes


n = 3
# Output: [
# [1,null,2,null,3],
# [1,null,3,2],
# [2,1,3],
# [3,1,null,null,2],
# [3,2,null,1]]
res = Solution().generateTrees(n)
# print(res)
for tree_i in res:
    print(serialize(tree_i))


n = 1
# Output: [[1]]
res = Solution().generateTrees(n)
for tree_i in res:
    print(serialize(tree_i))


