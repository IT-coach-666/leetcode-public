from typing import List
from collections import deque


#【01】N 叉树相关 ============================================================
class Node(object):
    """
    N 叉树的节点
    """
    def __init__(self, val=None, children=None):
        if children is None:
            children = []

        #jy: 当前节点值
        self.val = val
        #jy: 当前节点的下一层子节点 (N 叉树最多有 N 个节点)
        self.children = children


def build_N_ary_tree(ls_N_ary):
    """
    基于 N 叉树的序列化结果列表, 反序列化为 N 叉树

    [1, [3, [5, 6], 2, 4]] 表示的 N 叉树:
    节点 1 共有 [3, 2, 4] 三个子节点, 而节点 3 共有 [5, 6] 两个子节点

    序列化结果列表中, 有几个中括号嵌套就表示树有几层
    """
    #ls_N_ary = [1, [3, [5, 6], 2, 4]]

    def build_children(root, ls_N_ary):
        """
        root: 当前 N 叉树的根节点
        ls_N_ary: N 叉树根节点下面的子节点列表
        """
        for i in ls_N_ary:
            # jy: 如果列表中的元素是整数值, 表明该整数值的节点
            #     为根节点的子节点
            if isinstance(i, int):
                # jy: 构建 N 叉树的节点
                node = Node(i)
                root.children.append(node)
            # jy: 如果列表中的元素是列表类型, 表明该元素是前一个
            #     节点 node 下面的子节点, 递归构建该子 N 叉树`
            elif isinstance(i, list):
                build_children(node, i)
            
    # jy: 构建 N 叉树的根节点
    root = Node(ls_N_ary[0])
    # jy: 递归构建 N 叉树
    build_children(root, ls_N_ary[1])
    # jy: 返回 N 叉树的根节点
    return root


def show_N_ary_tree(root):
    """
    将 N 叉树进行序列化, 转换为列表存储

    如 N 叉树的节点 1 共有 [3, 2, 4] 三个子节点, 而节点 3 共有 [5, 6] 两
    个子节点, 则该 N 叉树对应的列表为: [1, [3, [5, 6], 2, 4]]
    """
    if root.val is None:
        return []

    def get_children(root):
        """
        传入 N 叉树的根节点, 返回根节点对应的子节点列表
        """
        ls_tmp = []
        # jy: 遍历根节点的子节点列表 (即 children 属性)
        for child in root.children:
            # jy: 将子节点的值放入列表, 如果该子节点存在下一层子节点,
            #     则递归获取下一层子节点的列表, 并存入到当前列表中
            ls_tmp.append(child.val)
            if child.children:
                ls_tmp.append(get_children(child))
        return ls_tmp

    # jy: 将根节点的值放入结果列表
    ls_ = [root.val]
    # jy: 获取根节点对应的子节点列表
    ls_.append(get_children(root))

    return ls_
   

#【01】二叉树相关 ============================================================
# 01) 二叉树节点 ------------------------------------------------
class TreeNode:
    """
    二叉树节点类 (含各种属性)
    """
    def __init__(self, val=0, left=None, right=None,
                 next=None, count=0, parent=None):
        # jy: 二叉树节点必备属性
        self.val = val
        self.left = left
        self.right = right

        # jy: 二叉树节点的扩充属性
        self.next = next      # jy: 【0116】中需要
        self.count = count    # jy: 【0315】的解法 1 中需要
        self.parent = parent  # jy: 【0510】【1650】中需要


