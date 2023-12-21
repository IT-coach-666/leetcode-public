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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "trapping-rain-water(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "双指针 | 列表缓存 | 栈"


"""
Given `n` non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it is able to trap after raining.


Example 1:
https://www.yuque.com/it-coach/leetcode/zr7st5
Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Explanation: The above elevation map (black section) is represented by array
             [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]. In this case, 6 units of 
             rain water (blue section) are being trapped.

Example 2:
Input: height = [4, 2, 0, 3, 2, 5]
Output: 9
 

Constraints:
1) n == height.length
2) 1 <= n <= 2 * 10^4
3) 0 <= height[i] <= 10^5
"""



class Solution:
    """
解法 1: 对于图例中的 i 处来说, 它的蓄水能力等同于 i 左边的最高高度和 i 右边
的最高高度的较小者减去 i 处的高度, 所以可以遍历 height, 计算当前高度左边和
右边的最高值, 然后减去当前的高度算出当前位置 i 的蓄水量
    """
    def trap_v1(self, height: List[int]) -> int:
        count = 0
        for i in range(1, len(height)-1):
            left_max = max(height[0: i], default=0)
            right_max = max(height[i+1: ], default=0)
            left_right_min = min(left_max, right_max)
            # jy: 判断当前高度与左右两边能否构成蓄水池
            if left_right_min > height[i]:
                count += left_right_min - height[i]
        return count


    """
解法 2: 列表缓存, 优化解法 1 

解法 1 的时间耗在每次求左右两边的最大高度上, 实际上可以事先将左右两边的
最大高度分别计算出来
    """
    def trap_v2(self, height: List[int]) -> int:
        if not height:
            return 0

        count, length = 0, len(height)

        # jy: left_max[i] 记录下标位置 i 左侧 (含位置 i) 的最大高度
        left_max = [0] * length
        # jy: 第一个下标位置的最大高度为自己对应的高度 (因为左边没有高度值)
        left_max[0] = height[0]
        # jy: 从第二个下标位置开始, 从左往右初始化 left_max 的值
        for i in range(1, length):
            left_max[i] = max(left_max[i-1], height[i])

        # jy: right_max[i] 记录下标位置 i 右侧 (含位置 i) 的最大高度
        right_max = [0] * length
        # jy: 最后一个下标位置的最大高度为自己对应的高度 (因为右边没有高度值)
        right_max[length-1] = height[length-1]
        # jy: 从倒数第二个下标位置开始, 从后往前初始化 right_max
        for i in range(length-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        # jy: 下标位置 i 的左右两边的最大高度中的小的一方即: 
        #     min(left_max[i-1], right_max[i+1])
        for i in range(1, length-1):
            left_right_min = min(left_max[i-1], right_max[i+1])
            # jy: 判断当前高度与左右两边能否构成蓄水池
            if left_right_min > height[i]:
                count += left_right_min - height[i]
        return count


    """
解法 3: 双指针

双指针位置初始化为列表首末位置, 并均向中间靠拢, 移动时记录至今为止左边和
右边的最大高度:
1) 当 left_max < right_max 时, 下标位置为 left 的蓄水量取决于 left_max
2) 当 left_max 大于 right_max 时, 下标位置为 right 处的蓄水量取决于 right_max
    """
    def trap_v3(self, height: List[int]) -> int:
        if not height:
            return 0

        count = 0
        left, right = 0, len(height)-1
        # jy: 初始化左右两侧的最大高度
        left_max, right_max = height[left], height[right]
        # jy: 左右两边向中间靠(一次循环只移动相对较低的一边), 直到左右位置重叠
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            # jy: 如果当前是右侧最大高度更高一些, 则以左边的最大高度为基准计算
            #     当前位置的蓄水量, 然后左指针前进 1
            if left_max < right_max:
                count += left_max - height[left]
                left += 1
            # jy: 如果当前是左侧最大高度更高一些, 则以右边的最大高度为基准计算
            #     当前位置的蓄水量, 然后右指针往左缩进 1
            else:
                count += right_max - height[right]
                right -= 1
        return count


    """
解法 4: 栈: 以上解法都是基于垂直方向的蓄水能力, 此处基于水平方向的蓄水能力

遍历 height, 将当前高度加入到栈中, 如果当前高度大于栈顶 (即最近一次入栈的值)
的高度, 说明从栈顶的前一个元素 (注意是栈顶的前一个元素) 到当前高度可以蓄水
(即横向的蓄水); 所以出栈一个元素 (出栈后的栈顶即为原来栈顶的前一个元素), 此
时的栈顶对应的高度与当前高度可以蓄水:
横向蓄水的高度 = 左右两边高度取较小值 - 栈顶元素的高度
横向蓄水的宽度 = 当前高度的下标位置 - 栈顶的前一个元素的下标位置 - 1 
    
注意: 
蓄水宽度 != 当前高度对应位置 - 出栈元素对应的所在位置
因为出栈元素的所在位置与出栈后的栈顶对应的所在位置不一定是相邻的
    """
    def trap_v4(self, height: List[int]) -> int:
        if not height:
            return 0
        traped_water = 0
        # jy: 用栈 stack 记录 height 的下标位置
        stack = []
        # jy: 遍历列表中的各个高度的下标位置
        for i in range(len(height)):
            # jy: 当栈不为空, 且栈顶对应的下标位置 stack[-1] 比当前下标位置对
            #     应的高度低时, 表明栈顶的前一个下标位置与当前下标位置对应的高
            #     度之间能蓄水, 此时可以计算横向蓄水量
            while stack and height[stack[-1]] < height[i]:
                # jy: 栈顶对应的下标位置出栈, 如果出栈后栈为空, 表明栈顶的前一
                #     个元素不存在, 不能进行蓄水, 直接退出内部循环
                top_stack = stack.pop()
                if not stack:
                    break

                # jy: 计算横向蓄水的宽度 (经过以上栈顶元素出栈后, stack[-1] 表
                #     示栈顶前一个元素的下标位置): 
                #     当前高度的下标位置 - 栈顶的前一个元素的下标位置 - 1
                distance = i - stack[-1] - 1
                # jy: 计算横向蓄水的高度: 左右两边高度取其小值 - 栈顶元素的高度
                bounded_height = min(height[i], height[stack[-1]]) - height[top_stack]
                traped_water += distance * bounded_height
            # jy: 每次都将当前下标位置入栈
            stack.append(i)
        return traped_water


    """
解法 5: 思路同解法 4, 但栈中直接存储 (高度对应的下标位置, 高度值)
    """
    def trap_v5(self, height: List[int]) -> int:
        if not height:
            return 0

        traped_water = 0

        stack = [(0, height[0])]
        for i in range(1, len(height)):
            # jy: 判断当前高度与栈中的高度是否能蓄水, 如果能, 则计算横向蓄水量
            while stack and height[i] > stack[-1][1]:
                top_stack = stack.pop()
                if not stack:
                    break

                distance = i - stack[-1][0] - 1
                bounded_height = min(height[i], stack[-1][1]) - top_stack[1]
                traped_water += bounded_height * distance
            # jy: 每次均将当前位置的下标位置和高度入栈
            stack.append((i, height[i]))
        return traped_water



height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = Solution().trap_v1(height)
print(res)

res = Solution().trap_v2(height)
print(res)

res = Solution().trap_v3(height)
print(res)

res = Solution().trap_v4(height)
print(res)

res = Solution().trap_v5(height)
print(res)
