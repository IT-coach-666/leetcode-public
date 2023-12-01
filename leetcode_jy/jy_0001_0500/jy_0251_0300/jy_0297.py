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
title_jy = "Serialize-and-Deserialize-Binary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
Serialization is the process of converting a data structure or object into a sequence
of bits so that it can be stored in a file or memory buffer, or transmitted across a
network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction
on how your serialization/deserialization algorithm should work. You just need to ensure
that a binary tree can be serialized to a string and this string can be deserialized to
the original tree structure.


Example: You may serialize the following tree:
    1
   / \
  2   3
     / \
    4   5

as "[1, 2, 3, null, null, 4, 5]"


Clarification: The above format is the same as how LeetCode serializes a binary tree. You do
not necessarily need to follow this format, so please be creative and come up with different
approaches yourself.


Note: 
Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.
"""



from typing import Deque
from collections import deque
from about_TreeNode import *


"""
解法1: 序列化时对树进行前序遍历, 保存各结点的值用逗号分隔, 即使节点为空, 也需要加上空字符串进行占位, 便于在反
序列化时处理左右子树; 反序列化时, 字符串的第一个元素为根结点的值, 然后递归调用反序列化左右子树;
"""
class Codec_v1:

    def serialize(self, root):
        """序列化: 对树进行前序遍历, 最终将遍历结果列表中的值以 "," 隔开形成字符串并返回"""
        # jy: deque 是为了高效实现插入和删除操作的双向列表, 适合用于队列和栈;
        encoded = deque()
        self._preorder(root, encoded)
        return ', '.join(list(encoded))


    def deserialize(self, data):
        """反序列化, 将字符串先转换为双向队列, 随后进行反序列化"""
        return self._deserialize(deque(data.split(', ')))


    def _preorder(self, root: TreeNode, encoded: Deque) -> None:
        """前序遍历, 当前节点为 None 时, 也将其加入遍历结果"""
        if not root:
            encoded.append("None")
        else:
            encoded.append(str(root.val))
            self._preorder(root.left, encoded)
            self._preorder(root.right, encoded)


    def _deserialize(self, encoded: Deque) -> TreeNode:
        # jy: 传入的双向列表 encoded 里面的值是字符串形式; 如果值为 'None', 则将其从左
        #    侧移除, 并返回 None; 由于树的前序遍历结果第一个元素不可能为 None, 此逻辑
        #    不是针对第一个元素;
        if encoded[0] == 'None':
            encoded.popleft()
            return None

        # jy: 经过以上对 'None' 的处理, 此处的 root_value 不再会是 'None', 故可以对以下两行进行替换简化:
        # root_value = encoded.popleft()
        # root_value = int(root_value) if root_value != "None" else root_value
        root_value = int(encoded.popleft())

        root = TreeNode(root_value)
        # jy: 先递归构造左子树(由于序列化遍历时会)
        root.left = self._deserialize(encoded)
        root.right = self._deserialize(encoded)

        return root


"""
解法2: 也可以用广度优先搜索求解;
"""
class Codec_v2:
    def serialize(self, root):
        encoded = []
        # jy: 先将根节点加入双向列表中;
        queue = deque([root]) if root else deque()

        # jy: 当列表不为空时, 不断左侧出元素并将其加入结果列表中;
        while queue:
            node = queue.popleft()

            if not node:
                encoded.append('None')
                continue

            # jy: 先将当前节点值加入双向链表;
            encoded.append(str(node.val))
            # jy: 再将当前节点的左, 右子节点加入双向链表, 不断循环迭代就会将中序
            #    遍历结果加入到结果列表中;
            queue.append(node.left)
            queue.append(node.right)

        return ', '.join(encoded)


    def deserialize(self, data):
        if not data:
            return None

        # jy: 先将序列化后的字符串转换为数值双向列表, 并使用第一个值(非 None)构造根节点;
        values = deque(data.split(', '))
        root = TreeNode(int(values.popleft()))
        # jy: 将根节点加入树节点双向列表中;
        queue = deque([root])

        # jy: 如果树节点双向列表和数值双向列表均不为空, 则遍历执行;
        while queue and values:
            # jy: 从树节点双向列表中出一个节点, 为该节点构造左右子节点(左右子节点的对应数值来源于数值
            #    双向列表), 并将左右子节点依次加入树节点双向列表中, 待后续不断左侧出列表为相应节点继
            #    续设置左右子节点, 直到数值双向列表或树节点双向列表中有一个为空时, 则停止;
            node = queue.popleft()
            left_value = values.popleft()
            right_value = values.popleft()

            if left_value != 'None':
                node.left = TreeNode(int(left_value))
                queue.append(node.left)

            if right_value != 'None':
                node.right = TreeNode(int(right_value))
                queue.append(node.right)

        return root



ls_ = [1, 2, 3, None, None, 4, 5]
root = build_binary_tree(ls_)
res = Codec_v1().serialize(root)
print("pre_order-serialize: ", res)
res = Codec_v1().deserialize(res)
print("pre_order-deserialize: ", pre_order(res))

print("="*88)

ls_ = [1, 2, 3, None, None, 4, 5]
root2 = build_binary_tree(ls_)
res2 = Codec_v2().serialize(root2)
print("pre_order-serialize: ", res2)
res3 = Codec_v2().deserialize(res2)
print("pre_order-deserialize: ", pre_order(res3))


