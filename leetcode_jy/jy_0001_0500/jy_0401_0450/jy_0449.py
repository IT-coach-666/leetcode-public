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
title_jy = "Serialize-and-Deserialize-BST(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Serialization is the process of converting a data structure or object into a sequence of bits so
that it can be stored in a file or memory  buffer, or transmitted across a network connection
link to be  reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree.  There is no restriction
on how your serialization/deserialization algorithm should work. You just need to ensure that a
binary search tree can be serialized to a string and this string can be deserialized to the
original tree structure. The encoded string should be as compact as possible.


Example 1:    https://www.yuque.com/frederick/dtwi9g/muuesq
root: [8,5,10,1,7,null,12]
preorder: [8,5,1,7,10,12]


Note:
Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.
"""


from typing import List
from about_TreeNode import *
from collections import deque


"""
借助 1008_Construct-Binary-Search-Tree-from-Preorder-Traversal.py 作为反序列化的手段, 序
列化时对树进行前序遍历, 以逗号分隔结点的值;
"""
class Codec:

    def serialize(self, root: TreeNode) -> str:
        encoded = []
        self._preorder(root, encoded)
        return ','.join([str(x) for x in encoded])

    def _preorder(self, root: TreeNode, encoded: List[str]) -> None:
        if not root:
            return
        encoded.append(root.val)
        self._preorder(root.left, encoded)
        self._preorder(root.right, encoded)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        # jy: 将前序遍历序列化字符串结果转换为列表;
        decoded = list(map(lambda x: int(x), data.split(',')))
        return self._build_tree(decoded, 0, len(decoded) - 1)

    def _build_tree(self, preorder: List[int], start: int, end: int) -> TreeNode:
        """构建二叉搜索树"""
        if start > end:
            return None
        # jy: 构造根节点(前序遍历的第一个值即为树的根节点值);
        root_value = preorder[start]
        root = TreeNode(root_value)

        # jy: 获取当前根节点的右子树的所有节点(二叉搜索树的前序遍历结果中, 比当前根节点值大的
        #    位置开始部分即为右子树部分);
        right_tree_start = next((i for i in range(start, end + 1) if preorder[i] > root_value), end + 1)
        # jy: 递归构造左子树;
        root.left = self._build_tree(preorder, start + 1, right_tree_start - 1)
        # jy: 递归构造右子树;
        root.right = self._build_tree(preorder, right_tree_start, end)

        return root


'''
JY: 也可以当做普通二叉树的序列化和反序列化:
1) 序列化时, 将二叉树序列化为能使用 build_binary_tree 函数构造出来的形式, 如以下
   的 ls_ 列表的字符串表示形式;
2) 反序列化时, 就是依据 ls_ 列表通过 build_binary_tree 函数构造二叉树;
'''
class Codec_jy:

    def serialize(self, root: TreeNode) -> str:
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
        # return ",".join([str(i) for i in ls_res])


ls_ = [8, 5, 10, 1, 7, None, 12]
# serialize (ls_preoder) : [8, 5, 1, 7, 10, 12]
root = build_binary_tree(ls_)
res_serialize = Codec().serialize(root)
print(res_serialize)

res_deserialize = Codec().deserialize(res_serialize)
print("pre_order: ", pre_order(res_deserialize))

print("="*88)
ls_ = [8, 5, 10, 1, 7, None, 12]
root = build_binary_tree(ls_)
res_serialize = Codec_jy().serialize(root)
print(res_serialize)

print("="*88)
ls_ = [2,1,3]
root = build_binary_tree(ls_)
res_serialize = Codec_jy().serialize(root)
print(res_serialize)


