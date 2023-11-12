from typing import List
from collections import deque


#【01】N 叉树相关 ====================================
class Node(object):
    def __init__(self, val=None, children=None):
        if children is None:
            children = []

        #jy: 当前节点值;
        self.val = val
        #jy: 当前节点的下一层子节点(N 叉树, 最多能有 N 个节点)
        self.children = children


def build_N_ary_tree(ls_N_ary):
    """
    N 叉树的节点关联关系通过类似 [1, [3, [5, 6], 2, 4]] 列表表示:
    节点 1 共有 [3, 2, 4] 三个子节点, 而节点 3 共有 [5, 6] 两个
    子节点    
    """
    #ls_N_ary = [1, [3, [5, 6], 2, 4]]

    def build_children(root, ls_N_ary):
        for i in ls_N_ary:
            if isinstance(i, int):
                node = Node(i)
                root.children.append(node)
                #print("root_.children====: ", [j.val for j in root_.children], 
                #      "int---i: ", i)
            elif isinstance(i, list):
                build_children(node, i)
            
    root = Node(ls_N_ary[0])
    build_children(root, ls_N_ary[1])
    #print("====root: ", root, "====root.children", [j.val for j in root.children])
 
    return root


def show_N_ary_tree(root):
    """
    将 N 叉树转换为类似 [1, [3, [5, 6], 2, 4]] 列表表示:
    节点 1 共有 [3, 2, 4] 三个子节点, 而节点 3 共有 [5, 6] 两
    个子节点

    即构造二叉树的逆过程, 可视为反序列化过程
    """
    if root.val is None:
        return

    def get_children(root):
        ls_tmp = []
        for child in root.children:
            ls_tmp.append(child.val)
            if child.children:
                ls_tmp.append(get_children(child))
        return ls_tmp

    ls_ = [root.val]
    ls_.append(get_children(root))

    return ls_
   

#【01】二叉树相关 =====================================
class TreeNode:
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    """
    def __init__(self, val=0, left=None, right=None,
                 next=None):
        self.val = val
        self.left = left
        self.right = right

        self.next = next    #jy: 【0116】中需要
        self.count = 0      #jy: 【0315】的解法 1 中需要
        self.parent = None  #jy: 【0510】【1650】中需要


def pre_order(root: TreeNode) -> List[int]:
    """
    注意: 可变类型如 [] 不要作为函数参数默认值使用, 故递归调用存放
    入以下子函数(因为递归调用中需要传入列表参照); 也可以在主函数中
    传入列表参数, 但不能指定默认值为空列表, 因此每次调用都需要明确
    传递一个空列表
    """
    def _pre_order(root: TreeNode, ls_) -> List[int]:
        if not root:
            return
        ls_.append(root.val)
        _pre_order(root.left, ls_)
        _pre_order(root.right, ls_)

    res = []
    _pre_order(root, res)
    return res


def pre_order2(root: TreeNode) -> List[int]:
    """
    前序遍历的非递归写法(栈 + 循环)
    """
    res = []
    if not root:
        return res
    stack = [root]
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return res


def in_order(root: TreeNode) -> List[int]:
    """
    注意: 可变类型如 [] 不要作为函数参数默认值使用, 故递归调用存放
    入以下子函数(因为递归调用中需要传入列表参照); 也可以在主函数中
    传入列表参数, 但不能指定默认值为空列表, 因此每次调用都需要明确
    传递一个空列表
    """
    def _in_order(root: TreeNode, ls_) -> List[int]:
        if not root:
            return
        _in_order(root.left, ls_)
        ls_.append(root.val)
        _in_order(root.right, ls_)

    res = []
    _in_order(root, res)
    return res


def in_order2(root: TreeNode) -> List[int]:
    """
    中序遍历的非递归写法
    """
    res = []
    if not root:
        return res

    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            res.append(root.val)
            root = root.right
    return res


def post_order(root: TreeNode) -> List[int]:
    """
    注意: 可变类型如 [] 不要作为函数参数默认值使用, 故递归调用存
    放入以下子函数(因为递归调用中需要传入列表参照); 也可以在主函数
    中传入列表参数, 但不能指定默认值为空列表, 因此每次调用都需要明
    确传递一个空列表
    """
    def _post_order(root: TreeNode, ls_) -> List[int]:
        if not root:
            return
        _post_order(root.left, ls_)
        _post_order(root.right, ls_)
        ls_.append(root.val)

    res = []
    _post_order(root, res)
    return res


def post_order2(root: TreeNode) -> List[int]:
    """
    后续遍历的非递归写法
    """
    res = []
    if not root:
        return res
    # jy-version-1-Begin --------------------------------
    stack1 = []
    # jy: stack2 用于保存 stack1 中出栈时的元素, 因为 stack1 出
    #     栈的顺序会构造成后序遍历的逆序, 将其入栈 stack2 后, 最
    #     后 stack2 不断出栈即为真正的后序遍历结果
    stack2 = []
    stack1.append(root)
    while stack1:
        root = stack1.pop()
        stack2.append(root)
        if root.left:
            stack1.append(root.left)
        if root.right:
            stack1.append(root.right)
    while stack2:
        res.append(stack2.pop().val)
    # jy-version-1-End ---------------------------------
    # jy-version-2-Begin -------------------------------
    '''
    stack = [root]
    while stack:
        c = stack[-1]
        if c.left and root != c.left and root != c.right:
            stack.append(c.left)
        elif c.right and root != c.right:
            stack.append(c.right)
        else:
            res.append(stack.pop().val)
            root = c
    '''
    # jy-version-2-End ----------------------------------
    return res



def build_binary_tree(ls_: List):
    """
