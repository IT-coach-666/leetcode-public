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
title_jy = "Maximum-XOR-of-Two-Numbers-in-an-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array ``nums``, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n

Follow up: Could you do this in O(n) runtime?


Example 1:
Input: nums = [3, 10, 5, 25, 2, 8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:
Input: nums = [0]
Output: 0

Example 3:
Input: nums = [2, 4]
Output: 6

Example 4:
Input: nums = [8, 10, 2]
Output: 10

Example 5:
Input: nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
Output: 127


Constraints:
1 <= nums.length <= 2 * 10^4
0 <= nums[i] <= 2^31 - 1
"""

import sys
from typing import List


class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}
        self.value = 0


class Solution:
    """
Trie 的应用;
首先将所有数字的二进制表示插入到 Trie 中, Trie 的搜索表示寻找和入参的 bits 作 XOR 运算后
的最大值;

根据 XOR 的性质, 相同位置上的数不同得 1, 所以搜索时优先选择各自比特位不同的路径; 最后遍
历数组, 搜索每个数字在 Trie 中的 XOR 最大值;

JY: 此处算法的时间复杂度为 O(n^2), 且空间复杂度较高, 待优化
    """
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        max_xor = -sys.maxsize

        for n in nums:
            # jy: bin(n) 实现将数值 n 转换为二进制表示(字符串形式), 前两个字符为固定的 "0b", 如 bin(3) 为 "0b11"
            #    zfill(x) 表示在字符串左侧用 "0" 填充, 直到字符串长度为 x 为止; 此处即假设对应数值 n 的二进制表
            #    示不会超过 31 位, 最大为 31 个 "1", 即 2^31 - 1 (符合题目中的 constraints 中的要求)
            bits = (bin(n)[2:]).zfill(31)
            # jy: 将数值的二进制字符串形式插入到 Trie 字典树中, 并将最后一个字符对应的 TrieNode 的 end_of_word
            #    属性设置为 True, 且 value 属性记录该二进制表示的对应数值;
            # jy: end_of_word 属性可以去掉, 并通过 value 属性值来判断是否有该值存在即可(需要将 TrieNode 的 value
            #    属性的默认值修改为 -1, 因为 nums[i] 是大于或等于 0 的数, 如果后续 Trie 树的某 字符对应的节点的
            #    value 属性值不为 -1, 则表示截止该字符对应的 TrieNode 节点构成一个已存在的数值, 值为 value 属性值)
            self._insert(root, bits, n)

            max_xor = max(max_xor, self._search(root, bits, n))

        return max_xor


    def _insert(self, root, bits, value):
        """
        将数值的二进制字符串形式插入到 Trie 字典树中, 并将最后一个字符对应的 TrieNode 的 end_of_word
        属性设置为 True, 且 value 属性记录该二进制表示的对应数值;

        end_of_word 属性可以去掉, 并通过 value 属性值来判断是否有该值存在即可(需要将 TrieNode 的 value
        属性的默认值修改为 -1, 因为 nums[i] 是大于或等于 0 的数, 如果后续 Trie 树的某 字符对应的节点的
        value 属性值不为 -1, 则表示截止该字符对应的 TrieNode 节点构成一个已存在的数值, 值为 value 属性值)
        """
        current = root

        for bit in bits:
            if bit not in current.children:
                current.children[bit] = TrieNode()

            current = current.children[bit]

        current.end_of_word = True
        current.value = value


    def _search(self, root, bits, target):
        """
        在当前的 Trie 树中找出与 bits 进行异或运算后值最大的结果
        bits 为 target 的二进制表示形式(字符串);
        """
        current = root
        # jy: 遍历 bits 字符串;
        for bit in bits:
            # jy: 如果当前字符为 "1", 且 "0" 字符在 Trie 树的当前 TrieNode 节点中, 则
            #    当前 TrieNode 节点更新为 "0" 字符对应的 TrieNode 节点, 使得每轮循环
            #    都能与 Trie 树中的对应字符一一同步(以下同理);
            if bit == '1' and '0' in current.children:
                current = current.children['0']
            # jy: 如果当前字符为 "0", 且 "1" 字符在 Trie 树的当前 TrieNode 节点中, 则
            #    当前 TrieNode 节点更新为 "1" 字符对应的 TrieNode 节点;
            elif bit == '0' and '1' in current.children:
                current = current.children['1']
            # jy: 如果当前字符为 "0" 且 "1" 不在 Trie 树的当前 TrieNode 节点中, 或当前
            #    字符为 "1" 且 "0" 不在 Trie 树的当前 TrieNode 节点中, 即表明当前字符
            #    bit 在 Trie 树的当前 TrieNode 节点中, 则当前 TrieNode 节点更新为 bit
            #    字符对应的 TrieNode 节点;
            elif bit in current.children:
                current = current.children[bit]
            # jy: 注意, 以下的 else 部分是多余的, 因为不存在除了以上之外的其它可能情况(LeetCode 已验证)
            # else:
            #     break

        # jy: 跳出循环后, 将 target 与 current.value (如果以某二进制字符结尾的数值存在, 则 current.value
        #    有其对应的数值, 否则为 0 或 -1, 取决于默认值设置为多少; -1 也是可以的, 因为正数与 -1 做异或
        #    运算的结果为负数, 不影响逻辑过程) 做异或运算;
        return target ^ current.value


nums = [3, 10, 5, 25, 2, 8]
# Output: 28
res = Solution().findMaximumXOR(nums)
print(res)


nums = [0]
# Output: 0
res = Solution().findMaximumXOR(nums)
print(res)


nums = [2, 4]
# Output: 6
res = Solution().findMaximumXOR(nums)
print(res)


nums = [8, 10, 2]
# Output: 10
res = Solution().findMaximumXOR(nums)
print(res)


nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
# Output: 127
res = Solution().findMaximumXOR(nums)
print(res)


# jy: bin(x) 和 zfill(x) 的应用示例:
"""
print(bin(3)[2:].zfill(5))
print(type(bin(3)))
print("asa".zfill(6))

print(2 ^ -1)
"""


