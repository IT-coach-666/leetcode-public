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
tag_jy = "递归 | 链表双指针技巧"


"""
Given the `head` of a singly linked list where elements are sorted in
ascending order, convert it to a height-balanced BST.


Example 1: 
Input: head = [-10, -3, 0, 5, 9]
Output: [0, -3, 9, -10, null, 5]
Explanation: One possible answer is [0, -3, 9, -10, null, 5], which
             represents the shown height balanced BST.
               0   
              / \  
            -3   9   
            /   /  
          -10  5  

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
1) The number of nodes in head is in the range [0, 2 * 10^4].
2) -10^5 <= Node.val <= 10^5
"""


from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_TreeNode import TreeNode, build_binary_tree
from leetcode_jy.utils_jy.about_TreeNode import serialize


class Solution:
    """
解法 1: 同 0108

先将列表转为有序数组, 则题目变为 0108 (Convert-Sorted-Array-to-Binary-Search-Tree)
    """
    def sortedListToBST_v1(self, head: ListNode) -> TreeNode:
        values = self._get_sorted_array(head)
        return self._convert_sorted_array_to_bst(values, 0, len(values) - 1)

    def _get_sorted_array(self, head):
        """
        基于有序链表获取有序数组
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
解法 2: 类似解法 1, 但使用了快慢指针来定位中间节点 (即根节点)
    """
    def sortedListToBST_v2(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        return self._sorted_list_to_bst(head, None)

    def _sorted_list_to_bst(self, head, tail):
        """
        基于链表的 head 至 tail 节点构建平衡二叉搜索树 (不包含 tail 节点)

        tail 节点初始化时为链表最后一个节点的下一个节点, 即 None
        """
        if head is tail:
            return None
        # jy: 初始化快慢指针, 均指向头节点; 快指针每次走两步, 慢指针每次走一
        #     步, 则快指针走到 tail 时, 慢指针所在的节点即为中间节点
        slow, fast = head, head
        while fast is not tail and fast.next is not tail:
            fast = fast.next.next
            slow = slow.next

        root = TreeNode(slow.val) 
        # jy: 基于链表的 head 至 slow 节点构建左子树 (构建时不包含 slow 节点)
        root.left = self._sorted_list_to_bst(head, slow)
        # jy: 基于链表 slow 节点的下一节点至 tail 构建右子树 (构建时不会包含
        #     tail 节点)
        root.right = self._sorted_list_to_bst(slow.next, tail)

        return root


ls_ = [-10, -3, 0, 5, 9]
head = getListNodeFromList(ls_)
res = Solution().sortedListToBST_v1(head)
# jy: [0, -10, 5, None, -3, None, 9]
print(serialize(res))

ls_ = []
head = getListNodeFromList(ls_)
res = Solution().sortedListToBST_v1(head)
# jy: []
print(serialize(res))

ls_ = [0]
head = getListNodeFromList(ls_)
res = Solution().sortedListToBST_v2(head)
# jy: [0]
print(serialize(res))

ls_ = [1, 3]
head = getListNodeFromList(ls_)
res = Solution().sortedListToBST_v2(head)
# jy: [3, 1]
print(serialize(res))


