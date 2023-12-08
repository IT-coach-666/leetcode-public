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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Count-of-Smaller-Numbers-After-Self(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an integer array nums and you have to return a new counts array. The
counts array has the property where counts[i] is the number of smaller elements to
the right of nums[i].


Example 1:
Input: nums = [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2:
Input: nums = [-1]
Output: [0]

Example 3:
Input: nums = [-1,-1]
Output: [0,0]


Constraints:
1<= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""


from typing import List

from about_TreeNode import TreeNode


class Solution:
    """
解法1(超时): 维护一个二叉搜索树, 树节点额外定义 count 属性表示左子树中节点(比当前节点
的值小)的个数, 从数组尾向前遍历数组, 依次向二叉搜索树中插入节点, 并更新 count 的数量;

超时: 因为当输入的数组是有序时, 二叉搜索树会退化为链表, 时间复杂度变为 O(n^2)
    """
    def countSmaller_v1(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        counts = [0]
        # jy: 以最后一个数值构建树节点;
        root = TreeNode(nums[-1])

        # jy: 从数组的倒数第二个元素反向遍历, 并基于相应数值构造树节点并插入二叉搜索树中;
        for i in range(len(nums)-2, -1, -1):
            # jy: 基于 nums[i] 构造树节点并插入二叉搜索树中, 并返回当前该节点的左子树节
            #    点个数;
            count = self._insert(root, nums[i])
            counts.append(count)

        # jy: 返回 counts 的反转结果;
        return list(reversed(counts))


    def _insert(self, root, value):
        # jy: 统计二叉搜索树中比 value 值小的节点的个数;
        count = 0
        prev, current = None, root

        while current:
            prev = current
            # jy: 如果当前节点的值小于 value, 则 count 基于当前节点的 count 属性值(该属
            #    性值表示比当前节点值小的节点的个数, 即其左子树的节点个数)的基础上加 1,
            #    并将当前节点切换到其右子树(因为左子树已经统计完成了), 继续循环统计;
            if current.val < value:
                count += current.count + 1
                current = current.right
            # jy: 如果当前节点值大于 value, 表明如果当 value 值对应的节点加入到二叉搜索
            #    树后, 比当前节点对应的值小的节点个数又多了1个, 因此当前节点的 count 属
            #    性值加 1; 并将当前节点更新为其左子节点(因为目标是为了找出小于 value 的
            #    节点的个数, 如果当前节点值大于 value, 则只有其左子树可能存在小于 value
            #    的节点);
            else:
                current.count += 1
                current = current.left
        # jy: 经过以上循环, 最后的 prev 节点为 value 值对应的节点的父节点(会依据 value 值
        #    不断在已有二叉搜索树中判断该值应该插入的位置);
        if prev.value < value:
            prev.right = TreeNode(value)
        else:
            prev.left = TreeNode(value)
        # jy: 最后返回比当前 value 值对应节点小的节点的个数;
        return count



    """
解法2: 借鉴归并排序的思想, 使用归并排序将数组从大到小排序, 排序时需要带上数字在数组中
的位置, 在合并时, 由于左右两部分都是排好序的, 如果当前左半部分的数大于当前右半部分的
数, 则更新比左半部分的数小的个数;

jy: 分治算法
    """
    def countSmaller_v2(self, nums: List[int]) -> List[int]:
        # jy: 将结果列表值均初始化为 0;
        result = [0] * len(nums)
        # jy: 分治算法求解, 会对 result 进行更新;
        self._divide(list(enumerate(nums)), result)
        # jy: 返回最终结果;
        return result


    def _divide(self, nums, result):
        if len(nums) <= 1:
            return nums

        middle = len(nums) // 2
        # jy: left 和 right 均为递归调用 _divide 方法的结果, 返回的结果为 _conquer 方法
        #    的返回结果, 为一个二维数组;
        left = self._divide(nums[:middle], result)
        right = self._divide(nums[middle:], result)

        return self._conquer(left, right, result)


    def _conquer(self, left, right, result):
        sorted_nums = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][1] > right[j][1]:
                sorted_nums.append(left[i])
                result[left[i][0]] += len(right) - j
                i += 1
            else:
                sorted_nums.append(right[j])
                j += 1

                i += 1
            else:
                sorted_nums.append(right[j])
                j += 1

        sorted_nums.extend(left[i:] or right[j:])

        return sorted_nums

nums = [5, 2, 6, 1]
# Output: [2, 1, 1, 0]
res = Solution().countSmaller_v1(nums)
print(res)


nums = [-1]
# Output: [0]
res = Solution().countSmaller_v2(nums)
print(res)


nums = [-1, -1]


