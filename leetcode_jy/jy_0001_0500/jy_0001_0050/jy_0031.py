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
title_jy = "Next-Permutation(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Implement next permutation, which rearranges numbers into the lexicographically next
greater permutation of numbers. If such an arrangement is not possible, it must rearrange
it as the lowest possible order (i.e., sorted in ascending order). The replacement must
be in place and use only constant extra memory.


Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:
Input: nums = [1]
Output: [1]


Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""




class Solution:
    """
同 556_Next-Greater-Element-III.py, 额外增加当不存在下一个较大值时将数组反转;
函数不返回任何值, 因为是 in-place 置换;
    """
    def nextPermutation(self, nums: List[int]) -> None:
        # jy: 如果数组是降序排序, 反转其为升序;
        i = len(nums) - 1
        while i-1 >= 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i == 0:
            # jy: 在 556_Next-Greater-Element-III.py 的基础上补充对数组进行倒序排列;
            nums.reverse()
            return
        # jy: 截止当前 i 位置, 其右侧的数据均是降序排序的
        j = i
        while j+1 < len(nums) and nums[j+1] > nums[i-1]:
            j += 1

        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = nums[i:][::-1]



nums = [1,2,3]
# Output: [1,3,2]
Solution().nextPermutation(nums)
print(nums)


nums = [3,2,1]
# Output: [1,2,3]
Solution().nextPermutation(nums)
print(nums)


nums = [1,1,5]
# Output: [1,5,1]
Solution().nextPermutation(nums)
print(nums)


nums = [1]
# Output: [1]
Solution().nextPermutation(nums)
print(nums)


