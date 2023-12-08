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
title_jy = "Next-Greater-Element-I(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
The next greater element of some element ``x`` in an array is the first greater
element that is to the right of ``x`` in the same array.

You are given two distinct 0-indexed integer arrays ``nums1`` and ``nums2``,
where ``nums1`` is a subset of ``nums2``. For each 0 <= i < nums1.length, find
the index ``j`` such that nums1[i] == nums2[j] and determine the next greater
element of nums2[j] in ``nums2``. If there is no next greater element, then the
answer for this query is -1.

Return an array ``ans`` of length ``nums1.length`` such that ans[i] is the next
greater element as described above.


Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
             4 is underlined in nums2 = [1,3,4,2]. There is no next greater element,
             so the answer is -1. 1 is underlined in nums2 = [1,3,4,2]. The next greater
             element is 3. 2 is underlined in nums2 = [1,3,4,2]. There is no next greater
             element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
             2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3. 4 is underlined
             in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.


Constraints:
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 10^4
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
"""


from typing import List


class Solution:
    """
维护一个单调递减的栈, 遍历 nums2, 如果当前数字大于栈顶的元素, 则持续出栈, 出栈
的数字的下一个比其大的数就是当前数字, 将映射关系保存到 Map 中
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_elements = {}
        stack = []
        result = []
        # jy: 遍历 nums2, 如果当前数字大于 stack 栈顶元素, 则持续出栈, 出栈的数字的下
        #     一个比其大的数字就是当前数字, 将其映射关系保存到字典 greater_elements 中;
        for n in nums2:
            while stack and stack[-1] < n:
                greater_elements[stack.pop()] = n
            stack.append(n)
        # print("stack_", stack)
        # jy: 由于 nums1 中的数值都是在 nums2 中存在的, 则经过以上 for 循环后, greater_elements
        #     已经保存了 nums2 中的数值的后一个比其大的数字(如果后面没有比其大的数值, 则不会被记录);
        for n in nums1:
            result.append(greater_elements.get(n, -1))

        return result


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
# Output: [-1,3,-1]
res = Solution().nextGreaterElement(nums1, nums2)
print(res)


nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
# Output: [3,-1]
res = Solution().nextGreaterElement(nums1, nums2)
print(res)


