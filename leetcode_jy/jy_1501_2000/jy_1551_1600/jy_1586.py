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
title_jy = "Binary-Search-Tree-Iterator-II(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Implement the ``BSTIterator`` class that represents an iterator over the in-order 
traversal of a binary search tree (BST):
BSTIterator(TreeNode root) : Initializes an object of the BSTIterator class. The root 
                             of the BST is given as part of the constructor. The pointer
                             should be initialized to a non-existent number smaller than
                             any element in the BST.
boolean hasNext() : Returns true if there exists a number in the traversal to the right 
                    of the pointer, otherwise returns false.
int next() :  Moves the pointer to the right, then returns the number at the pointer.
boolean hasPrev() : Returns true if there exists a number in the traversal to the left
                    of the pointer, otherwise returns false.
int prev() : Moves the pointer to the left, then returns the number at the pointer.


Notice that by initializing the pointer to a non-existent smallest number, the first call 
to next() will return the smallest element in the BST. You may assume that next() and prev() 
calls will always be valid. That is, there will be at least a next/previous number in the 
in-order traversal when next()/prev() is called.



Example 1:
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);   # state is   [3, 7, 9, 15, 20]
bSTIterator.next();      # state becomes [3, 7, 9, 15, 20], return 3
bSTIterator.next();      # state becomes [3, 7, 9, 15, 20], return 7
bSTIterator.prev();      # state becomes [3, 7, 9, 15, 20], return 3
bSTIterator.next();      # state becomes [3, 7, 9, 15, 20], return 7
bSTIterator.hasNext();   # return true
bSTIterator.next();      # state becomes [3, 7, 9, 15, 20], return 9
bSTIterator.next();      # state becomes [3, 7, 9, 15, 20], return 15
bSTIterator.next();      # state becomes [3, 7, 9, 15, 20], return 20
bSTIterator.hasNext();   # return false
bSTIterator.hasPrev();   # return true
bSTIterator.prev();      # state becomes [3, 7, 9, 15, 20], return 15
bSTIterator.prev();      # state becomes [3, 7, 9, 15, 20], return 9


Constraints:
The number of nodes in the tree is in the range [1, 10^5].
0 <= Node.val <= 10^6
At most 10^5 calls will be made to hasNext, next, hasPrev, and prev.


Follow up: Could you solve the problem without precalculating the values of the tree?
"""

from about_TreeNode import *

"""
解法1: 和 173_Binary-Search-Tree-Iterator.py 的解法 1 一样, 实现计算出树的中序遍历; 
"""
class BSTIterator_v1:
    
    def __init__(self, root: TreeNode):
        self.nodes = []
        # jy: 初始化时即将二叉搜索树的中序遍历结果记录到 self.nodes 列表;
        self._inorder(root, self.nodes)
        # jy: 记录当前节点的坐标位置(初始化为 -1);
        self.pointer = -1


    def hasNext(self) -> bool:
        return self.pointer + 1 < len(self.nodes)


    def next(self) -> int:
        """题干中说明 next 调用确保有效, 否则需要再补充 if 判断, 确保有下一个值"""
        self.pointer += 1
        return self.nodes[self.pointer]


    def hasPrev(self) -> bool:
        return self.pointer - 1 >= 0


    def prev(self) -> int:
        """题干中说明 prev 调用确保有效, 否则需要再补充 if 判断, 确保有上一个值"""
        self.pointer -= 1
        return self.nodes[self.pointer]


    def _inorder(self, root, nodes):
        if not root:
            return

        self._inorder(root.left, nodes)
        nodes.append(root.val)
        self._inorder(root.right, nodes)



"""
解法2: Follow up 中要求不能提前构建中序遍历;

使用两个栈, next_stack 和 prev_stack, 分别用来维护下一个和上一个节点; 当调用 next 时, 
同 173_Binary-Search-Tree-Iterator.py 的解法2, 将弹出的节点的右子树的左节点都入栈;

