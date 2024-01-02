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
title_jy = "Word-Search(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归"


"""
Given an m x n grid of characters `board` and a string `word`, return true if
word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.
 

Example 1:
Input: board = [
 ["A", "B", "C", "E"],
 ["S", "F", "C", "S"],
 ["A", "D", "E", "E"]]
word = "ABCCED"
Output: true

Example 2:
Input: board = [
 ["A", "B", "C", "E"],
 ["S", "F", "C", "S"],
 ["A", "D", "E", "E"]]
word = "SEE"
Output: true

Example 3:
Input: board = [
 ["A", "B", "C", "E"],
 ["S", "F", "C", "S"],
 ["A", "D", "E", "E"]]
word = "ABCB"
Output: false
 

Constraints:
1) m == board.length
2) n = board[i].length
3) 1 <= m, n <= 6
4) 1 <= word.length <= 15
5) `board` and `word` consists of only lowercase and uppercase English letters.
 

Follow up: 
Could you use search pruning to make your solution faster with a larger `board`?
"""


class Solution:
    """
解法 1: 暴力求解, 时间复杂度 O(3^k * m * n), 空间复杂度 O(k)

m 和 n 分别为矩阵行列大小, k 为字符串 word 长度; 从矩阵中遍历长度为 k 的字符
串时, 每个字符有上、下、左、右四个方向可以选择, 舍弃回头 (上一个字符) 的方向
后, 剩余 3 种选择, 因此方案的时间复杂度为 O(3^k); 矩阵中共有 m * n 个起点, 
因此总的时间复杂度为 O(3^k * m * n); 搜索过程中的递归深度不超过 k, 因此系统
因函数调用累计使用的栈空间占用 O(k) (函数返回后, 系统调用的栈空间会释放)


通过递归, 先朝一个方向搜到底, 再回溯至上个节点, 沿另一个方向搜索, 以此类推
在搜索中如果遇到 "这条路不可能和目标字符串匹配成功" 的情况 (例如当前矩阵元
素和目标字符不匹配或该元素已被访问) 则立即返回终止该路径的继续查找
    """
    def exist_v1(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False

            # jy: 如果 k 已经遍历到 word 的最后一个字符, 且 board[i][j] 与
            #     word[k] 相等, 则表明存在符合条件的结果, 返回 True
            if k == len(word) - 1:
                return True

            # jy: 递归前先将当前已知的 board[i][j] == word[k] 修改为不等的结
            #     果 (代表此元素已访问过), 防止后续的递归过程中发现相等而导致
            #     的重复使用当前位置
            board[i][j] = ""
            # jy: 朝当前元素的上、下、左、右四个方向开启下层递归, 只需递归找
            #     到一条可行路径即可, 将结果用 res 记录 (不能直接返回, 因为还
            #     对原先的 board[i][j] 修改进行恢复后才能返回)
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            # jy: 将递归前的修改进行恢复 (回溯处理), 避免修改对后续的过程产
            #     生影响
            board[i][j] = word[k]
            return res

        # jy: 尝试逐个位置进行递归, 如果能递归找到符合要求的结果, 则返回 True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): 
                   return True
        return False


board = [
 ["A", "B", "C", "E"],
 ["S", "F", "C", "S"],
 ["A", "D", "E", "E"]]
word = "ABCCED"
res = Solution().exist_v1(board, word)
# jy: true
print(res)


board = [
 ["A", "B", "C", "E"],
 ["S", "F", "C", "S"],
 ["A", "D", "E", "E"]]
word = "SEE"
res = Solution().exist_v1(board, word)
# jy: true
print(res)


board = [
 ["A", "B", "C", "E"],
 ["S", "F", "C", "S"],
 ["A", "D", "E", "E"]]
word = "ABCB"
res = Solution().exist_v1(board, word)
# jy: false
print(res)


