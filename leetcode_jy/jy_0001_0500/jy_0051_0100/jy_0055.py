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
title_jy = "Jump-Game(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array of non-negative integers ``nums``, you are initially positioned at
the first index of the array. Each element in the array represents your maximum jump
length at that position. Determine if you are able to reach the last index.


Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length
             is 0, which makes it impossible to reach the last index.


Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""


from typing import List


class Solution:
    """
解法1(超时): 递归搜索, 对于 nums 中的每个数字 nums[i], 尝试走 1 至 nums[i] 步
(递归方法中的第 2 个参数记录当前已走到的位置)
    """
    def canJump_v1(self, nums: List[int]) -> bool:
        return self._dfs(nums, 0)

    def _dfs(self, nums, start):
        # jy: 此处的 if 判断也可替换为 start >= len(nums), 但递归时 start 总是不断加 1;
        if start == len(nums):
            return True

        for step in range(nums[start]):
            if self._dfs(nums, start + step + 1):
                return True

        return nums[start] == 0 and start == len(nums) - 1

    """
解法2: 遍历 nums, 记录至今能走到的最远位置, 如果该位置小于当前遍历 nums 时的下标, 则说
明无法到达后面的位置, 否则根据当前步长更新能走到的最远位置
    """
    def canJump_v2(self, nums: List[int]) -> bool:
        # jy: 记录至今能走到的最远位置(位置均用列表下标表示, 初始化为第一个位置下标 0);
        end = 0
        n = len(nums)
        # jy: 遍历列表位置下标 i, 结合该位置 i 以及从该位置能往后跳的步数 nums[i], 更新当
        #    前能跳到的最远距离 end; 如果遍历到当前位置 i 时, 上一步能跳到的最远距离 end
        #    (还没结合当前能跳的最远距离进行更新) 小于当前位置 i, 则说明之前能跳到的最远
        #    距离不能到当前位置 i, 则后续的位置都将无法跳到, 直接返回 False;
        # jy: 遍历时实际上只需要遍历到倒数第二个位置即可, 因为如果能跳到倒数第二个位置(即
        #    下标为 n-2, 只要 nums[n-2] 不为 0, 则就可以往后跳, 此时最后一轮的 end 会更新
        #    为大于或等于 n-1 的值; 最极短的情况下的上一轮只能跳到 n-2 位置, 且 nums[n-2]
        #    的值为 0, 表明从该位置之后不能再继续往后跳了, 此时更新后的 end 也仍然保持在
        #    n-2, 最终返回的也是 False); 当然直接循环到最后一个位置也是可以的, 因为如果能
        #    跳到最后一个位置, 则 end 值会基于最后位置 n-1 的基础上结合最后的 nums[n-1] 进
        #    行更新, 尽管后面没有其它位置可跳, 但 end 能执行到该更新逻辑也表明其能到达最后
        #    一个位置了, 否则会在更新 end 之前就返回 False 了;
        for i in range(n-1):
            step = nums[i]

            if i > end:
                return False
            # jy: 基于当前能走的最大步数更新至今能走到的最远位置;
            end = max(end, i + step)
        # jy: 可以在 for 循环中加入 if 判断满足条件则提前终止循环;
        return end >= n-1

    """
解法3: 同解法 2, 代码更简洁;
    """
    def canJump_v3(self, nums: List[int]) -> bool:
        # jy: 初始化当前能到达最远的位置
        max_i = 0
        # jy: i 为当前位置, jump 是当前位置的跳数
        for i, jump in enumerate(nums):
            # jy: 如果当前位置能到达, 并且当前位置 + 跳数 > 至今能跳到的最远位置 max_i, 则
            # 更新 max_i;
            # if max_i >= i and i + jump > max_i:
            if i + jump > max_i >= i:
                max_i = i + jump
        return max_i >= i



nums = [2, 3, 1, 1, 4]
# Output: true
res = Solution().canJump_v1(nums)
print(res)


nums = [3, 2, 1, 0, 4]
# Output: false
res = Solution().canJump_v2(nums)
print(res)


