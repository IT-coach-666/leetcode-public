
"""
【01】快慢指针 ===================================================================
"""
def get_mid_or_upMid_node(head):
    """
    返回链表的中点（奇数长度返回中点，偶数长度返回上中点）
    """
    # version-1-Begin---------------------------------------
    '''
    if not head or not head.next or not head.next.next:
        return head

    # jy: 如果以上没返回, 表明链表至少有 3 个节点
    slow = head.next
    fast = head.next.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    '''
    # version-1-End-----------------------------------------
    # version-2-Begin---------------------------------------
    if not head or not head.next:
        return head

    # jy: 如果以上没返回, 表明链表至少有 3 个节点
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # version-2-End-----------------------------------------
    return slow


def get_mid_or_downMid_node(head):
    """
    返回链表的中点(奇数长度返回中点，偶数长度返回下中点)
    """
    # version-1-Begin---------------------------------------
    '''
    if not head or not head.next:
        return head
    # jy: 以下 if 判断去除也可以; 
    # if not head.next.next:
    #     return head.next

    # jy: 如果以上没返回, 表明链表至少有 3 个节点
    slow = head.next
    fast = head.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    '''
    # version-1-End-----------------------------------------
    # version-2-Begin---------------------------------------
    # jy: 包含了所有边界条件
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # version-2-End-----------------------------------------
    return slow


def get_mid_or_upMid_preNode(head):
    """
    返回链表的中点前一个（奇数长度返回中点前一个，偶数长度返回上中点前一个）
    """
    if not head or not head.next or not head.next.next:
        return None

    # jy: 如果以上没返回, 表明链表至少有 3 个节点
    slow = head
    fast = head.next.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def get_mid_or_downMid_preNode(head):
    """
    返回链表的中点前一个（奇数长度返回中点前一个，偶数长度返回下中点前一个）
    """
    if not head or not head.next:
        return None
    if not head.next.next:
        return head

    # jy: 如果以上没返回, 表明链表至少有 3 个节点
    slow = head
    fast = head.next
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow



