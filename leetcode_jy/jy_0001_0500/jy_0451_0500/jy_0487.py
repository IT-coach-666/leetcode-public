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
title_jy = "Max-Consecutive-Ones-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary array, find the maximum number of consecutive 1s in this array if
you can flip at most one 0.


Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
            After flipping, the maximum number of consecutive 1s is 4.


Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000


Follow up:
What if the input numbers come in one by one as an infinite stream? In other words,
you can't store all numbers coming from the stream as it's too large to hold in memory.
Could you solve it efficiently?
"""


from typing import List


class Solution:
    """
解法1: 在 485_Max-Consecutive-Ones.py 的基础上, 增加 prev_length 表示前一个连续
的 1 的长度, 初始化为 -1; 遍历数组: 如果当前数字是 1, 则 length_so_far 加 1, 否
则 prev_length 赋值为 length_so_far, length_so_far 重置为 0; 然后比较
length_so_far + prev_length + 1 和 max_length 的大小, 更新 max_length 的值,
这里加 1 表示反转了一个 0, 而 prev_length 初始化为 -1 也是为了避免特殊处理加 1
的逻辑(如第一个数字为 1 时, 遍历到第一个数字时, max_length 应该为 1, 而如果
prev_length 初始化为 0, 则 max_length 变为了 2);
    """
    def findMaxConsecutiveOnes_v1(self, nums: List[int]) -> int:
        max_length = 0
        length_so_far = 0
        prev_length = -1
        # jy: 遍历数组, length_so_far 保存截止当前数值 1 为止, 连续的 1 的个数;
        #    prev_length 保存上个连续为 1 的长度; 当如果出现连续的两个 0 时, 则
        #    到第二个 0 时, prev_length 和 length_so_far 均为 0;
        for n in nums:
            if n == 1:
                length_so_far += 1
            else:
                prev_length, length_so_far = length_so_far, 0
            # jy: 每一次循环遍历均要进行 max_length 判断;
            max_length = max(length_so_far + prev_length + 1, max_length)

        return max_length

    """
解法2: 在解法 1 中, prev_length 是不包含 0 的, 如果当前数字为 0, 则赋值 prev_length 为
length_so_far + 1, 即包含了一个 0 的长度, 最后比较 length_so_far + prev_length 和
max_length 即可;

JY: 对解法 1 进行微调;
    """
    def findMaxConsecutiveOnes_v2(self, nums: List[int]) -> int:
        max_length = 0
        length_so_far = 0
        prev_length = 0

        for n in nums:
            if n == 1:
                length_so_far += 1
            else:
                prev_length, length_so_far = length_so_far + 1, 0

            max_length = max(length_so_far + prev_length, max_length)

        return max_length

    """
Follow up: 上述解法并不依赖将整个数组加载到内存中, 在流式数据的场景下依然适用:
    """
    def findMaxConsecutiveOnes_v3(self, nums: List[int]) -> int:
        max_length = 0
        length_so_far = 0
        prev_length = -1

        while stream.has_next():
            n = stream.read()

            if n == 1:
                length_so_far += 1
            else:
                prev_length, length_so_far = length_so_far, 0

            max_length = max(length_so_far + prev_length + 1, max_length)

        return max_length


    """
JY: 保留 prev_1_length, current_0_length 和 current_1_length:
1) 当 current_0_length 大于 1 时,
   max_length = max(max(prev_1_length, current_1_length) + 1, max_length)
2) 当 current_0_length 等于 1 时,
   max_length = max(prev_1_length + current_1_length + 1, max_length)
    """
    def findMaxConsecutiveOnes_jy(self, nums: List[int]) -> int:
        max_length = 0
        # prev_0_length = 0
        # prev_1_length = 0
        current_0_length = 0
        current_1_length = 0
        len_ = len(nums)
        i = 0
        while i < len_:
            prev_1_length = current_1_length
            prev_0_length = current_0_length
            current_1_length = 0
            current_0_length = 0
            while i < len_ and nums[i] == 1:
                current_1_length += 1
                i += 1

            while i < len_ and nums[i] == 0:
                current_0_length += 1
                i += 1

            if prev_0_length == 1:
                print("===========1==========")
                max_length = max(prev_1_length + current_1_length + 1, max_length)
            else:
                max_length = max(max(prev_1_length, current_1_length) + 1, max_length)


        return max_length



# nums = [1,0,1,1,0]
nums = [1,0,1,1,0,1]
# Output: 4
res = Solution().findMaxConsecutiveOnes_v1(nums)
print(res)

res = Solution().findMaxConsecutiveOnes_v2(nums)
print(res)

res = Solution().findMaxConsecutiveOnes_jy(nums)
print(res)

# jy: 解法中的 stream 未知
# res = Solution().findMaxConsecutiveOnes_v3(nums)
# print(res)


