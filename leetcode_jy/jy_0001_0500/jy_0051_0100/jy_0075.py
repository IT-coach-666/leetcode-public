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
title_jy = "Sort-Colors(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "双指针 IMP"


"""
Given an array `nums` with `n` objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in
the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and
blue, respectively. You must solve this problem without using the library's
sort function.


Example 1:
Input: nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]

Example 2:
Input: nums = [2, 0, 1]
Output: [0, 1, 2]
 

Constraints:
1) n == nums.length
2) 1 <= n <= 300
3) nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant
extra space?
"""



class Solution:
    """
解法 1: 计算出 0, 1, 2 各自的数量, 然后根据数量依次给数组赋值 (该方法适合
非数值排序)
    """
    def sortColors_v1(self, nums: List[int]) -> None:
        # jy: 此处用列表来统计各数值的个数
        counts = [0] * 3
        for number in nums:
            counts[number] += 1
        j = 0
        # jy: 依据不同颜色的个数, 不断填充数组
        for i, count in enumerate(counts):
            for _ in range(count):
                nums[j] = i
                j += 1


    """
解法 2: 双指针, 只适合三个数值 (颜色) 的排序

使用两个指针 red 和 blue 分别指向数组的首尾 (red, white, blue = 0, 1, 2),
然后不断遍历数组的每一个位置, 如果值为 0 则和 red 指针位置交换, 并让 red
向右移一步, 如果值为 2 则和 blue 指针位置交换, 并让 blue 向左移动一步
    """
    def sortColors_v2(self, nums: List[int]) -> None:
        # jy: 左指针 red 初始化在最左侧, 右指针 blue 初始化为最右侧
        red, blue = 0, len(nums) - 1
        # jy: i 用于对数组进行从左到右的遍历, 只需遍历至右指针为止
        i = 0
        # jy: 注意, i == blue 时也需要遍历, 因为如果此时 nums[i] 为
        #     0 (代表 red), 则需要将其与 red 指针所处的位置进行交换
        while i <= blue:
            # jy: 如果当前位置的值为 0, 则与 red 指针交换 (将 0 替换
            #     到 red 指针处), 并让 red 指针前进 1; 交换后的当前
            #     位置 i 已经明确归为红色, 可进行下一个位置的判断
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
                i += 1
            # jy: 如果当前位置的值为 2, 则与 blue 指针交换 (将 2 替换
            #     到 blue 指针处), 并让 blue 指针减 1; 交换后的当前位
            #     置 i 的结果还不确定是什么值, 还需要对该位置进行判断
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
            # jy: 如果当前位置为 1, 则不需交换, i 移动下一位后继续判断
            else:
                i += 1


nums = [2, 0, 2, 1, 1, 0]
res = Solution().sortColors_v1(nums)
print(nums)


nums = [1, 0, 2, 1, 2, 0]
res = Solution().sortColors_v2(nums)
print(nums)


