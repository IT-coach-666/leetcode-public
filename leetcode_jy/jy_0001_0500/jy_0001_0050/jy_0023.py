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
type_jy = ""
# jy: 记录该题的英文简称以及所属类别
title_jy = "merge-k-sorted-lists(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

Example:
Input:
[ 1->4->5,
  1->3->4,
  2->6]
Output: 1->1->2->3->4->4->5->6
"""
# ===============================================================
from typing import List
import heapq             
from about_ListNode import *


class Solution:
    """
解法1: 021_merge-two-sorted-lists.py 的升级版, 由原来的 2 个有序链表变为了 k 个; 这道
题类似于``归并排序``, 采用分治的思想, 将数组分成两个子数组, 对每个子数组进行链表排序, 排
序后的两个子数组分别返回一个链表, 然后对这两个链表进行排序, 而对两个链表排序就可以复
用 021_merge-two-sorted-lists.py 的代码; 每一次递归调用时, 当前数组会被分成 2 个子数组
处理, 记数组的长度为 n, 则递归的深度是 lg(n), 而每一层递归需要排序的链表结点数为所有链
表的结点数的和, 记为 k, 所以算法的时间复杂度为 O(k*lg(n)), 空间复杂度为 O(1);
    """
    def mergeKLists_v1(self, lists: List[ListNode]) -> ListNode:
        return self._merge(lists, 0, len(lists)-1)

    def _merge(self, lists: List[ListNode], low: int, high: int) -> ListNode:
        # jy: 如果 low 大于 high, 返回 None, 则终止递归;
        if low > high:
            return None
        if low == high:
            return lists[low]

        middle = (low + high) // 2
        list1, list2 = self._merge(lists, low, middle), self._merge(lists, middle+1, high)
        return self._merge_two_lists(list1, list2)

    def _merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        合并两个有序链表, 同 021_merge-two-sorted-lists.py
        """
        dummy = ListNode(-1)
        prev = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 or l2
        return dummy.next


    """
解法2: 基于列表中的有序链表的头结点构造最小堆(即最小堆的堆顶总是代表一个链表的头节点, 其
节点值是所有链表头节点中最小的); 由于 ListNode 无法进行大小比较, 我们需要定义一个封装类实
现 __lt__ 方法来比较链表结点的大小(对原链表进行封装, 并在封装类中实现 __lt__ 方法, 使得能
根据链表头节点比较链表之间的大小);

构造完最小堆后, 每次从最小堆中出一个元素, 即为头节点值最小的链表, 将该头节点的值加入
构造的有序链表, 随后再将其下一个节点加入到最小堆中(如果下一个节点存在的话), 不断重复
直到最小堆为空; 

记数组的长度为 n, 所有链表的结点数之和为 k, 则初始化优先队列的时间复杂度为 O(n) (即: 取
所有链表的头结点和初始化优先队列), 优先队列的取元素和插入元素的时间复杂度为 O(lg(n)), 总
共有 k 个元素, 所以构建新链表的时间复杂度为 O(k*lg(n)), 整体的时间复杂度为 
max{O(n), O(k*lg(n))}, 当 k 大于 n 时, 时间复杂度简化为 O(k*lg(n)); 

额外的空间消耗为构建优先队列, 故空间复杂度为 O(n);
    """
    def mergeKLists_v2(self, lists: List[ListNode]) -> ListNode:
        # jy: node 为一个有序链表的头结点, 此处对有序链表的头结点进行封装, 并放到队列中;
        queue = [ListNodeWrap(node) for node in lists if node]
        # jy: 使列表具有堆特性;
        heapq.heapify(queue)
        dummy = ListNode(-1)
        prev = dummy

        while queue:
            # jy: 从堆中弹出最小的元素(封装后的链表的大小比较为首元素大小比较), 即
            #    头元素最小的经过封装后的链表;
            node_wrap = heapq.heappop(queue)
            # jy: 还原未经封装时的链表;
            node = node_wrap.node
            # jy: 获取链表的头节点(即最小值);
            prev.next = ListNode(node.val)
            prev = prev.next
            # jy: 将链表的后一节点开始的部分再次封装后入堆(如果其存在的话);
            if node.next:
                heapq.heappush(queue, ListNodeWrap(node.next))
        return dummy.next

    """
JY: 将有序链表先转为有序数组, 排序后的有序数组再转为链表即可;
以下仅以有序数组为例进行实现;
    """
    def mergeKLists_jy(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists_jy(lists[: mid])
        right = self.mergeKLists_jy(lists[mid:])
        return self.merge_two_list(left, right)

    def merge_two_list(self, list1, list2):
        i = 0
        j = 0
        merged = []
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1

        if i < len(list1):
            merged += list1[i:]
        elif j < len(list2):
            merged += list2[j:]

        return merged



class ListNodeWrap:
    def __init__(self, node: ListNode):
        self.node = node

    # jy: 使得经过 ListNodeWrap 封装后的链表在比较大小时通过头元素大小进行比较;
    #    实现该方法使得这种封装后的链表入堆后能构造出堆具有的特性; 如果去掉该
    #    方法, 则当执行到以上 heapq.heapify(queue) 时会出现以下报错:
    """
TypeError: '<' not supported between instances of 'ListNodeWrap' and 'ListNodeWrap'
    """
    def __lt__(self, other: 'ListNodeWrap'):
        return self.node.val < other.node.val



ls1 = [1, 4, 5]
ls2 = [1, 3, 4]
ls3 = [2, 6]
ln1 = getListNodeFromList(ls1)
ln2 = getListNodeFromList(ls2)
ln3 = getListNodeFromList(ls3)
print("ln1 ============: ")
showLnValue(ln1)
print("ln2 ============: ")
showLnValue(ln2)
print("ln3 ============: ")
showLnValue(ln3)

ls_ln = [ln1, ln2, ln3]
res_ln = Solution().mergeKLists_v1(ls_ln)
print("res_ln ============: ")
showLnValue(res_ln)



ls1 = [1, 4, 5]
ls2 = [1, 3, 4]
ls3 = [2, 6]
ln1 = getListNodeFromList(ls1)
ln2 = getListNodeFromList(ls2)
ln3 = getListNodeFromList(ls3)

ls_ln = [ln1, ln2, ln3]
res_ln = Solution().mergeKLists_v2(ls_ln)
print("res_ln ============: ")
showLnValue(res_ln)

ls_ = [[1,4,5],[1,3,4],[2,6]]
# [1,1,2,3,4,4,5,6]
res = Solution().mergeKLists_jy(ls_)
print(res)





