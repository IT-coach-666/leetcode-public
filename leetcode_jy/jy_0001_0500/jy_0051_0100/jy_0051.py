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
from typing import List, Dict, Set
# jy: 记录该题的难度系数
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "N-Queens(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | 相似题: 0052 | IMP"


"""
The n-queens puzzle is the problem of placing `n` queens on an n×n chessboard
such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.


Example 1: 图示: https://www.yuque.com/it-coach/leetcode/ge8qgf
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],
 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

Example 2:
Input: n = 1
Output: [["Q"]]


Constraints:
1 <= n <= 9
"""


class Solution:
    """
解法 1: 暴力解法

尝试的过程中可以过滤掉一些无需考虑的组合; 首先从第一行开始, 对于第一行的每
一列, 假设该列放了棋子, 则采用深度优先搜索递归判断后续行的棋子应该放在哪里

如果位置 (row, column) 放了棋子, 则同一行、同一列、左斜对角线、右斜对角线就
不能再放置棋子:
1) 同一行不用判断, 因为每次深度优先搜索都是往下一层
2) 同一列很好判断, 只要看 column 是否相等即可
3) 同对角线的判断利用了一个隐藏的性质: 对于 (a, b) 和 (c, d) 两个点来说
   a) 如果是左下至右上的斜对角线, 则有 a + b = c + d
   b) 如果是左上至右下的斜对角线, 则有 a - b = c - d

因此可以使用 Set 来保存分别不能放置的行和对角线; 当递归的深度达到了 n, 就说
明找到了一组解
    """
    def solveNQueens_v1(self, n: int) -> List[List[str]]:
        result = []
        self._dfs(0, n, set(), set(), set(), [], result)
        #print(result)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in solution]
                for solution in result]

    def _dfs(self, row: int, n, columns: Set[int], 
             left_diagonals: Set[int],
             right_diagonals: Set[int], 
             solution: List[int],
             result: List[List[int]]) -> None:
        """
        row: 当前递归过程中尝试在下标为 row 的行的每一列放置 "Q"
        n: 矩阵维度, 递归过程中该值不变
        columns: 记录递归过程中不能再放置 "Q" 的列
        left_diagonals: 记录递归过程中不能再放置 "Q" 的左下至右上的斜对角线
        right_diagonals: 记录递归过程中不能再放置 "Q" 的左上至右下的斜对角线
        solution: 记录可能的方案, 如果是一个正确的方案, 则是一个长度为 n 的列
                  表; solution[i] 表示 n × n 的矩阵 arr 中 arr[i, solution[i]]
                  应放置 "Q", 而第 i 行的其余位置为 "."
        result: 存放所有的 solution 结果
        """
        # jy: 如果递归过程中递归到的 row 值为 n, 表明找到了一组可行解, 将其加
        #     入 result 列表, 并返回, 终止递归
        if row == n:
            result.append(solution)
            return

        # jy: 在当前 row 行的 column 列逐个尝试放入 "Q", 并深度遍历下一行的每
        #     一列, 尝试放入 "Q", 如果可以放置, 则不断深度遍历, 如果最终能放
        #     满, 则将该种解决方案加入到结果列表
        for column in range(n):
            # jy: 如果当前列在不能放置 "Q" 的列或当前坐标位置在不能放置 "Q" 的
            #     对角线上, 则跳过, 继续尝试在其它列中放置 "Q"
            if column in columns or row + column in left_diagonals \
                    or row - column in right_diagonals:
                continue

            # jy: 在 column 列放置 "Q" 后, 后续就不能在该列再放置了
            columns.add(column)
            # jy: 在当前坐标位置放置 "Q" 后, 后续与该位置属于同一对角线上的位
            #     置就都不能再放置 "Q", 而与当前坐标位置属于同一对角线的位置的
            #     的坐标的特点是: row + column 或 row - column 的值与当前坐标
            #     位置相同 
            left_diagonals.add(row + column)
            right_diagonals.add(row - column)
            # jy: 递归 (深度优先遍历), 尝试在下一行的每一列中放置 "Q"
            self._dfs(row + 1, n, columns, left_diagonals,
                      right_diagonals, solution + [column], result)
            # jy: 回溯, 使得当前列尝试放置后又将其恢复为原样, 不影响尝试后续其
            #     它列中尝试放置的结果
            columns.remove(column)
            left_diagonals.remove(row + column)
            right_diagonals.remove(row - column)


n = 4
res = Solution().solveNQueens_v1(n)
print(res)



n = 6
res = Solution().solveNQueens_v1(n)
print(res)



n = 9
res = Solution().solveNQueens_v1(n)
print(res)
