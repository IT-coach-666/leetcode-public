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
title_jy = "Triangle(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a triangle array, return the minimum path sum from top to bottom. For
each step, you may move to an adjacent number of the row below. More formally,
if you are on index `i` on the current row, you may move to either index `i`
or index i + 1 on the next row.

 
Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11

Example 2:
Input: triangle = [[-10]]
Output: -10
 

Constraints:
1) 1 <= triangle.length <= 200
2) triangle[0].length == 1
3) triangle[i].length == triangle[i - 1].length + 1
4) -10^4 <= triangle[i][j] <= 10^4


Follow up: Could you do this using only O(n) extra space, where `n` is the
           total number of rows in the triangle?
"""


class Solution:
    """
动态规划算法;
解法1: 三角形中到每一个数字的路径和取决于这个数字的上方有几个数字, 如果只有一个数字, 则当前
数字的路径和为加上它上方的数字, 如果上方数字有两个, 则当前数字的路径和为加上它上方数字的较小值;

所以首先建立一个数组, 数组的长度为三角形中数字的个数, 数组中的值表示: 从三角形顶端到任一三角形
中的数字的路径和的最小值, 第一个元素的值为三角形顶端的数字; 从三角形的第二层开始遍历, 依次设
置到指定的数字的最小路径和, 同时注意边界的判断; 最后返回三角形最后一层中路径和的最小值即可;
    """
    def minimumTotal_v1(self, triangle: List[List[int]]) -> int:
        # jy: 获取三角形(二维数组)中的元素个数;
        count = sum(len(x) for x in triangle)
        # jy: 初始化一个一维数组 sums, 长度为三角形中元素个数, 初始值均为 0;
        sums = [0] * count
        # jy: sums 的第一个元素为三角形的顶点元素值;
        sums[0] = triangle[0][0]
        # jy: 从三角形的第二层(下标为 1)开始遍历;
        for i in range(1, len(triangle)):
            # jy: 下标为 i 的层为第 i+1 层, 有 i+1 个元素(三角形第 n 层有 n 个元素);
            #    此处即遍历每一层的元素;
            for j in range(i+1):
                # jy: 计算下标为 i 的层的第 j 个元素的对应在 sums 中的下标(即下标为 i 的层的前面所有
                #    层的元素个数 + j); 由于 i 从 1 开始(从第二层开始遍历), 故 index 最小值为 1;
                index = i * (i+1) // 2 + j
                # jy: 初始化 sums 中的该值为原值;
                sums[index] = triangle[i][j]
                # jy: 如果是当前层的第 1 个元素(下标为 0), 则顶点到该位置的路径和最小值等于顶点到该位置的
                #    上一层的第一个节点的路径和最小值(即 sums[index-i])加上该位置的原有值;
                if j == 0:
                    sums[index] += sums[index - i]
                # jy: 如果不是当前层的第一个元素, 且不是最后一个元素(最后一个元素的下标为 len(triangle[i-1]),
                #    其实也等于 i), 则当前数字的路径和为加上它上方数字的较小值;
                elif j-1 >= 0 and j <= len(triangle[i-1]) - 1:
                    sums[index] += min(sums[index - i-1], sums[index - i])
                # jy: 此处逻辑即对应该行中的最后一个元素(sums[index - i-1]);
                else:
                    sums[index] += sums[index - i-1]
        # jy: 返回最后一层中路径和最小的值(最后一层的起始元素下标即: 总元素个数-最后一层元素个数);
        return min(sums[count - len(triangle[-1]):])



    """
解法2: 解法 1 用了一维数组来保存路径和, 过于复杂, 使用和三角形一样的二维数组即可;
    """
    def minimumTotal_v2(self, triangle: List[List[int]]) -> int:
    # jy: 构建与三角形一致的二维数组, 初始化数值为 0;
        sums = [[0] * len(t) for t in triangle]
        # jy: 第一个数值设置为三角形的第一个相同;
        sums[0][0] = triangle[0][0]
        # jy: 从三角形的第 2 层开始遍历;
        for i in range(1, len(triangle)):
            # jy: 第 n 层有 n 个元素, 下标为 i 的层为第 i+1 层, 共有 i+1 个元素;
            #    此处即遍历该层的所有元素;
            for j in range(i+1):
                # jy: 先初始化 sums 中具体值为原先三角形中的值;
                sums[i][j] = triangle[i][j]
                # jy: 如果是该层的第 1 个元素, 则加上 sums 的上一层的第一个元素的值即可;
                if j == 0:
                    sums[i][j] += sums[i-1][0]
                # jy: 如果是该层的中间部分元素(非首尾元素), 则加上 sums 的上一层的同等位置元素和其
                #    前一个元素中的较小值;
                elif j-1 >= 0 and j <= len(triangle[i-1]) - 1:
                    sums[i][j] += min(sums[i-1][j-1], sums[i-1][j])
                # jy: 如果是该层的最后一个元素, 则加上 sums 的上一层的最后一个元素;
                else:
                    sums[i][j] += sums[i-1][j-1]
        # jy: 返回 sums 的最后一层元素的最小值;
        return min(sums[-1])



    """
解法3: 以上解法是从上往下推导, 此处则是从下往上推导; 相比于前两种解法, 这种
方法不用考虑边界, 最后第一个数组的第一个元素就是路径最小的和;
    """
    def minimumTotal_v3(self, triangle: List[List[int]]) -> int:
        # jy: 初始化 sums 维度同三角形, 初始数值均为 0;
        sums = [[0] * len(t) for t in triangle]
        # jy: 遍历三角形的最后一层, 并将 sums 的最后一层的值初始化同三角形最后一层;
        for i, value in enumerate(triangle[-1]):
            sums[len(triangle)-1][i] = value
        # jy: 从三角形的倒数第二层开始层层往上遍历;
        for i in range(len(triangle)-2, -1, -1):
            # jy: 下标为 i 的为第 i+1 层, 共有 i+1 个值, 此处遍历该层的所有值;
            #    将该层的当前位置节点加上下一层的同位置和下一个位置的较小值;
            for j in range(i+1):
                sums[i][j] = triangle[i][j] + min(sums[i+1][j], sums[i+1][j+1])
        # jy: 返回 sums 的顶点值即为最终结果;
        return sums[0][0]


triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]]
res = Solution().minimumTotal_v1(triangle)
print(res)


res = Solution().minimumTotal_v2(triangle)
print(res)


res = Solution().minimumTotal_v3(triangle)
print(res)


