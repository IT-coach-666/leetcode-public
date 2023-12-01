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
title_jy = "Serialize-and-Deserialize-N-ary-Tree(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Serialization is the process of converting a data structure or object into a sequence
of bits so that it can be stored in a file or memory buffer, or transmitted across a
network connection link to be reconstructed later in the same or another computer
environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a
rooted tree in which each node has no more than N children. There is no restriction
on how your serialization/deserialization algorithm should work. You just need to
ensure that an N-ary tree can be serialized to a string and this string can be
deserialized to the original tree structure.



For example, you may serialize the following 3-ary tree:
(图: https://www.yuque.com/frederick/dtwi9g/tbc7nb)
as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily need
to follow this format.

Or you can follow LeetCode's level order traversal serialization format, where each
group of children is separated by the null value.
(图见: https://www.yuque.com/frederick/dtwi9g/tbc7nb)
For example, the above tree may be serialized as:
[1, null, 2, 3, 4, 5, null, null, 6, 7, null, 8, null, 9, 10, null, null, 11, null, 12, null, 13, null, null, 14].



You do not necessarily need to follow the above suggested formats, there are many more
different formats that work so please be creative and come up with different approaches
yourself.


Constraints:
The number of nodes in the tree is in the range [0, 10^4].
0 <= Node.val <= 10^4
The height of the n-ary tree is less than or equal to 1000
Do not use class member/global/static variables to store states.
Your encode and decode algorithms should be stateless.
"""



from collections import deque

from about_TreeNode import *



"""
解法1: 和 297_Serialize-and-Deserialize-Binary-Tree.py 类似, 序列化时进行前序遍历, 使用 'None' 作为
孩子节点的结束标记; 反序列化时第一个元素为根节点, 然后只要元素不为空, 则一直递归反序列化作为孩子节
点, 然后弹出空字符串(孩子节点结束的标志);
"""
class Codec_v1:
    def serialize(self, root: 'Node') -> str:
        # jy: 初始化双向列表;
        encoded = deque()
        # jy: 前序遍历, 将遍历结果存入双向列表中;
        self._preorder(root, encoded)
        # jy: 双向列表中的值以 "," 分隔并返回字符串格式;
        return ','.join(list(encoded))


    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        return self._deserialize(deque(data.split(',')))


    def _preorder(self, root, encoded):
        """N 叉树的前序遍历"""
        # jy: 如果节点为空, 直接返回;
        if not root:
            return ''
        # jy: 将当前节点值存入双向列表;
        encoded.append(str(root.val))
        # jy: 如果当前节点的子节点不为空, 则循环遍历子节点(对每个子节点进行递归前序遍历);
        if root.children:
            for child in root.children:
                self._preorder(child, encoded)
        # jy: 每一次深度遍历完一个孩子节点后, 用空字符分割(叶子节点结束后会加 'None', 叶子
        #    节点的父节点如果也是孩子节点, 其结束后也会加 'None', 因此可能会出现连续的多
        #    个 'None');
        # jy: 该方式导致序列化结果中可能会出现过多的 'None';
        encoded.append('None')


    def _deserialize(self, encoded):
        # jy: 构造根节点;
        root_value = int(encoded.popleft())
        root = Node(root_value, [])
        # jy: 如果当前的双向列表中的首个元素不为空字符, 表明其为当前 root 节点的子节点;
        while encoded[0] != 'None':
            child = self._deserialize(encoded)
            root.children.append(child)

        encoded.popleft()

        return root


"""
解法2: 广度优先搜索版本, 序列化时遍历完孩子节点后会往队列中放一个 'None' 节点, 作为孩
子节点的结尾标记;
"""
class Codec_v2:
    def serialize(self, root: 'Node') -> str:
        # jy: 双向列表, 用于存放序列化后的结果;
        encoded = deque()
        # jy: 双向列表, 用户存放待遍历的节点; 先将根节点加入双向列表;
        queue = deque([root]) if root else deque()

        # jy: 如果节点双向列表不为空, 则不断从节点列表左侧出节点元素, 并将该元素加入
        #    到结果列表 encoded 中(即 encoded 列表的值的先后顺序与 节点列表 queue 中
        #    的是一模一样的; 由于 queue 中添加的值需要原加入的值不断出队后才得以不断
        #    添加, 所以需要有 encoded 列表来辅助保存所有元素);
        while queue:
            node = queue.popleft()
            # jy: 如果节点双向列表 queue 左侧出的是 None, 则往结果双向列表 encoded 右侧
            #    加入 'None', 并继续遍历;
            if not node:
                encoded.append('None')
                continue
            # jy: 如果当前节点双向列表中左侧出的不为 None(即表明是一个节点), 则将该节点
            #    值以字符串数值形式加入结果列表;
            encoded.append(str(node.val))
            # jy: 将当前节点的所有下一级子节点全部依次加入双向列表右侧;
            if node.children:
                for child in node.children:
                    queue.append(child)
            # jy: 当前节点的下一层子节点添加完成后, 会往节点列表右侧中加入 None; 如果当前
            #    节点没有下一节点, 也会在 queue 右侧加入 None;
            queue.append(None)

        return ','.join(encoded)


    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        # jy: 将传入的字符串双向列表化;
        encoded = deque(data.split(','))
        # jy: 从列表左侧出一元素, 即树的根节点;
        root = Node(int(encoded.popleft()), [])
        # jy: 将根节点加入双向节点队列 queue 中;
        queue = deque([root])

        # jy: 如果节点双向列表 queue 和 数值双向列表 encoded 均非空, 则不断从节点双向
        #    列表 queue 中左侧出节点, 为该节点添加 children 节点(即 encoded 列表中不
        #    断左侧出队的结果, 直到碰到 'None' 表示当前节点的孩子节点已添加完成);
        while queue and encoded:
            # jy: 从节点列表 queue 左侧出一个节点;
            node = queue.popleft()
            # jy: 为 node 节点添加 children 节点(encoded 列表中, 在碰到 'None' 之前的
            #    数值均为 node 节点的 children 节点对应的数值);
            while encoded[0] != 'None':
                child = Node(int(encoded.popleft()), [])
                node.children.append(child)
                queue.append(child)
            # jy: 如果当前 encoded 左侧元素为 'None', 表明当前 node 节点的 children 节点已
            #    添加完成, 将 encoded 左侧的 'None' 元素出队, 继续循环, 从 queue 中出节点,
            #    并继续为出队的节点设置 children 节点(依据当前的 encoded 列表中的元素进行
            #    设置, 如果左侧值为 'None', 表明当前节点没有 children 节点, 则继续进一步下
            #    一轮循环, 直到节点列表 queue 或数值列表 encoded 中有一方为空为止);
            encoded.popleft()

        return root


ls_N_ary = [1, [3, [5, 6], 2, 4]]
root = build_N_ary_tree(ls_N_ary)
# print(show_N_ary_tree(root))
serialize_res = Codec_v1().serialize(root)
print("====================== serialize_res: ", serialize_res)
res_root = Codec_v1().deserialize(serialize_res)
print("============== deserialize_res(tree): ", show_N_ary_tree(res_root))

print("-" * 88)

ls_N_ary = [1, [3, [5, 6], 2, 4]]
root = build_N_ary_tree(ls_N_ary)
serialize_res = Codec_v2().serialize(root)
# serialize_res:  1,3,2,4,None,5,6,None,None,None,None,None
print("====================== serialize_res: ", serialize_res)
res_root = Codec_v2().deserialize(serialize_res)
print("============== deserialize_res(tree): ", show_N_ary_tree(res_root))

print("\n\n" + "=" * 88 + "\n\n")

ls_N_ary = [1, [2, 3, [6, 7, [11, [14]]], 4, [8, [12]], 5, [9, [13], 10]]]
root = build_N_ary_tree(ls_N_ary)
# print(show_N_ary_tree(root))
serialize_res = Codec_v1().serialize(root)
print("====================== serialize_res: ", serialize_res)
res_root = Codec_v1().deserialize(serialize_res)
print("============== deserialize_res(tree): ", show_N_ary_tree(res_root))

print("-" * 88)

ls_N_ary = [1, [2, 3, [6, 7, [11, [14]]], 4, [8, [12]], 5, [9, [13], 10]]]
root = build_N_ary_tree(ls_N_ary)
serialize_res = Codec_v2().serialize(root)
print("====================== serialize_res: ", serialize_res)
res_root = Codec_v2().deserialize(serialize_res)
print("============== deserialize_res(tree): ", show_N_ary_tree(res_root))


