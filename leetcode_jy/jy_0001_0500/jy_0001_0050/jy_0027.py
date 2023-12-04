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
title_jy = "remove-element(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "循环"



"""
给定一个数组 nums 和一个值 val, 原地移除所有数值等于 val 的元素, 并返回移
除后数组的新长度; 不能使用额外的数组空间, 空间复杂度需为 O(1); 元素的顺序
可以改变, 不需考虑数组中超出新长度后面的元素


示例 1:
输入: nums = [3, 2, 2, 3], val = 3
输出: 2, nums = [2, 2]
解释: 返回新的长度 2, 且 nums 中的前两个元素均为 2; 不需要考虑数组中超出新
      长度后面的元素; 例如, 函数返回的新长度为 2, 而 nums = [2, 2, 3, 3] 或
      nums = [2, 2, 0, 0]

示例 2:
输入: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
输出: 5, nums = [0, 1, 3, 0, 4]
解释: 函数应该返回新的长度 5, 且 nums 中的前五个元素为 0, 1, 3, 0, 4
      注意: 这五个元素可为任意顺序
 

Notes:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""


class Solution:
    """
解法 1: 循环
    """
    def removeElement_v1(self, nums: List[int], val: int) -> int:
        len_ = 0
        for x in nums:
            if x != val:
                nums[len_] = x
                len_ += 1
        return len_ 



nums = [3, 2, 2, 3]
val = 3
# jy: 2, nums = [2, 2]
res = Solution().removeElement_v1(nums, val)
print(res)


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
# jy: 5, nums = [0, 1, 3, 0, 4]
res = Solution().removeElement_v1(nums, val)
print(res)