# 02) 二叉树的构建 ----------------------------------------------
def build_binary_tree(ls_: List):
    """
    基于二叉树列表存储方式, 还原二叉树

    ls_: 二叉树的列表存储 (即将二叉树补齐为完全二叉树, 随后从上到下、从左
         到右逐个元素记录到列表中); 满二叉树列表可以基于列表的下标位置定
         位到相应节点的父节点, 因此可基于该特性对二叉树进行恢复

    如以下二叉树存储为: [3, 9, 20, None, None, 15, 7]
            3
           / \
          9  20
            /  \
           15   7
    """
    if len(ls_) == 0:
        return None

    # jy: 初始化树节点
    ls_tree_node = [TreeNode(i) for i in ls_]
    for i in range(len(ls_)):
        # jy: 对应根节点, 无需操作
        if i == 0:
            continue
        if ls_tree_node[i].val is not None:
            # jy: 如果 i 为奇数, 表明对应的节点为左子节点
            if i % 2 == 1:
                parent_idx = (i - 1) // 2
                ls_tree_node[parent_idx].left = ls_tree_node[i]

                #jy: 考虑 parent 属性时的二叉树设置
                ls_tree_node[i].parent = ls_tree_node[parent_idx]
            # jy: 如果 i 为偶数, 表明对应的节点为右子节点
            else:
                parent_idx = (i - 2) // 2
                ls_tree_node[parent_idx].right = ls_tree_node[i]

                # jy: 考虑 parent 属性时的二叉树设置
                ls_tree_node[i].parent = ls_tree_node[parent_idx]

    # jy: 返回二叉树的根节点
    return ls_tree_node[0]


# 03) 二叉树的遍历 ----------------------------------------------
def preorderTraversal(root: TreeNode) -> List[int]:
    """
    前序遍历: 递归

    前序遍历: 先遍历当前节点, 再遍历左子树, 最后遍历右子树
    """
    def pre_order(root: TreeNode, ls_) -> List[int]:
        if not root:
            return
        # jy: 先遍历当前节点, 再遍历左子树, 最后遍历右子树
        ls_.append(root.val)
        pre_order(root.left, ls_)
        pre_order(root.right, ls_)

    ls_res = []
    pre_order(root, ls_res)
    return ls_res


def preorderTraversal_v2(root: TreeNode) -> List[int]:
    """
    前序遍历: (栈 + 循环)
    """
    ls_res = []
    if not root:
        return ls_res

    # jy: 先将根节点入栈, 随后不断出栈树节点元素, 将元素值存放
    #     到结果列表; 接着先判断树节点元素是否有右子节点, 如果
    #     存在右子节点, 则将右子节点入栈, 再判断是否有左子节点,
    #     如果有, 则将左子节点入栈 (因为栈是后进先出, 左子节点
    #     后入栈, 后续出栈时才能确保左子节点比右子节点先遍历到)
    stack = [root]
    while stack:
        root = stack.pop()
        ls_res.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return ls_res


def inorderTraversal(root: TreeNode) -> List[int]:
    """
    中序遍历: 先遍历左子节点, 再遍历父节点, 最后遍历右子节点
    """
    def in_order(root: TreeNode, ls_) -> List[int]:
        if not root:
            return []
        in_order(root.left, ls_)
        ls_.append(root.val)
        in_order(root.right, ls_)

    ls_res = []
    in_order(root, ls_res)
    return ls_res


def inorderTraversal_v2(root: TreeNode) -> List[int]:
    """
    中序遍历: 非递归写法 (栈 + 循环/迭代)

    遍历完后不影响树的根节点

    思路: 维护一个栈, 只要当前结点不为空, 则不断入栈, 并更新当前节点为左
    子结点, 直到没有左子结点为止, 则出栈一个结点, 将节点值记录列表中, 然
    后将当前节点更新为出栈结点的右子结点, 随后不断重复原先的左子节点操作
    """
    if not root:
        return []

    ls_res = []
    stack = []
    # jy: 遍历完后不影响树的根节点
    current = root
    # jy: 当没有节点、且栈为空时才退出循环
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            ls_res.append(current.val)
            current = current.right
    return ls_res


def inorderTraversal_v3(root: TreeNode) -> List[int]:
    """
    中序遍历: 非递归写法的改写 (栈 + 循环/迭代)
    """
    if not root:
        return []

    ls_res = []
    stack = []
    # jy: 遍历完后不影响树的根节点
    current = root
    # jy: 当没有节点、且栈为空时才退出循环
    while stack or current:
        
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        ls_res.append(current.val)
        current = current.right
    return ls_res



