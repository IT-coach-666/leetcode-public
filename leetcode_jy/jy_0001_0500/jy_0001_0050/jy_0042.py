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
tag_jy = ""


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
的最高高度的较小者减去 i 处的高度, 所以可以遍历 height, 计算当前高度左边和右
边的最高值, 然后减去当前的高度算出蓄水量
    """
    def trap_v1(self, height: List[int]) -> int:
        count = 0
        for i in range(1, len(height)-1):
            left_max = max(height[0:i], default=0)
            right_max = max(height[i+1:], default=0)
            left_right_min = min(left_max, right_max)
            if left_right_min > height[i]:
                count += left_right_min - height[i]
        return count

    """
解法2: 解法 1 的时间耗在了每次求左右两边的最大高度上, 所以可以事先将左右两边的
最大高度分别计算出来;
    """
    def trap_v2(self, height: List[int]) -> int:
        if not height:
            return 0
        count, length = 0, len(height)
        # jy: 定义一个与列表长度相同的列表, 用于存放对应位置 i (下标)的左
        #    边(含位置 i)的最大高度;
        left_max = [0] * length
        # jy: 同理, 存放对应位置 i (下标)的右边(含位置 i )的最大高度;
        right_max = [0] * length
        # jy: 第一个位置最大高度为自己对应的高度(因为其左边没有高度值了);
        left_max[0] = height[0]
        # jy: 最后一个位置的最大高度为自己对应的高度(因为其右边没值了);
        right_max[length-1] = height[length-1]
        # jy: 初始化到位置 i 为止左边(包含位置 i)的最大高度; 需从左往右初始化;
        for i in range(1, length):
            left_max[i] = max(left_max[i-1], height[i])
        # jy: 初始化到位置 i 为止右边(包含位置 i)的最大高度; 需从右往左初始化;
        for i in range(length-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        # jy: 位置 i 的左右两边的最大高度中的小的一方即: min(left_max[i-1], right_max[i+1])
        for i in range(1, length-1):
            left_right_min = min(left_max[i-1], right_max[i+1])
            if left_right_min > height[i]:
                # jy: 左右两边的两个最高取其低, 与 i 处的高度差即为最优蓄水量;
                count += left_right_min - height[i]
        return count

    """
解法3: (与解法 2 相反)使用两个指针分别从首尾向中间靠拢, 左右指针移动时记录至今为止左边和右
边的最大高度, 如上图所示(见图例对应连接), 当 left_max 小于 right_max 时, left 的蓄水量只取
决于 left_max, 即使 right_max 不是 left 右边所有高度中最大的, 因为即使后来有比 right_max 还
大的蓄水量, 必然也比 left_max 大, 蓄水量也是以 left_max 为准, 同样的当 left_max 大于 right_max
时, right 处的蓄水量已 right_max 为准;
    """
    def trap_v3(self, height: List[int]) -> int:
        if not height:
            return 0
        count = 0
        left, right = 0, len(height)-1
        # jy: 初始化左右两边第1个位置的最高分别为左右两边的高度;
        left_max, right_max = height[left], height[right]
        # jy: 左右两边向中间靠(一次循环只移动一边), 直到左右位置重叠;
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            # jy: 如果当前是右边最高更高一些, 则左边前进 1, 并以左边的
            #    最高为基准计算蓄水量;
            if left_max < right_max:
                count += left_max - height[left]
                left += 1
            # jy: 如果当前是左边最高更高一些, 则右边往左靠近 1, 并以右边的
            #    最高为基准计算蓄水量;
            else:
                count += right_max - height[right]
                right -= 1
        return count

    """
解法4: 栈: 以上解法都是基于垂直方向的蓄水能力, 此处基于水平方向的蓄水能力;
遍历 height, 将当前高度加入到栈中, 如果当前高度大于栈顶(即最近一次入栈的值)的高度,
说明从栈顶的前一个元素(注意是栈顶的前一个元素)到当前高度可以蓄水(即横向的蓄水); 所
以出栈一个元素(出栈后的栈顶即为原来栈顶的前一个元素), 此时的栈顶对应的高度与当前高
度可以蓄水, 蓄水的高度为当前高度与此时栈顶高度的较小值减去出栈元素的高度; 蓄水的宽
度则为当前高度对应的位置减去此时栈顶的位置再减 1 (注意, 不能将当前高度对应位置减去
出栈元素对应的所在位置直接作为蓄水宽度, 因为出栈元素的所在位置与出栈后的栈顶对应的
所在位置不一定是相邻的) ; 可结合画图理解;
    """
    def trap_v4(self, height: List[int]) -> int:
        if not height:
            return 0
        traped_water, i = 0, 0
        # jy: 注意以下 stack 记录的是 height 的下标值;
        stack = []
        while i < len(height):
            # jy: 列表为空时, 对应 False; 此处用 stack[-1] 表示栈顶, 即最近一次进入列表的值;
            #    如果栈顶比当前位置低, 则栈顶出栈(用 current 变量表示), 并计算 current 在左
            #    右两边所处位置的横向蓄水量(为左右两边高度取其小值并与 current 做差所得值 * 宽度);
            while stack and height[stack[-1]] < height[i]:
                # jy: 记录栈顶对应的下标;
                current = stack.pop()
                # jy: 如果栈空, 则退出内部循环;
                if not stack:
                    break
                # jy: 计算 current 与左右两边的跨度;
                distance = i - stack[-1] - 1
                # jy: 左右两边高度取其小值并与 current 做差;
                bounded_height = min(height[i], height[stack[-1]]) - height[current]
                traped_water += distance * bounded_height
            stack.append(i)
            i += 1
        return traped_water

    """
JY: 思路同解法 4;
    """
    def trap_v5(self, height: List[int]) -> int:
        if not height:
            return 0
        traped_water = 0
        stack = [(0, height[0])]
        for i in range(1, len(height)):
            # jy-version-1-Begin -------------------------------------------------------
            # jy: version-1 代码便于理解, 但不是最简化代码;
            """
            if height[i] <= stack[-1][1]:
                stack.append((i, height[i]))
            else:
                while stack and height[i] > stack[-1][1]:
                    top_stack = stack.pop()
                    if not stack:
                        break
                    traped_water += (min(height[i], stack[-1][1]) - top_stack[1]) * (i - stack[-1][0] - 1)
                stack.append((i, height[i]))
            """
            # jy-version-1-End ---------------------------------------------------------
            # jy-version-2-Begin -------------------------------------------------------
            while stack and height[i] > stack[-1][1]:
                top_stack = stack.pop()
                if not stack:
                    break
                traped_water += (min(height[i], stack[-1][1]) - top_stack[1]) * (i - stack[-1][0] - 1)
            stack.append((i, height[i]))
            # jy-version-2-End ---------------------------------------------------------
        return traped_water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = Solution().trap_v5(height)
print(res)

res = Solution().trap_v2(height)
print(res)

res = Solution().trap_v3(height)
print(res)

res = Solution().trap_v4(height)
print(res)


