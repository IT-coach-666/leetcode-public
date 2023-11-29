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
title_jy = "merge-k-sorted-lists(linked_list)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Merge `k` sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

Example:
Input:
[ 1->4->5,
  1->3->4,
  2->6]
Output: 1->1->2->3->4->4->5->6
"""

import heapq             
from leetcode_jy.utils_jy.about_ListNode import ListNode, getListNodeFromList
from leetcode_jy.utils_jy.about_ListNode import getLen, getTailNode, showLnValue


class Solution:
    """
解法 1: 0021(merge-two-sorted-lists) 的升级版, 由原来的 2 个有序链表变为 k 个

类似归并排序, 可采用分治思想, 将数组分成两个子数组, 对每个子数组进行链表排序,
排序后的两个子数组分别返回一个链表, 然后对这两个链表进行排序, 而对两个链表排
序就可以复用 0021 的代码; 每一次递归调用时, 当前数组会被分成 2 个子数组处理,
记数组的长度为 n, 则递归的深度是 lg(n), 而每一层递归需要排序的链表结点数为所
有链表的结点数的和, 记为 k, 所以算法时间复杂度为 O(k*lg(n)), 空间复杂度为 O(1)
    """
    def mergeKLists_v1(self, lists: List[ListNode]) -> ListNode:
        return self._merge(lists, 0, len(lists)-1)

    def _merge(self, lists: List[ListNode], low: int, high: int) -> ListNode:
        """
        对链表数组 lists[low: high+1] 进行有序合并, 返回一个合并后的链表

        lists: 链表数组
        low: 链表数组的起始下标
        high: 链表数组的末尾下标
        """
        # jy: 如果 low > high, 返回 None, 终止递归
        if low > high:
            return None
        # jy: 如果 low == high, 表明待合并的链表只有一个, 直接返回
        if low == high:
            return lists[low]

        middle = (low + high) // 2
        # jy: 采用分治思想, 将待合并的链表数组拆分为更小的待合并链表子数组
        #     _merge 方法递归处理, 最终返回的是一个合并后的链表
        list_node1 = self._merge(lists, low, middle)
        list_node2 = self._merge(lists, middle+1, high)
        # jy: 对两个有序链表进行合并
        return self._merge_two_lists(list_node1, list_node2)

    def _merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        合并两个有序链表, 同 0021 (也可基于递归方式实现)
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
解法 2: 同解法 1, 但在主函数中进行递归
    """
    def mergeKLists_v2(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        list_node1 = self.mergeKLists_v2(lists[:mid])
        list_node2 = self.mergeKLists_v2(lists[mid:])
        return self._merge_two_lists(list_node1, list_node2)


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
    def mergeKLists_v3(self, lists: List[ListNode]) -> ListNode:
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
ln1 = getListNodeFromList(ls_[0])
ln2 = getListNodeFromList(ls_[1])
ln3 = getListNodeFromList(ls_[2])
ls_ln = [ln1, ln2, ln3]
res = Solution().mergeKLists_v3(ls_ln)
print("res_ln ============: ")
showLnValue(res_ln)