不同的是 next 操作时需要判断当前节点是否已经被访问过, 如果被访问过在执行当前 next 之前
曾经执行过 prev, 然后再次执行当前的 next 操作, 这种情况下右子树的左节点已经在 next_stack
中了, 不需要重复加入; 最后将 next_stack 中出栈的节点放到 prev_stack 中(即 prev_stack 的栈
顶元素即为当前元素); 调用 prev 时, 将 prev_stack 栈顶的元素放到 next_stack 中, 然后出栈 
prev_stack 栈顶的元素; 
"""
class BSTIterator_v2:
    def __init__(self, root: TreeNode):
        self.next_stack = []
        self.prev_stack = []
        self.visited = set()
        #:jy 初始化时, 先将当前节点(根节点)的及其左子节点不断递归入栈; 最后栈顶即为第一个元素;
        current = root
        while current:
            self.next_stack.append(current)
            current = current.left


    def hasNext(self) -> bool:
        # jy: next_stack 栈不为空即表示有下一个值;
        return len(self.next_stack) > 0


    def next(self) -> int:
        # jy: next_stack 栈顶即为下一个元素对应的值;
        node = self.next_stack.pop()
        # jy: 1) 如果当前出栈节点之前没有被访问过, 且其右节点不为空, 则不断将其右子节点及
        #       右子节点对应的左子节点递归入栈 next_stack, 确保该栈中的栈顶是下一个元素值;
        #    2) 如果当前出栈节点已经被遍历过, 说明在执行当前的 next 操作时之前已经执行过
        #       prev 操作, 然后再次执行当前的 next 操作, 这种情况下右子树的左节点已经在
        #       next_stack 中了, 不需要重复加入;
        if node not in self.visited and node.right is not None:
            current = node.right
            while current:
                self.next_stack.append(current)
                current = current.left
        # jy: 随后将当前节点加入已访问集合, 并加入到 prev_stack 栈中(该栈的栈顶即为当前的上一个元素值);
        self.visited.add(node)
        self.prev_stack.append(node)
        # jy: 返回当前节点值;
        return node.val


    def hasPrev(self) -> bool:
        # jy: prev_stack 栈不为空即表示有上一个值;
        return len(self.prev_stack) > 1


    def prev(self) -> int:
        # jy: 获取上一个值时, 先要出栈 prev_stack 栈顶的元素, 因为获取当前元素时, 读取得到后
        #    会将当前元素存入到 prev_stack 的栈顶;
        self.next_stack.append(self.prev_stack.pop())
        return self.prev_stack[-1].val


ls_ = [7, 3, 15, None, None, 9, 20]
root = build_binary_tree(ls_)
bSTIterator = BSTIterator_v1(root)   # state is   [3, 7, 9, 15, 20]
print(bSTIterator.next())      # state becomes [3, 7, 9, 15, 20], return 3
print(bSTIterator.next())      # state becomes [3, 7, 9, 15, 20], return 7
print(bSTIterator.prev())      # state becomes [3, 7, 9, 15, 20], return 3
print(bSTIterator.next())      # state becomes [3, 7, 9, 15, 20], return 7
print(bSTIterator.hasNext())   # return true
print(bSTIterator.next())      # state becomes [3, 7, 9, 15, 20], return 9
print(bSTIterator.next())      # state becomes [3, 7, 9, 15, 20], return 15
print(bSTIterator.next())      # state becomes [3, 7, 9, 15, 20], return 20
print(bSTIterator.hasNext())   # return false
print(bSTIterator.hasPrev())   # return true
print(bSTIterator.prev())      # state becomes [3, 7, 9, 15, 20], return 15
print(bSTIterator.prev())      # state becomes [3, 7, 9, 15, 20], return 9


ls_ = [7, 3, 15, None, None, 9, 20]
root = build_binary_tree(ls_)
bSTIterator = BSTIterator_v2(root)   # state is   [3, 7, 9, 15, 20]
print(bSTIterator.next())      # state becomes [3, 7, 9, 15, 20], return 3
print(bSTIterator.next())      # state becomes [3, 7, 9, 15, 20], return 7
print(bSTIterator.prev())      # state becomes [3, 7, 9, 15, 20], return 3
print(bSTIterator.next())      # state becomes [3, 7, 9, 15, 20], return 7
print(bSTIterator.hasNext())   # return true
print(bSTIterator.next())      # state becomes [3, 7, 9, 15, 20], return 9
print(bSTIterator.next())      # state becomes [3, 7, 9, 15, 20], return 15
print(bSTIterator.next())      # state becomes [3, 7, 9, 15, 20], return 20
print(bSTIterator.hasNext())   # return false
print(bSTIterator.hasPrev())   # return true
print(bSTIterator.prev())      # state becomes [3, 7, 9, 15, 20], return 15
print(bSTIterator.prev())      # state becomes [3, 7, 9, 15, 20], return 9

import os
print(os.getcwd())





