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
title_jy = "Largest-Rectangle-in-Histogram(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "单调递增栈 + 边界处理 | 相似题: 0085 | IMP"



"""
Given an array of integers `heights` representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle
in the histogram.


Example 1: 图示参考: https://www.yuque.com/it-coach/leetcode/srglxmgx5mcq8l2i
Input: heights = [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1. The largest
             rectangle is shown in the red area, which has an area = 10 units.

Example 2: 图示参考: https://www.yuque.com/it-coach/leetcode/srglxmgx5mcq8l2i
Input: heights = [2,4]
Output: 4


Constraints:
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""


class Solution:
    """
解法 1: 暴力求解 (循环 + 双指针), 时间复杂度 O(n^2), 超时

以第 i 根柱子为最矮柱子所能延伸的最大面积为: 以 i 为中心, 分别向左右两
边找第一个小于 heights[i] 的位置, 记为 left_i 和 right_i, 则最大面积为:
heights[i] * (right_i - left_i - 1)

遍历所有的位置 i 求解不同位置 i 下能取得的最大面积, 取最大值即可
    """
    def largestRectangleArea_v1(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        # jy: 遍历每一个下标位置 i, 并寻找到对应的 left_i 和 right_i,
        #     即可求以当前位置 i 的柱子为最矮柱子所能延伸的最大面积
        for i in range(n):
            left_i = i
            right_i = i
            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1
            res = max(res, (right_i - left_i - 1) * heights[i])
        return res


    """
解法 2: 类动态规划

优先求解出每个位置 i 的 left_i 和 right_i, 存储到 ls_left 和 ls_right 中,
随后遍历一次 heights 中每个位置下的数值, 即可求解出基于该位置的最大面积,
取所有位置中面积最大的即为目标结果
    """
    def largestRectangleArea_v2(self, heights: List[int]) -> int:
        if not heights:
            return 0

        n = len(heights)
        # jy: ls_left[i] 为左侧第一个比 heights[i] 小的位置下标
        ls_left = [0] * n
        # jy: 左侧第一个比 heights[0] 小的位置下标为 -1
        ls_left[0] = -1

        # jy: ls_right[i] 为右侧第一个比 heights[i] 小的位置下标
        ls_right = [0] * n
        # jy: 右侧第一个比 heights[-1] 小的位置下标为 n
        ls_right[-1] = n

        # jy: 求解 ls_left 中每一个位置中的数值 (以 [2, 1, 5, 6, 2, 3] 为例)
        for i in range(1, n):
            # jy: 找出下标位置 i 左侧第一个比 heights[i] 小的数值的下标位置:
            #     先将下标位置初始化为 i-1 (因为是要找左侧的), 如果 tmp 下标
            #     对应的高度比 i 下标对应的高度大, 则将 tmp 更新为左侧第一个
            #     比该位置的高度小的下标位置 (即 ls_left[tmp]); 由于 ls_left[i]
            #     的求解依赖于 i 左侧的下标位置, 因此需从左到右逐个求解
            tmp = i - 1
            while tmp >= 0 and heights[tmp] >= heights[i]:
                tmp = ls_left[tmp]
            ls_left[i] = tmp
        # jy: ls_left: [-1, -1, 1, 2, 1, 4]
        #print("ls_left: %s" % ls_left)

        # jy: 求解 ls_right 中每一个位置中的数值 (以 [2, 1, 5, 6, 2, 3] 为例)
        for i in range(n - 2, -1, -1):
            # jy: 找出下标位置 i 右侧第一个比 heights[i] 小的数值的下标位置:
            #     先将下标位置初始化为 i+1 (因为是要找右侧的), 如果 tmp 下标
            #     对应的高度比 i 下标对应的高度大, 则将 tmp 更新为右侧第一个
            #     比该位置的高度小的下标位置 (即 ls_right[tmp]); 由于 ls_right[i]
            #     的求解依赖于 i 右侧的下标位置, 因此需从后往前求解
            tmp = i + 1
            while tmp < n and heights[tmp] >= heights[i]:
                tmp = ls_right[tmp]
            ls_right[i] = tmp
        # jy: ls_right: [1, 6, 4, 4, 6, 6]
        #print("ls_right: %s" % ls_right)

        res = 0
        for i in range(n):
            res = max(res, (ls_right[i] - ls_left[i] - 1) * heights[i])
        return res


    """
解法 3: 改写解法 2, 基于单调递增栈寻找找 left_i 和 right_i


用栈解决问题时, 如果遍历完所有数值后栈不为空, 则还需要一步处理: 弹出栈中所有
元素, 分别计算最大面积 (参见解法 5)

