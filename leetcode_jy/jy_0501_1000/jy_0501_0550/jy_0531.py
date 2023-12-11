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
title_jy = "Lonely-Pixel-I(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an m * n ``picture`` consisting of black 'B' and white 'W' pixels, return the
number of black lonely pixels. A black lonely pixel is a character 'B' that located
at a specific position where the same row and same column don't have any other black
pixels.


Example 1:    https://www.yuque.com/frederick/dtwi9g/nhgg1x
Input: picture = [
["W","W","B"],
["W","B","W"],
["B","W","W"]]
Output: 3
Explanation: All the three 'B's are black lonely pixels.

Example 2:
Input: picture = [
["B","B","B"],
["B","B","W"],
["B","B","B"]]
Output: 0


Constraints:
m == picture.length
n == picture[i].length
1 <= m, n <= 500
picture[i][j] is 'W' or 'B'.
"""


from typing import List


class Solution:
    """
先统计每行每列 B 的个数再判断
    """
    def findLonelyPixel_v1(self, picture: List[List[str]]) -> int:
        # jy: m 行 n 列;
        m, n = len(picture), len(picture[0])
        rows = [0] * m
        columns = [0] * n
        count = 0
        # jy-version-1-Begin ----------------------------------------------
        '''
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    columns[j] += 1
        '''
        # jy-version-1-End ------------------------------------------------
        # jy-version-2-Begin ----------------------------------------------
        for i in range(m):
            rows[i] = picture[i].count("B")
        for j in range(n):
            columns[j] = [picture[row][j] for row in range(m)].count("B")
        # jy-version-2-End ------------------------------------------------

        # jy: 遍历所有行, 如果当前行的 "B" 的个数不为 1, 则跳过当前行; 如果当前
        #     行中的 "B" 的个数为 1, 则遍历遍历当前行的所有元素, 如果该行
        for i in range(m):
            if rows[i] != 1:
                continue
            # jy: 如果当前行中只有一个 "B", 则判断当前行的 "B" 所在的列是否也只有 1 个 "B",
            #     如果是, 则目标结果加 1;
            for j in range(n):
                if picture[i][j] == 'B' and columns[j] == 1:
                    count += 1
                    # jy: 加上 break 语句进行优化, 如果代码执行到当前 for 循环, 则
                    #     表明当前行只有一个 "B", 此时如果遍历到了, 后续则不再会有;
                    break

        return count


picture = [
["W","W","B"],
["W","B","W"],
["B","W","W"]]
# Output: 3
res = Solution().findLonelyPixel_v1(picture)
print(res)


picture = [
["B","B","B"],
["B","B","W"],
["B","B","B"]]
# Output: 0
res = Solution().findLonelyPixel_v1(picture)
print(res)


picture = [
["W","B","B","W"],
["W","B","W","W"],
["B","W","W","W"],
["B","W","W","W"]]
# Output: 0
res = Solution().findLonelyPixel_v1(picture)
print(res)