def postorderTraversal(root: TreeNode) -> List[int]:
    """
    后序遍历: 递归

    后序遍历: 先遍历左子树, 再遍历右子树, 最后遍历当前节点
    """
    def post_order(root: TreeNode, ls_) -> List[int]:
        if not root:
            return
        post_order(root.left, ls_)
        post_order(root.right, ls_)
        ls_.append(root.val)

    ls_res = []
    post_order(root, ls_res)
    return ls_res


def postorderTraversal_v2(root: TreeNode) -> List[int]:
    """
    后续遍历: 栈 + 循环

    基于以下二叉树进行思考:
            3
           / \
          9  20
            /  \
           15   7
    后续遍历结果为: [9, 15, 7, 20, 3]
    """
    ls_res = []
    if not root:
        return ls_res

    # jy: stack 出栈的顺序即后序遍历的逆序
    stack = []

    # jy: 先将根节点入栈, 随后不断循环出栈, 并将出栈节点值加入
    #     结果列表 ls_res, 同时如果出栈节点存在左子节点, 则先将
    #     左子节点入栈, 如果存在右子节点, 则将右子节点入栈; 因
    #     此后续不断出栈的元素总是优先将树的下一层右子节点出栈,
    #     其次是下一层的左子节点, 使得最终出栈结果为后续遍历的
    #     逆序顺序
    stack.append(root)
    while stack:
        root = stack.pop()
        ls_res.append(root.val)

        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)

    ls_res = ls_res[::-1]
    return ls_res


def postorderTraversal_v3(root: TreeNode) -> List[int]:
    """
    后续遍历: 栈 + 循环 (出栈结果无需倒序); 该方法逻辑较难梳理

    基于以下二叉树进行思考:
            3
           / \
          9  20
            /  \
           15   7
    后续遍历结果为: [9, 15, 7, 20, 3]
    """
    ls_res = []
    if not root:
        return ls_res

    stack = [root]
    while stack:
        # jy: 当前节点总是为栈顶节点 (并不出栈)
        cur = stack[-1]

        # jy: 如果当前节点存在左子节点, 且 root 不是当前节点的左/右
        #     子节点, 则将当前节点的左子节点入栈 (root 后续会被更新
        #     为最新出栈的节点, 如果当前节点的左/右子节点为 root 节
        #     点, 表明左/右子节点已经遍历过, 不能再将其加入栈中, 防
        #     止重复遍历)
        if cur.left and root != cur.left and root != cur.right:
            stack.append(cur.left)
        # jy: 如果当前节点存在右子节点, 且 root 不是当前节点的右子节
        #     点, 则将当前节点的右子节点入栈 (root 含义参见以上说明)
        elif cur.right and root != cur.right:
            stack.append(cur.right)
        # jy: 如果当前节点没有左右子节点, 或当前节点的左右子节点均已
        #     经被遍历过 (即 root 节点为当前节点的左/右子节点), 则将
        #     当前节点出栈, 并将该节点作为新的 root (代表已经遍历过)
        else:
            # jy: root 每次均更新为最新出栈的节点
            ls_res.append(stack.pop().val)
            root = cur

    return ls_res


def levelorderTraversal(root: TreeNode) -> List[List[int]]:
    """
    循环 + 队列 (先进先出)

    初始化时先将根节点入队, 随后遍历队列时, 先记录当前队列的长度 n,
    然后执行 n 次出队操作, 则这 n 次出队的结点都是同一层的结点
    """
    queue = deque([root]) if root else deque()
    ls_level = []
    while queue:
        ls_level_i = []
        # jy: 第一轮遍历时, 根节点一层只有一个元素, 循环一次: 出队一
        #     个元素, 并将其左右子节点入队 (入队过程中不会影响当前的
        #     len(queue), 需等原先 for 循环结束后该值再做更新; 但为了
        #     避免误解, 可将 len(queue) 放在 for 循环之前); 经过一轮
        #     循环后, queue 的长度即下一层元素的个数
        for _ in range(len(queue)):
            node = queue.popleft()
            ls_level_i.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ls_level.append(ls_level_i)
    return ls_level


