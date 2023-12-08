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
title_jy = "Candy-Crush(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
This question is about implementing a basic elimination algorithm for Candy Crush.
Given an ``m x n`` integer array ``board`` representing the grid of candy where
``board[i][j]`` represents the type of candy. A value of ``board[i][j]`` == 0
represents that the cell is empty.

The given ``board`` represents the state of the game following the player's move.
Now, you need to restore the board to a stable state by crushing candies according
to the following rules:
1) If three or more candies of the same type are adjacent vertically or horizontally,
   crush them all at the same time - these positions become empty.
2) After crushing all candies simultaneously, if an empty space on the board has
   candies on top of itself, then these candies will drop until they hit a candy
   or bottom at the same time. No new candies will drop outside the top boundary.
3) After the above steps, there may exist more candies that can be crushed. If so,
   you need to repeat the above steps.
4) If there does not exist more candies that can be crushed (i.e., the board is
   stable), then return the current board.

You need to perform the above rules until the board becomes stable, then return the
stable board.


Example 1:    https://www.yuque.com/frederick/dtwi9g/kmxu6f
board = [
 [110,   5, 112, 113,  114],
 [210, 211,   5, 213,  214],
 [310, 311,   3, 313,  314],
 [410, 411, 412,   5,  414],
 [5,     1, 512,   3,    3],
 [610,   4,   1, 613,  614],
 [710,   1,   2, 713,  714],
 [810,   1,   2,   1,    1],
 [1,     1,   2,   2,    2],
 [4,     1,   4,   4, 1014]]
Output:
[[   0    0    0    0    0]
 [   0    0    0    0    0]
 [   0    0    0    0    0]
 [ 110    0    0    0  114]
 [ 210    0    0    0  214]
 [ 310    0    0  113  314]
 [ 410    0    0  213  414]
 [ 610  211  112  313  614]
 [ 710  311  412  613  714]
 [ 810  411  512  713 1014]]

Example 2:
board = [
[1, 3, 5, 5, 2],
[3, 4, 3, 3, 1],
[3, 2, 4, 5, 2],
[2, 4, 4, 5, 5],
[1, 4, 4, 1, 1]]
Output:
[[1, 3, 0, 0, 0],
 [3, 4, 0, 5, 2],
 [3, 2, 0, 3, 1],
 [2, 4, 0, 5, 2],
 [1, 4, 3, 1, 1]]


Constraints:
m == board.length
n == board[i].length
3 <= m, n <= 50
1 <= board[i][j] <= 2000
"""


from typing import List
import numpy


class Solution:
    """
解法1: 遍历矩阵, 如果当前坐标向左两格和向上两格和当前坐标相同, 则表示这些坐标需要消除;
消除后需要将其他坐标下沉, 下沉时从下往上逐列逐行遍历
    """
    def candyCrush_v1(self, board: List[List[int]]) -> List[List[int]]:
        # jy: m 行 n 列;
        m, n = len(board), len(board[0])

        while True:
            # jy: crush 用于记录要被消除(即置为 0)的坐标位置;
            crush = set()

            # jy: 遍历二维矩阵, 获取需要被消除的位置下标;
            for i in range(m):
                for j in range(n):
                    # jy: 判断当前位置 (i, j) 的右方 3 个元素是否均相同, 如果是则将 3 个位置坐标加入
                    #     到 crush 集合中;
                    if j > 1 and board[i][j] != 0 and board[i][j] == board[i][j-1] == board[i][j-2]:
                        crush.add((i, j))
                        crush.add((i, j-1))
                        crush.add((i, j-2))
                    # jy: 判断当前位置 (i, j) 的上方 3 个元素是否均相同, 如果是则将 3 个位置坐标加入
                    #     到 crush 集合中;
                    if i > 1 and board[i][j] != 0 and board[i][j] == board[i-1][j] == board[i-2][j]:
                        crush.add((i, j))
                        crush.add((i-1, j))
                        crush.add((i-2, j))

            # jy: 如果经过一轮循环遍历没有再次找到需要被消除的位置下标, 则退出循环, 表明已消除所有可
            #     消除的位置;
            if not crush:
                break

            # jy: 如果 crush 中有指定位置待消除, 则将其消除(在 board 中的该位置置为 0);
            for i, j in crush:
                board[i][j] = 0

            # jy: 消除后需要将其他坐标下沉, 下沉时以列为单位(从第一列开始遍历, 遍历所有
            #     board 中的列), 从下往上逐行遍历;
            for j in range(n):
                # jy: 从下往上逐行遍历, 如果一直没有碰到相应行对应的位置为 0, 则 k 与 i 的
                #     值总是保持同步相等的, 直到碰到某位置为 0, 则 k 的值将比 i 的大, 随后
                #     会将 (i, j) 更新到 (k, j) 中, 不断重复使得为 0 的位置的上方的值不断下
                #     移, 即原本位置为 0 的会被消除掉;
                k = m-1
                for i in range(m-1, -1, -1):
                    if board[i][j] != 0:
                        board[k][j] = board[i][j]
                        k -= 1
                # jy: 当非 0 的位置下移后, 最上方要用 0 填充;
                for i in range(k+1):
                    board[i][j] = 0

        return board


board = [
 [110,   5, 112, 113,  114],
 [210, 211,   5, 213,  214],
 [310, 311,   3, 313,  314],
 [410, 411, 412,   5,  414],
 [5,     1, 512,   3,    3],
 [610,   4,   1, 613,  614],
 [710,   1,   2, 713,  714],
 [810,   1,   2,   1,    1],
 [1,     1,   2,   2,    2],
 [4,     1,   4,   4, 1014]]

'''
Output:
[[   0    0    0    0    0]
 [   0    0    0    0    0]
 [   0    0    0    0    0]
 [ 110    0    0    0  114]
 [ 210    0    0    0  214]
 [ 310    0    0  113  314]
 [ 410    0    0  213  414]
 [ 610  211  112  313  614]
 [ 710  311  412  613  714]
 [ 810  411  512  713 1014]]
'''
res = Solution().candyCrush_v1(board)
print(numpy.array(res))


board = [
[1, 3, 5, 5, 2],
[3, 4, 3, 3, 1],
[3, 2, 4, 5, 2],
[2, 4, 4, 5, 5],
[1, 4, 4, 1, 1]]

'''
Output:
[[1, 3, 0, 0, 0],
 [3, 4, 0, 5, 2],
 [3, 2, 0, 3, 1],
 [2, 4, 0, 5, 2],
 [1, 4, 3, 1, 1]]
'''
res = Solution().candyCrush_v1(board)
print(numpy.array(res))


