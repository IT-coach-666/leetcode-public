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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Move-Zeroes(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.


Example:
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]


Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

JY: 题目变形: 将所有 0 放置到最右边; 解题思路同理;
"""


from typing import List


class Solution:
    """
解法1: tail 初始化为数组中第一个位置下标 0 (tail 即表示遍历到数组 nums 的位置 i 时, 截止
当前位置 i 为止, 非零数值存放于数组左侧的末尾位置), 遍历数组中的数值, 如果数值非 0, 则将
其放在 tail 处, 并将 tail 加 1 (注意, 并不需要确保 tail 的初始下标位置对应的值是 0, 如果
最开始即为非 0, 则遍历数组 nums 的初始元素时(i = 0), 就会使得 nums[tail] = nums[i], 即
nums[0] = nums[0], 随后 tail 和 i 都会右移, 后续逻辑同理, 直到 tail 下标对应的数值为 0, 此
时会找到一个位置下标 i, 其对应的数值为非 0, 会赋值到下标位置 tail 中, 并使得 tail 进一步加
1); 遍历完整个数组中的数值后, 所有非 0 数值都将会被放置到数组的前端, 此时从tail 处开始之后
的数值都应更新为 0;
    """
    def moveZeroes_v1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tail = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[tail] = nums[i]
                tail += 1

        for i in range(tail, len(nums)):
            nums[i] = 0

    """
解法2: 优化解法 1, 减少一次 for 循环; 初始化 tail 指向数组中第一个位置, 遍历数组, 如果
数字非 0, 交换 tail 和 i 处的数字(如果 tail 初始位置上的值不为 0, 则 i 为 0 时就会与 tail
进行交换, 即相同位置赋值操作, 此时 tail 和 i 也都会同时前进一位, 继续后续的判断), 并
将 tail 加 1;
    """
    def moveZeroes_v2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tail = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail += 1


nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
res = Solution().moveZeroes_v1(nums)
print(nums)

nums = [0, 1, 0, 3, 12]
res = Solution().moveZeroes_v2(nums)
print(nums)


