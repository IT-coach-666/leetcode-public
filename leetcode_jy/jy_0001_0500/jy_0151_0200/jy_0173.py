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
title_jy = "Binary-Search-Tree-Iterator(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of
a binary search tree (BST):

1) BSTIterator(TreeNode root): Initializes an object of the BSTIterator class. The root of the
   BST is given as part of the constructor. The pointer should be initialized to a non-existent
   number smaller than any element in the BST.

2) boolean hasNext(): Returns true if there exists a number in the traversal to the right of the
   pointer, otherwise returns false.

3) int next(): Moves the pointer to the right, then returns the number at the pointer.




Notice that by initializing the pointer to a non-existent smallest number, the first call to next()
will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number
in the in-order traversal when next() is called.



Example 1:
    7
   / \
  3   15
     / \
    9   20

BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False



Constraints:
The number of nodes in the tree is in the range [1, 10^5].
0 <= Node.val <= 10^6
At most 10^5 calls will be made to hasNext, and next.

Follow up: Could you implement next() and hasNext() to run in average O(1) time and
           use O(h) memory, where h is the height of the tree?
"""


from about_TreeNode import *
"""
解法1: 很容易想到先求得树的中序遍历, next 和 hasNext 就变为数组指针的移动;
"""
class BSTIterator_v1:
    def __init__(self, root: TreeNode):
        self.nodes = []
        # jy: 初始化树时就对树进行中序遍历, 遍历的结果将在 self.nodes 列表中;
        self._inorder(root, self.nodes)
        # jy: 定义 pointer 用于记录调用 next 属性时遍历的具体位置, 初始化为中
        #    序遍历的第一个元素, 即下次调用 next 时需要返回的元素;
        self.pointer = 0


    def next(self) -> int:
        value = self.nodes[self.pointer]
        self.pointer += 1

        return value


    def hasNext(self) -> bool:
        # jy: 如果 pointer 小于树的总元素个数, 则表示还有下一个元素(因为当遍历
        #    到最后一个元素时, self.pointer 将会更新为 len(self.nodes))
        return self.pointer < len(self.nodes)


    def _inorder(self, root, nodes):
        """树的中序遍历"""
        if not root:
            return

        self._inorder(root.left, nodes)
        nodes.append(root.val)
        self._inorder(root.right, nodes)

"""
解法2: Follow up 中要求空间复杂度为 O(h), 而解法 1 的空间复杂度为 O(n), 使用一个栈保存二叉搜索
树的所有左节点, 调用 next 时, 等价于从栈顶出元素, 同时将出栈节点的所有左节点加入到栈中;
"""
class BSTIterator_v2:
    def __init__(self, root: TreeNode):
        self.nodes = []
        current = root

        while current:
            self.nodes.append(current)
            current = current.left

    def next(self) -> int:
        top = self.nodes.pop()
        current = top.right

        while current:
            self.nodes.append(current)
            current = current.left

        return top.val

    def hasNext(self) -> bool:
        return len(self.nodes) > 0


ls_ = [7, 3, 15, None, None, 9, 20]
root = build_binary_tree(ls_)
bSTIterator = BSTIterator_v1(root)
print(bSTIterator.next())    # return 3
print(bSTIterator.next())    # return 7
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 9
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 15
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 20
print(bSTIterator.hasNext())

print(" ================================= ")
bSTIterator = BSTIterator_v2(root)
print(bSTIterator.next())    # return 3
print(bSTIterator.next())    # return 7
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 9
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 15
print(bSTIterator.hasNext()) # return True
print(bSTIterator.next())    # return 20
print(bSTIterator.hasNext())