依据二叉树的列表存储方式, 还原二叉树, 如:
Given binary tree [3, 9, 20, None, None, 15, 7],
    3
   / \
  9  20
    /  \
   15   7    
    """
    if len(ls_) == 0:
        return None

    ls_tree_node = [TreeNode(i) for i in ls_]
    for i in range(len(ls_)):
        if i == 0:
            continue
        if ls_tree_node[i].val is not None:
            if i % 2 == 1:
                ls_tree_node[(i-1)//2].left = ls_tree_node[i]

                #jy: 构建树时也构建其 parent 属性值;
                ls_tree_node[i].parent = ls_tree_node[(i-1)//2]
            else:
                ls_tree_node[(i-2)//2].right = ls_tree_node[i]
                # jy: 构建树时也构建其 parent 属性值;
                ls_tree_node[i].parent = ls_tree_node[(i-2)//2]
         
    return ls_tree_node[0]


def serialize(root):
    if not root:
        return ""
    ls_res = []
    deque_ = deque([root])
    while deque_ and deque_.count(None) != len(deque_):
        size_ = len(deque_)
        for i in range(size_):
            node = deque_.popleft()
            ls_res.append(node.val if node else None)
            if node is not None:
                deque_.append(node.left)
                deque_.append(node.right)
            else:
                deque_.append(None)
                deque_.append(None)

    while ls_res[-1] is None:
        ls_res.pop()

    return str(ls_res)



if __name__ == "__main__":
    ls_ = [3, 9, 20, None, None, 15, 7]
    # ls_ = [1, None, 2, None, None, 3]
    root = build_binary_tree(ls_)
    print("pre_order: ", pre_order(root))
    print("pre_order2: ", pre_order2(root))
    print("in_order: ", in_order(root))
    print("in_order2: ", in_order2(root))
    print("post_order: ", post_order(root))
    print("post_order2: ", post_order2(root))

    #ls_N_ary = [1, [3, [5, 6], 2, 4]]
    ls_N_ary = [1, [2, 3, [6, 7, [11, [14]]], 4, [8, [12]], 5, [9, [13], 10]]]
    root = build_N_ary_tree(ls_N_ary)
    print(show_N_ary_tree(root))

