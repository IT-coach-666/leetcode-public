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
title_jy = "Path-Sum-IV(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
If the depth of a tree is smaller than 5, then this tree can be represented by an array of
three-digit integers. For each integer in this array:
1) The hundreds digit represents the depth d of this node where 1 <= d <= 4.
2) The tens digit represents the position p of this node in the level it belongs to
   where 1 <= p <= 8. The position is the same as that in a full binary tree.
3) The units digit represents the value v of this node where 0 <= v <= 9.

Given an array of ascending three-digit integers nums representing a binary tree with a
depth smaller than 5, return the sum of all paths from the root towards the leaves.

It is guaranteed that the given array represents a valid connected binary tree.


Example 1:  (图: https://www.yuque.com/frederick/dtwi9g/dbk03r)
Input: nums = [113,215,221]
Output: 12
Explanation: The tree that the list represents is shown.
The path sum is (3 + 5) + (3 + 1) = 12.

Example 2:
Input: nums = [113,221]
Output: 4
Explanation: The tree that the list represents is shown.
The path sum is (3 + 1) = 4.


Constraints:
1 <= nums.length <= 15
110 <= nums[i] <= 489
nums represents a valid binary tree with depth less than 5.
"""


from typing import List
from collections import deque


class Solution:
    """
解法1: 使用 Map 保存树的节点, "深度+位置" 即可定位一个树的节点, 即使用数组中数字的前两位, 递归
遍历左右子树的路径和;
    """
    def pathSum_v1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # jy: 字典的 key 为 "深度+位置" 代表的数值(使用 "深度+位置" 即可定位节点), value 为节点值;
        nodes = {}
        for n in nums:
            nodes[n // 10] = n % 10
        # jy: nums[0] 为根节点对应的三位数值, 取该值的前两位(即 "深度+位置")即可从 nodes 中获取该节点值;
        return self._dfs(nums[0] // 10, 0, nodes)

    def _dfs(self, root, sum_so_far, nodes):
        # jy: 如果 "深度+位置" 所代表的节点不在 modes 中(即该节点不存在), 则终止递归;
        if root not in nodes:
            return 0
        # jy: 获取 "深度" depth
        depth = root // 10
        # jy: 获取 "位置" position
        position = root % 10
        # jy: 计算当前节点左子节点对应的 "深度+位置" 所对应的值;
        left = (depth + 1) * 10 + position * 2 - 1
        # jy: 当前节点右子节点所对应的 "深度+位置" 值为左子节点对应的值加 1;
        right = left + 1
        # jy: 加上当前节点对应的值;
        sum_so_far += nodes.get(root, 0)

        # jy: 如果当前节点的左子节点和右子节点均不存在, 则返回 sum_so_far, 终止递归;
        if left not in nodes and right not in nodes:
            return sum_so_far

        # jy: 如果左子节点和右子节点(即与当前节点相连的节点, 属于 path 中的一部分, 递归完
        #    之后就计算整个 path)中至少有一个存在, 则继续递归求解;  sum_so_far 表示的是
        #    从根节点到当前节点的路径的节点值之和;
        return self._dfs(left, sum_so_far, nodes) + self._dfs(right, sum_so_far, nodes)

    """
解法2: 使用栈的深度优先搜索;
    """
    def pathSum_v2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nodes = {}
        sums = []
        # jy: 将根节点的 "深度+位置" 以元组方式入栈: ("深度+位置", sum_so_far)
        stack = [(nums[0] // 10, 0)]
        # jy: nodes 字典的 key 为 "深度+位置" 代表的数值(使用 "深度+位置" 即可定位节点), value 为节点值;
        for n in nums:
            nodes[n // 10] = n % 10

        while stack:
            # jy: 出栈, 依据 "深度+位置" 获取深度和位置, 并计算左右子节点的 "深度+位置" 值;
            node, sum_so_far = stack.pop()
            depth = node // 10
            position = node % 10
            left = (depth + 1) * 10 + position * 2 - 1
            right = left + 1
            # jy: 将当前出栈节点的值加到 sum_so_far 上;
            sum_so_far += nodes.get(node, 0)
            # jy: 如果左右子节点均不存在, 则表明当前即为叶子节点, 即已经遍历得到一个完整路径, 将
            #    sum_so_far 加入 sums 中;
            if left not in nodes and right not in nodes:
                sums.append(sum_so_far)
            # jy: 如果左子节点存在, 则将其以及根节点到该左子节点的路径和(该左子节点的值暂未加
            #    上, 该节点出栈时即加上) 以及该左子节点的 "深度+位置" 值所对应的元组入栈;
            if left in nodes:
                stack.append((left, sum_so_far))
            # jy: 与左子节点同理(右子节点是后入栈, 会先出栈遍历);
            if right in nodes:
                stack.append((right, sum_so_far))

        return sum(sums)

    """
解法3: 使用队列的广度优先搜索;
    """
    def pathSum_v3(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nodes = {}
        sums = []
        # jy: 将根节点的 "深度+位置" 以元组方式入队: ("深度+位置", sum_so_far)
        #     逻辑类似栈深度优先搜索, 只不过队列是先进先出, 每次遍历均辉将左右
        #     子节点右侧入队(如果节点存在), 而每次左侧出队总是会把同一层的节点
        #     先出完, 并把该层节点的下一层节点入队, 故是广度优先搜索;
        queue = deque([(nums[0] // 10, 0)])

        for n in nums:
            nodes[n // 10] = n % 10

        while queue:
            node, sum_so_far = queue.popleft()
            depth = node // 10
            position = node % 10
            left = (depth + 1) * 10 + position * 2 - 1
            right = left + 1
            sum_so_far += nodes.get(node, 0)

            if left not in nodes and right not in nodes:
                sums.append(sum_so_far)

            if left in nodes:
                queue.append((left, sum_so_far))

            if right in nodes:
                queue.append((right, sum_so_far))

        return sum(sums)


nums = [113, 215, 221]
# Output: 12
res = Solution().pathSum_v1(nums)
print(res)

nums = [113, 221]
# Output: 4
res = Solution().pathSum_v2(nums)
print(res)

nums = [113, 221]
# Output: 4
res = Solution().pathSum_v3(nums)
print(res)



