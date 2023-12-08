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
title_jy = "Lonely-Pixel-II(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an m x n ``picture`` consisting of black 'B' and white 'W' pixels and an integer
``target``, return the number of black lonely pixels. A black lonely pixel is a character
'B' that located at a specific position (r, c) where:
1) Row ``r`` and column ``c`` both contain exactly ``target`` black pixels.
2) For all rows that have a black pixel at column ``c``, they should be exactly the same
   as row ``r``.


Example 1:    https://www.yuque.com/frederick/dtwi9g/hndfe4
Input: picture = [
["W","B","W","B","B","W"],
["W","B","W","B","B","W"],
["W","B","W","B","B","W"],
["W","W","B","W","B","W"]],
target = 3
Output: 6
Explanation: All the green 'B' are the black pixels we need (all 'B's at column 1 and 3).
             Take 'B' at row r = 0 and column c = 1 as an example:
             Rule 1: row r = 0 and column c = 1 both have exactly target = 3 black pixels.
             Rule 2: the rows have black pixel at column c = 1 are row 0, row 1 and row 2.
                     They are exactly the same as row r = 0.

Example 2:
Input: picture = [
["W","W","B"],
["W","W","B"],
["W","W","B"]],
target = 1
Output: 0


Constraints:
m == picture.length
n == picture[i].length
1 <= m, n <= 200
picture[i][j] is 'W' or 'B'.
1 <= target <= min(m, n)
"""


import collections
from typing import List


class Solution:
    """
首先统计出 "B" 所在的行对应哪些列, 所在的列对应哪些行; 然后再次遍历矩阵. 判断当前行和
当前列的 B 的个数是否相等, 以及是否满足规则 2
    """
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        m, n = len(picture), len(picture[0])
        # jy: 存放每行中 "B" 的所在列下标;
        row_to_column = collections.defaultdict(list)
        # jy: 存放每列中 "B" 的所在行下标;
        column_to_row = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_to_column[i].append(j)
                    column_to_row[j].append(i)

        count = 0
        # jy: 遍历所有行;
        for i in range(m):
            # jy: 如果当前行 i 不在 row_to_column 中(表明当前行 i 中不含有 "B"), 或者
            #     当前行 i 中的 "B" 的个数不等于目标值 target, 则跳过当前循环;
            if i not in row_to_column or len(row_to_column[i]) != target:
                continue

            # jy: 执行到此处, 则表明当前行 i 中 "B" 的个数为 target 个; 此时逐个判断这
            #     target 个 "B" 所在的列的 "B" 的个数是否也是 target 个, 如果不是, 则跳
            #     过当前循环, 继续判断下一列;
            for j in range(len(row_to_column[i])):
                if len(column_to_row[row_to_column[i][j]]) != target:
                    continue
                is_valid = True
                # jy: 执行到此处时表明 rule-1 已经满足, 以下 for 循环即实现 rule-2 的判断;
                for k in range(1, target):
                    # jy: 获取满足 rule-1 的当前行列位置所在列对应的 "B" 的行坐标;
                    row = column_to_row[row_to_column[i][j]]

                    if picture[row[k-1]] != picture[row[k]]:
                        is_valid = False
                        break
                if is_valid:
                    count += 1

        return count


picture = [
["W","B","W","B","B","W"],
["W","B","W","B","B","W"],
["W","B","W","B","B","W"],
["W","W","B","W","B","W"]]
target = 3
# Output: 6
res = Solution().findBlackPixel(picture, target)
print(res)


picture = [
["W","B","W","B","B","W"],
["W","B","W","B","B","W"],
["W","W","W","B","B","W"],
["W","B","B","W","B","W"]]
target = 3
# Output: 0
res = Solution().findBlackPixel(picture, target)
print(res)


picture = [
["W","W","B"],
["W","W","B"],
["W","W","B"]]
target = 1
# Output: 0
res = Solution().findBlackPixel(picture, target)
print(res)


