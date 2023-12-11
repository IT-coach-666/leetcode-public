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
title_jy = "Design-Tic-Tac-Toe(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:
1) A move is guaranteed to be valid and is placed on an empty block.
2) Once a winning condition is reached, no more moves is allowed.
3) A player who succeeds in placing n of their marks in a horizontal, vertical,
   or diagonal row wins the game.


Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |      # Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |      # Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |      # Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |      # Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |      # Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |      # Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |      # Player 1 makes a move at (2, 1).
|X|X|X|


Follow up: Could you do better than O(n^2) per move() operation?
"""



"""
解法1: 每次下完一步判断当前棋子所在的行, 列, 对角线是否都是同一棋子即可;
"""
class TicTacToe_v1:
    def __init__(self, n: int):
        # jy: 初始化棋盘为 n 方阵;
        self.board = [['' for _ in range(n)] for _ in range(n)]


    def move(self, row: int, col: int, player: int) -> int:
        # jy: 如果是 player 1 下棋, 填 'X', 否则 player 2 下棋为 'O'
        self.board[row][col] = 'X' if player == 1 else 'O'

        result = 0
        # jy: 如果是 player 1, 则判断其下棋后是否能赢, result 为 1 表示 player 1 赢;
        if player == 1:
            result = 1 if self._is_player_win(1, row, col) else 0
        # jy: 如果是 player 2, 则判断其下棋后是否能赢, result 为 2 表示 player 2 赢;
        elif player == 2:
            result = 2 if self._is_player_win(2, row, col) else 0

        return result


    def _is_player_win(self, player: int, row: int, column: int) -> bool:
        # jy: 获取当前对应的 player 的所下棋类型;
        mark = 'X' if player == 1 else 'O'
        # jy: 获取方阵维度;
        n = len(self.board)
        # jy: 判断当前行是否均为 mark 标志旗号, 如果是则直接返回 True;
        if all(x == mark for x in [self.board[row][i] for i in range(n)]):
            return True
        # jy: 判断当前列是否均为 mark 标志旗号, 如果是则直接返回 True;
        if all(x == mark for x in [self.board[i][column] for i in range(n)]):
            return True
        # jy: 如果行号与列号相等(主对角线特点), 则判断所在的对角线(左上至右下)是否均
        #    为 mark 标志, 如果是则返回 True;
        if row == column and all(x == mark for x in [self.board[i][i] for i in range(n)]):
            return True
        # jy: 如果行号和列号下标和为 n-1 (右上至左下对角线特点), 则判断所在对角线是否均为
        #    mark 标志, 如果是则返回 True;
        if row + column == n-1 and all(x == mark for x in [self.board[i][n-1-i] for i in range(n)]):
            return True

        return False

"""
解法2: 创建一个行和列对应的数组, 长度均为 n, 分别用来记录每一行和每一列玩家 1 和玩家 2 各
有多少棋子; 当玩家 1 在某格放置棋子时, 对应行, 列加 1, 反之玩家 2 则减 1; 同样的, 创建两个
变量来表示两条对角线的棋子数; 当放置完棋子后, 判断对应行, 列, 对角线的值是否是 n 或 -n, 如
果是则表示当前玩家获胜;
"""
class TicTacToe_v2:
    def __init__(self, n: int):
        self.board = [['' for _ in range(n)] for _ in range(n)]
        # jy: 创建行和列对应数组, 记录该行玩家 1 和玩家 2 各有多少棋子(当玩家 1 在某格放置棋
        #    子时, 对应行, 列加 1, 反之玩家 2 则减 1)
        self.rows = [0] * n
        self.columns = [0] * n
        # jy: 同样的, 创建两个变量来表示两条对角线的棋子数;
        self.diagonals1 = 0
        self.diagonals2 = 0


    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = 'X' if player == 1 else 'O'
        self.rows[row] += 1 if player == 1 else -1
        self.columns[col] += 1 if player == 1 else -1

        if row == col:
            self.diagonals1 += 1 if player == 1 else -1

        if row + col == len(self.board) - 1:
            self.diagonals2 += 1 if player == 1 else -1

        target = len(self.board) if player == 1 else - len(self.board)

        if self.rows[row] == target or self.columns[col] == target or self.diagonals1 == target or self.diagonals2 == target:
            return player
        else:
            return 0

toe = TicTacToe_v1(3)
print(toe.move(0, 0, 1))    # Returns 0 (no one wins)
print(toe.move(0, 2, 2))    # Returns 0 (no one wins)
print(toe.move(2, 2, 1))    # Returns 0 (no one wins)
print(toe.move(1, 1, 2))    # Returns 0 (no one wins)
print(toe.move(2, 0, 1))    # Returns 0 (no one wins)
print(toe.move(1, 0, 2))    # Returns 0 (no one wins)
print(toe.move(2, 1, 1))    # Returns 1 (player 1 wins)

toe = TicTacToe_v2(3)
print(toe.move(0, 0, 1))    # Returns 0 (no one wins)
print(toe.move(0, 2, 2))    # Returns 0 (no one wins)
print(toe.move(2, 2, 1))    # Returns 0 (no one wins)
print(toe.move(1, 1, 2))    # Returns 0 (no one wins)
print(toe.move(2, 0, 1))    # Returns 0 (no one wins)
print(toe.move(1, 0, 2))    # Returns 0 (no one wins)
print(toe.move(2, 1, 1))    # Returns 1 (player 1 wins)