def levelorderTraversal_v2(root: TreeNode) -> List[List[int]]:
    """
    递归 (深度优先搜索)

    深度优先搜索时记录当前的层数, 如果 ls_level 的长度小于当前层数, 说明
    当前节点属于新的一层, 则在 ls_level 中加入一个新数组, 接着将结点的值
    加入到对应层的 ls_level 数组中
    """
    def _dfs(root: TreeNode, level: int, ls_level: List[List[int]]) -> None:
        """
        当前树节点 root 属于第 level 层; ls_level 用于存放所有层结果
        """
        # jy: 如果 root 不存在, 则 return 终止
        if not root:
            return
        # jy: 如果 level 大于 ls_level 的长度, 表明第 level 层还不存在
        #     于 ls_level 中, 应往 ls_level 中加入新层 [], 用以存放当
        #     前 root 元素
        if level > len(ls_level):
            ls_level.append([])

        # jy: 将 root 加入 ls_level 的第 n 层中 (对应的下标为 n-1)
        ls_level[level - 1].append(root.val)
        _dfs(root.left, level + 1, ls_level)
        _dfs(root.right, level + 1, ls_level)

    ls_level = []
    # jy: 先将 root 节点加入第 1 层 (如果 root 为空, 则 _dfs 会直接返回,
    #     不会在 ls_level 中加入数值)
    _dfs(root, 1, ls_level)
    return ls_level


# 04) 二叉树的序列化存储 ----------------------------------------
def serialize(root):
    """
    广度优先遍历 (BFS) 序列化树节点值
    """
    if not root:
        return []

    ls_res = []
    # jy: 将根节点放入双端队列
    deque_ = deque([root])
    # jy: 如果队列不为空, 且队列中至少有一个有效树节点, 表明当前队
    #     列中的元素为树结构中的同一层, 统计该层的节点数后不断左侧
    #     出队并添加到结果列表里, 同时将相应节点的左右子节点右侧入
    #     队, 如果相应节点为 None, 其对应的左右子节点也均对应为 None
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

    # jy: 去除结果列表中最右侧的 None (构造完全二叉树即可, 不需为满
    #     二叉树)
    while ls_res[-1] is None:
        ls_res.pop()

    #return str(ls_res)
    return ls_res



if __name__ == "__main__":
    # jy: 二叉树 ================================================
    ls_ = [3, 9, 20, None, None, 15, 7]
    # ls_ = [1, None, 2, None, None, 3]
    # jy: 构建二叉树 --------------------------------------------
    root = build_binary_tree(ls_)

    # jy: 二叉树遍历 --------------------------------------------
    print("preorderTraversal: ", preorderTraversal(root))
    print("preorderTraversal_v2: ", preorderTraversal_v2(root))
    print("inorderTraversal: ", inorderTraversal(root))
    print("inorderTraversal_v2: ", inorderTraversal_v2(root))
    print("postorderTraversal: ", postorderTraversal(root))
    print("postorderTraversal_v2: ", postorderTraversal_v2(root))
    print("postorderTraversal_v3: ", postorderTraversal_v3(root))

    # jy: 二叉树的序列化存储 ------------------------------------
    ls_res = serialize(root)
    print(ls_res)

    # jy: N 叉树 ================================================
    #ls_N_ary = [1, [3, [5, 6], 2, 4]]
    ls_N_ary = [1, [2, 3, [6, 7, [11, [14]]], 4, [8, [12]], 5, [9, [13], 10]]]
    # jy: 构建 N 叉树 -------------------------------------------
    root = build_N_ary_tree(ls_N_ary)
    # jy: N 叉树的序列化过程 ------------------------------------
    print(show_N_ary_tree(root))