当在 heights 的前后添加两个 0 后, 则栈一定不会为空, 最终结束后栈中存放的是前
后添加的 0 的下标位置
    """
    def largestRectangleArea_v3(self, heights: List[int]) -> int:
        # jy: 栈中维护 heights 中单调递增的高度的下标位置
        stack = []
        # jy: 以 heights = [2, 1, 5, 6, 2] 为例进行思考
        # jy: 往 heights 的前后添加 0 并不影响原 heights 中高度之间的相对距离
        heights = [0] + heights + [0]
        # jy: 往原 heights 的前后多加 0 并不会影响后续逻辑的正确性
        #heights = [0, 0, 0] + heights + [0, 0, 0]
        res = 0
        # jy: heights = [0, 2, 1, 5, 6, 2, 0]
        for i in range(len(heights)):
            # jy: 由于栈中存储的是递增的下标位置, 因此第一个数值 0 必定一直存
            #     在于栈中, 最后一个数值 0 必定不会入栈
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                # jy: 此时的 i 即 right_i, 栈顶元素值 stack[-1] 即 left_i
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        # jy: 最终结束后栈中存放的是前后添加的 0 的下标位置
        print(stack, "--------")
        return res


    """
解法 4: 优化解法 3

不在 heights 的前面添加 0, 因为在数组前部追加元素的时间复杂度为 O(n)

而是提前在栈中加入 -1 (表示最小的 left_i 为 -1), 只用在数组的尾部添加
一个 0, 使得栈不可能为空, 且不影响原 heights 中的各高度的相对位置 (不
影响宽度的计算), 因此无需考虑栈为空的情况下进行单独处理
    """
    def largestRectangleArea_v4(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        mxarea = 0
        for i, v in enumerate(heights):
            while heights[stack[-1]] > v:
                mid = stack.pop()
                area = heights[mid] * (i - stack[-1] - 1)
                if area > mxarea:
                    mxarea = area
            stack.append(i)
        print(stack, "============")
        return mxarea


    """
解法 5: 单调递增栈 (参考解法 3)

基于单调递增栈寻找指定位置的 left_i 和 right_i
    """
    def largestRectangleArea_v5(self, heights: List[int]) -> int:
        # jy: 用于保存递增的高度的下标位置 (不要求连续) 的栈
        stack = []
        max_area = 0

        len_ = len(heights)
        i = 0

        # jy: 循环遍历至末尾下标之后的一个位置 (right_i 的最大值)
        while i <= len_:
            # jy: 如果 i 等于数组长度, 表明数组已经遍历完成, 将当前位置的高
            #     度为 0, 使得后续的 if 判断逻辑中, 不会再入栈, 而是出栈并计
            #     算以栈顶位置的高度为基准下的最大面积
            current_height = 0 if i == len_ else heights[i]

            # jy: 如果栈为空, 或当前位置的高度大于或等于栈顶对应的位置的高度,
            #     则将当前位置入栈, 并将位置进一位
            if not stack or current_height >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            # jy: 如果栈非空, 且已经遍历到最后一个 right_i, 或当前的位置高度
            #     低于栈顶对应的位置的高度, 则出栈, 计算以栈顶位置的高度为基
            #     准下的最大面积 (注意: 此时的 i 即为 right_i, 将其运用与计算
            #     宽度后继续下一轮循环)
            else:
                high = heights[stack.pop()]
                # jy: 如果出栈后栈为空, 表明 i 的值已经是 len_ (即 right_i 为
                #     len_), 则此时的 left_i 为 -1, 对应的宽度为 len_
                width = i if not stack else (i - stack[-1] - 1)
                max_area = max(max_area, high * width)

        return max_area


    """
解法 6: 解法 5 的改写 (主要修改 if ... elif 中的逻辑, else 部分的逻辑不变)
    """
    def largestRectangleArea_v6(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        len_ = len(heights)
        i = 0

        while i <= len_:
            # jy: 在下标位置 i 有效的情况下, 如果栈为空或当前下标位置的高度
            #     大于栈顶下标位置的高度, 则将当前下标位置入栈
            if i < len_ and (not stack or heights[i] >= heights[stack[-1]]):
                stack.append(i)
                i += 1
            # jy: 如果下标 i 等于 len_, 且栈为空, 则可终止循环 (如果栈不为空,
            #     则需不断出栈并基于 i 的值计算面积)
            elif i == len_ and not stack:
                break
            # jy: 如果栈非空, 且已经遍历到最后一个 right_i, 或当前的位置高度
            #     低于栈顶对应的位置的高度, 则出栈, 计算以栈顶位置的高度为基
            #     准下的最大面积
            else:
                high = heights[stack.pop()]
                width = i if not stack else (i - stack[-1] - 1)
                max_area = max(max_area, high * width)

        return max_area



heights = [2, 1, 5, 6, 2, 3]
res = Solution().largestRectangleArea_v1(heights)
# jy: 10
print(res)


heights = [2, 4]
res = Solution().largestRectangleArea_v1(heights)
# jy: 4
print(res)


heights = [2, 1, 5, 6, 2, 3]
res = Solution().largestRectangleArea_v2(heights)
# jy: 10
print(res)


heights = [2, 1, 5, 6, 2]
res = Solution().largestRectangleArea_v3(heights)
# jy: 10
print(res)


heights = [2, 4]
res = Solution().largestRectangleArea_v4(heights)
# jy: 4
print(res)


heights = [2, 1, 5, 6, 2, 3]
res = Solution().largestRectangleArea_v5(heights)
# jy: 10
print(res)


heights = [2, 1, 5, 6, 2]
res = Solution().largestRectangleArea_v6(heights)
# jy: 10
print(res)


