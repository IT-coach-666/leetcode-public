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
title_jy = "Jump-Game-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of non-negative integers ``nums``, you are initially positioned at
the first index of the array. Each element in the array represents your maximum jump
length at that position. Your goal is to reach the last index in the minimum number
of jumps. You can assume that you can always reach the last index.


Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
             Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2


Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
"""


from typing import List


class Solution:
    """
解法1: 在 055_Jump-Game.py 的基础上记录上一跳所在的位置, 当上一跳所在的位置等于当前 nums
中的元素的位置, 则说明需要进行下一跳; 以 nums 为 [2, 3, 0, 1, 4] 作为示例进行思考;
    """
    def jump_v1(self, nums: List[int]) -> int:
        # jy: 记录最少需要几跳能使最终跳到末尾位置(题目中已确保肯定能跳到最后);
        jumps = 0
        # jy: 判断跳一次之后的所在位置, 初始化为第一个位置(下标为 0)
        current_end = 0
        # jy: 记录从当前位置以及之前的位置往后跳一次, 能往后跳到的最远距离; 初始化为当前位置;
        max_end = 0
        # jy: 从位置 0 开始循环遍历所在位置, 遍历到倒数第二个位置(即 n-2)即可;
        # jy: 注意, 针对该问题, 当循环到最后一个位置(即 n-1)时则会报错, 必须循环到倒数第二个
        #     位置(不像 055_Jump-Game.py 中, 可循环到倒数第二个位置或最后一个位置)
        for i in range(len(nums) - 1):
            # jy: 记录从当前位置 i 的跳数;
            step = nums[i]
            # jy: 基于当前能跳到的最大位置, 更新当前位置以及之前的位置往后跳一次能跳到的最远位置;
            max_end = max(max_end, i + step)
            # jy: 当上一跳所能跳到的最远位置(即 current_end)等于当前位置 i 时, 进行下一跳(jumps 跳
            #     数加 1), 同时 current_end 更新为截止当前位置 i 以及之前的位置, 往后跳一次能跳到的
            #     最远位置;
            if i == current_end:
                jumps += 1
                current_end = max_end

        return jumps

    """
解法2: 思路同解法1, 代码略有区别
    """
    def jump_v2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        jumps = 0
        current_end = 0
        max_end = 0
        # jy: 此处与解法 1 的区别在于, 循环时必须循环到最后一个位置;
        for i in range(len(nums)):
            # jy: 当 current_end 小于 i 时, 表明需要跳一次了, 则跳一次, 并将此次一跳
            #     能跳到的最远距离赋值给 current_end
            if current_end < i:
                jumps += 1
                current_end = max_end
            max_end = max(max_end, i + nums[i])
        return jumps


nums = [2, 3, 1, 1, 4]
# Output: 2
res = Solution().jump(nums)
print(res)


nums = [2, 3, 0, 1, 4]
# Output: 2
res = Solution().jump(nums)
print(res)


