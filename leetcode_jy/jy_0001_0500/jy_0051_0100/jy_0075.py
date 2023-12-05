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
tag_jy = ""


"""
Given an array with n objects colored red, white or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order
red, white and blue. Here, we will use the integers 0, 1, and 2 to represent
the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
Example:
Input: [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]


Follow up:
• A rather straight forward solution is a two-pass algorithm using counting sort.
  First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
  array with total number of 0's, then 1's and followed by 2's.
• Could you come up with a one-pass algorithm using only constant space?
"""



from typing import List
class Solution:
    """
解法1: 第一种解法是计算出 0, 1, 2 各自的数量, 然后根据数量依次给数组赋值; 该方法适合
非数值排序;
    """
    def sortColors_v1(self, nums: List[int]) -> None:
        # jy: 此处用列表来统计各数值的个数;
        counts = [0] * 3
        for number in nums:
            counts[number] += 1
        j = 0
        # jy: 依据不同颜色的个数, 不断填充数组;
        for i, count in enumerate(counts):
            for _ in range(count):
                nums[j] = i
                j += 1


    """
解法2: 使用两个指针 red 和 blue 分别指向数组的首尾(red, white, blue = 0, 1, 2), 然后
遍历数组, 如果遇到 0, 则和 red 交换数字, 同时 red 向右移动一步, 如果遇到 2, 则和 blue 交
换数字, 同时 blue 向左移动一步;

jy: 该方法只适合三个数值(颜色)的排序;
    """
    def sortColors_v2(self, nums: List[int]) -> None:
        # jy: 指定左右指针位置, 左 red 右 blue;
        red, blue = 0, len(nums) - 1
        # jy: i 用于对数组进行从左到右的遍历;
        i = 0
        while i <= blue:
            # jy: 碰到 0 则与左指针(red)交换(将 0 替换到 red 指针处), 且 red 指针前进 1;
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
            # jy: 碰到 2 则与右指针(blue)交换(将 2 替换到 blue 指针处), 且 blue 指针减 1;
            #    此时 i 需要减 1, 使得与后续加 1 抵消, 即还是对原来的位置的值(即从原先 blue
            #    指针替换回的值)进行再次判断, 因为原先 blue 指针的值不确定是多少;
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
                i -= 1
            i += 1


nums = [2, 0, 2, 1, 1, 0]
res = Solution().sortColors_v1(nums)
print(nums)


nums = [1, 0, 2, 1, 2, 0]
res = Solution().sortColors_v2(nums)
print(nums)


