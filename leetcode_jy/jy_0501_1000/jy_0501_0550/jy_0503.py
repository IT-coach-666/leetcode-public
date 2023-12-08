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
title_jy = "Next-Greater-Element-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a circular integer array ``nums`` (i.e., the next element of nums[nums.length - 1]
is nums[0]), return the next greater number for every element in ``nums``.

The next greater number of a number ``x`` is the first greater number to its
traversing-order next in the array, which means you could search circularly to
find its next greater number. If it doesn't exist, return -1 for this number.


Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; The number 2 can't find next
             greater number. The second 1's next greater number needs to search
             circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]


Constraints:
1 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
"""


from typing import List


class Solution:
    """
和 496_Next-Greater-Element-I.py 类似, 同样是维护一个单调递减的栈, 不过保存的不
是数字的值, 而是数字所在数组中的下标, 这样当栈顶表示的数字小于当前数字时, 就可以
取出栈顶的下标, 该下标表示的数字的下一个较大值就是当前数字;

注意这里循环的次数是数组长度的 2 倍, 因为数组是循环数组, 所以循环两次保证排在每个
数字后面的数字都能被访问到
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # jy: 先初始化 result 的值均为 -1 (表示在该相应下标位置之后没找到比该位置下
        #     标对应的值更大的数值), 后续查找过程中, 如果找到, 则会对相应位置的值进
        #     行更新;
        stack, result = [], [-1] * len(nums)

        for i in range(len(nums) * 2):
            # jy: 获取当前循环对应下标的数值(由于下标可能大于等于 len(nums), 因此获取
            #     当前循环的下标时要基于 len(nums) 取余数)
            n = nums[i % len(nums)]
            # jy: stack 中记录的是数值对应的下标, stack 会将数值的所有下标都记录到;
            #     如果当前数值比 stack 栈顶的下标的对应数值大, 则不断出栈顶下标, 将
            #     该下标位置下的 result 值设置为当前数值 n, 即找到了该下标位置对应的
            #     原数值之后的第一个比其大的数值;
            while stack and nums[stack[-1]] < n:
                result[stack.pop()] = n

            if i < len(nums):
                stack.append(i)

        return result


nums = [1, 2, 1]
# Output: [2,-1,2]
res = Solution().nextGreaterElements(nums)
print(res)


nums = [1, 2, 3, 4, 3]
# Output: [2,3,4,-1,4]
res = Solution().nextGreaterElements(nums)
print(res)


