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
title_jy = "Convert-Sorted-List-to-Binary-Search-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given the head of a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST. For this problem, a height-balanced binary tree
is defined as a binary tree in which the depth of the two subtrees of every node
never differ by more than 1.


Example 1:    https://www.yuque.com/frederick/dtwi9g/ap3tpm
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [0]
Output: [0]

Example 4:
Input: head = [1,3]
Output: [3,1]


Constraints:
The number of nodes in head is in the range [0, 2 * 10^4].
-10^5 <= Node.val <= 10^5
"""


from about_ListNode import *
from about_TreeNode import *


class Solution:
    """
先将列表转为有序数组, 则题目变为 108_Convert-Sorted-Array-to-Binary-Search-Tree.py
    """
    def sortedListToBST_v1(self, head: ListNode) -> TreeNode:
        values = self._get_sorted_array(head)
        return self._convert_sorted_array_to_bst(values, 0, len(values) - 1)

    def _get_sorted_array(self, head):
        """
        将有序链表节点值存储到一个数组, 形成有序数组
        """
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def _convert_sorted_array_to_bst(self, values, low, high):
        """
        基于有序数组递归构造平衡二叉搜索树
        """
        # jy: 如果 low 大于 high, 则直接返回 None, 终止递归;
        if low > high:
            return None

        middle = low + (high - low) // 2
        root = TreeNode(values[middle])
        root.left = self._convert_sorted_array_to_bst(values, low, middle - 1)
        root.right = self._convert_sorted_array_to_bst(values, middle + 1, high)
        return root

    """
解法2: 和解法 1 的思想类似, 不过巧妙的使用了快慢指针来定位根节点(对应解法 1 中的 middle)
    """
    def sortedListToBST_v2(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        return self._sorted_list_to_bst(head, None)

    def _sorted_list_to_bst(self, head, tail):
        if head is tail:
            return None
        # jy: 初始化快慢指针, 均指向头节点;
        slow, fast = head, head
        # jy: 每次循环快指针走两步, 慢指针走一步, 当 fast 或 fast.next 指针为末尾节点时
        #    (用 tail 参数表示, 方便后续递归调用; 初始化时为 None), 此时的 slow 即为 middle
        #    节点, 即平衡二叉搜索树的根节点;
        #    (链表为奇数长度时 slow 为中点，偶数长度时 slow 为下中点; 将 fast 的初始值修改为
        #     head.next 即可使得链表为偶数长度时 slow 为上中点, 将上中点作为树的根节点也符合
        #     要求)
        while fast is not tail and fast.next is not tail:
            fast = fast.next.next
            slow = slow.next

        root = TreeNode(slow.val)
        root.left = self._sorted_list_to_bst(head, slow)
        root.right = self._sorted_list_to_bst(slow.next, tail)

        return root


ls_ = [-10, -3, 0, 5, 9]
head = getListNodeFromList(ls_)
# Output: [0,-3,9,-10,null,5]
res = Solution().sortedListToBST_v1(head)
print(serialize(res))

ls_ = []
head = getListNodeFromList(ls_)
# Output: []
res = Solution().sortedListToBST_v1(head)
print(serialize(res))

ls_ = [0]
head = getListNodeFromList(ls_)
# Output: [0]
res = Solution().sortedListToBST_v2(head)
print(serialize(res))

ls_ = [1, 3]
head = getListNodeFromList(ls_)
# Output: [3,1]
res = Solution().sortedListToBST_v2(head)
print(serialize(res))


