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
title_jy = "Construct-Binary-Tree-from-Preorder-and-Postorder-Traversal(tree)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Return any binary tree that matches the given preorder and postorder traversals.
Values in the traversals pre and post are distinct positive integers.


Example 1:
Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


Note:
1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""


from typing import List
from about_TreeNode import *



class Solution:
    """
解法1: 和 105_Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal.py 一样的思想:
1) 确定根节点
2) 确定左子树的大小, 从而拆分左右子树

不同的是, 前序遍历的第一个元素是根节点, 后序遍历的最后一个元素是根节点, 无法拿根节点去
划分左右子树; 这里可以使用前序遍历的第二个元素去后序遍历中划分左右子树, 对于前序遍历来
说, 存在左子树的情况下, 第二个元素就是左子树的根节点 (但如果不存在左子树时, 则其为右子
树的根节点, 比如 [1, 2], 如果左子树存在, 则 2 是左子树的根节点, 否则是右子树的根节点)

因此答案有多个, 我们只要返回一种情况即可;
    """
    def constructFromPrePost_v1(self, pre: List[int], post: List[int]) -> TreeNode:
        return self._build_tree(pre, 0, len(pre) - 1, post, 0, len(post) - 1)

    def _build_tree(self, pre, pre_start, pre_end, post, post_start, post_end):
        if pre_start > pre_end or post_start > post_end:
            return None
        # jy: 将前序遍历的第一值作为树的根节点;
        root = TreeNode(pre[pre_start])
        # jy: 如果该值已经是前序遍历的最后一个值, 则表明以当前节点为根节点的树构建完成;
        if pre_start == pre_end:
            return root
        # jy: 将前序遍历的第二个值作为左子树的根节点值;
        left_tree_root_value = pre[pre_start + 1]

        # jy: 依据左子树根节点值到后续遍历结果中找出左子树的节点数: 即为后续遍历中
        #    左子树根节点值所在的下标(即此处的 post_left_tree_root_index)与当前后
        #    续遍历的起始下标之间的节点数;
        post_left_tree_root_index = -1
        for i, n in enumerate(post):
            if n == left_tree_root_value:
                post_left_tree_root_index = i
                break
        left_tree_size = post_left_tree_root_index - post_start + 1
        # jy: 依据后续遍历中的左子树节点值所在位置确认左子树的节点总数 left_tree_size, 因此结合前序
        #    遍历中的当前节点(根节点)后的 left_tree_size 个数值作为左子树的前序遍历结果, 后续遍历结
        #    果中的前 left_tree_size 个节点数作为左子树的后续遍历结果, 依据前序遍历和后续遍历结果构
        #    建左子树;
        root.left = self._build_tree(pre, pre_start + 1, pre_start + left_tree_size, post, post_start, post_start + left_tree_size - 1)
        # jy: 依据前序遍历中的当前节点值(根节点值)和随后的 left_tree_size 个数值(左子树的节点值)的后
        #    一数值开始到前序遍历的末尾, 作为右子树的所有节点的前序遍历结果; 依据后续遍历中 left_tree_size
        #    个数值之后到最后一个数值(不包括最后一个数值, 其为根节点)作为右子树的后续遍历结果, 依据
        #    前序遍历结果和后续遍历结果构建右子树;
        root.right = self._build_tree(pre, pre_start + left_tree_size + 1, pre_end, post, post_start + left_tree_size, post_end - 1)

        return root


    """
解法2: 创建一个栈, 遍历前序遍历结果, 将遇到的节点不断入栈, 入栈前的当前节点就是栈顶
的左节点或右节点, 因为前序遍历类似于从上到下, 正好和入栈的顺序相反; 前序遍历中的节点
入栈前, 判断栈顶的元素是否等于后序遍历的当前元素, 如果相等, 则出栈栈顶的元素, 表示后
续遍历对应的当前节点已处理完毕;
    """
    def constructFromPrePost_v2(self, pre: List[int], post: List[int]) -> TreeNode:
        # jy: 将前序遍历的第一个值对应的节点入栈;
        stack = [TreeNode(pre[0])]
        # jy: 记录后续遍历的当前位置;
        j = 0
        # jy: 遍历前序遍历中的第 2 个元素及其之后的所有元素;
        for value in pre[1:]:
            # jy: 依据前序遍历节点值构造树节点, 待加入到栈中;
            node = TreeNode(value)
            # jy: 如果当前栈顶的节点值等于当前后续遍历的节点值, 则出栈(表示该节点已经
            #    构造完成), 同时后续遍历的当前位置进 1;
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            # jy: 经过以上结合后续遍历当前结果出栈后, 栈顶的节点还未构造完成(左或右子节
            #    点可再填充), 如果该节点的左子节点不存在, 则将当前前序遍历的节点作为栈
            #    顶的左子节点, 否则为右子节点;
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            # jy: 随后将当前遍历的前序遍历节点入栈;
            stack.append(node)

        return stack[0]


pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
res = Solution().constructFromPrePost_v1(pre, post)
print(serialize(res))


pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
res = Solution().constructFromPrePost_v2(pre, post)
print(serialize(res))



