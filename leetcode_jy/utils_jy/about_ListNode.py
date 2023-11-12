class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

    # def __eq__(self, other):
    #     return other.val


def getListNodeFromList(ls_, pos=-1):
    """
    将 list 转换为 ListNode 形式
    
    pos 不为 -1 时表示有环 (最后一个值的 next 为 pos 位置的对应
    的 ListNode)
    """
    if not ls_:
        return None

    ls_list_node = [ListNode(i) for i in ls_]
    for i in range(len(ls_list_node)-1):
        ls_list_node[i].next = ls_list_node[i+1]
    if pos != -1:
        ls_list_node[-1].next = ls_list_node[pos]
    return ls_list_node[0]


def getTailNode(ln_):
    """
    获取链表中的最后一个节点
    """
    tmp_ln = ln_
    while tmp_ln.next:
        tmp_ln = tmp_ln.next
    return tmp_ln


def getLen(ln_):
    """
    获取链表的长度
    """
    tmp_ln = ln_
    len_ = 0
    while tmp_ln:
        len_ += 1
        tmp_ln = tmp_ln.next
    return len_


def showLnValue(head_):
    """
    展示 ListNode 对象中的值 (不改变原有对象, 遍历后不将原有对象置
    于链尾)
    """
    tmp_ln = head_
    str_ = ""
    while tmp_ln:
        str_ += str(tmp_ln.val) + "->"
        tmp_ln = tmp_ln.next
    # jy: 仅对右侧去除 "->" 字符即可(即表示右侧如果有这两个字符中
    #     的其中一个, 都会去除)
    print(str_.rstrip("->"))


def showCircleLnValue(head_):
    """
    展示带环 ListNode (头结点为环的交接点) 中的值
    (不改变原有对象; 遍历后不将原有对象置于链尾)
    """
    tmp_ln = head_
    str_ = ""
    while tmp_ln:
        str_ += str(tmp_ln.val) + "->"
        tmp_ln = tmp_ln.next
        if tmp_ln is head_:
            break
    print(str_.strip("->"))

    
def showDoublyLinkedListValue(head_):
    """
    展示双向链表 Doubly-linked-List (不成环) 中的值, 并且不改变原
    有对象(遍历后不将原有对象置于链尾);
    """
    tmp_ln = head_
    str_ = ""
    while tmp_ln:
        str_ += str(tmp_ln.val) + "->"
        tmp_ln = tmp_ln.next
    print(str_.strip("->"))


if __name__ == "__main__":
    ls_ = [11, 22, 33, 44, 55]
    head_ = getListNodeFromList(ls_)
    print("ListNode1 :")
    showLnValue(head_)



