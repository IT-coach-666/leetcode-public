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
title_jy = "Dungeon-Game(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
The demons had captured the princess and imprisoned her in the bottom-right corner of a `dungeon`. The `dungeon` consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through `dungeon` to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

 

Example 1: 图示参考: https://www.yuque.com/it-coach/leetcode/xyqvsic3aba1cbbs
Input: dungeon = [
[-2, -3,  3],
[-5, -10, 1],
[10, 30, -5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.

Example 2:
Input: dungeon = [[0]]
Output: 1
 

Constraints:
1) m == dungeon.length
2) n == dungeon[i].length
3) 1 <= m, n <= 200
4) -1000 <= dungeon[i][j] <= 1000
"""

class Solution:
    """
解法 1: https://leetcode.cn/problems/dungeon-game/solutions/173401/dong-tai-gui-hua-ji-qi-shu-xue-tui-dao-by-mzh1996/
    """
    def calculateMinimumHP_v1(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        if m == 1 and n == 1:#1x1的地牢
            return max(1,1-dungeon[0][0])
        elif m == 1 and n != 1:#1xn的地牢
            newlist = []
            for i in range(n):
                newlist.append(-1)
            newlist[-1] = max(1,1-dungeon[0][-1])
            for i in range(n-1):
                tempindex = n - i - 2
                newlist[tempindex] = max(1,newlist[tempindex+1] - dungeon[0][tempindex])
            return newlist[0]
        elif m != 1 and n == 1:#nx1的地牢
            newlist = []
            for i in range(m):
                newlist.append(-1)
            newlist[-1] = max(1,1-dungeon[-1][0])
            for i in range(m-1):
                tempindex = m - i - 2
                newlist[tempindex] = max(1,newlist[tempindex+1] - dungeon[tempindex][0])
            return newlist[0]
        #以下针对mxn的地牢，m和n都大于1
        #初始化一个m行n列的dplist
        print('地牢的size为',m,n)
        newlist = []
        for i in range(m):
            templist = []
            for j in range(n):
                templist.append(-1)            
            newlist.append(templist)
        #我们先初始化最下面一行和最右边一列
        #先初始化最右下角的
        newlist[m-1][n-1] = max(1,1 - dungeon[-1][-1])
        tempinit = newlist[-1][-1]
        #最下面一行，共n-1个待补充的数字
        for i in range(n-1):
            tempindex = n - i - 2
            newlist[-1][tempindex] = max(1,newlist[-1][tempindex+1] - dungeon[-1][tempindex])
        #最右边一列，共m-1个待补充的数字
        for j in range(m-1):
            tempindex = m - j - 2
            newlist[tempindex][-1] = max(1,newlist[tempindex+1][-1] - dungeon[tempindex][-1])
        #从[m-2][n-2]开始填充,一直到[0][0],共(m-1)x(n-1)个
        #先从倒数第二行倒数第二列开始，然后是倒数第二行倒数第三列，......
        for i in range(m-1):
            tempi = m - i - 2
            for j in range(n-1):
                tempj = n - j - 2
                newlist[tempi][tempj] = max(1,min(newlist[tempi+1][tempj],newlist[tempi][tempj+1])-dungeon[tempi][tempj])
        print(newlist)
        return newlist[0][0]

    
dungeon = [
[-2, -3,  3],
[-5, -10, 1],
[10, 30, -5]]
res = Solution().calculateMinimumHP_v1(dungeon)
# jy: 7
print(res)


dungeon = [[0]]
res = Solution().calculateMinimumHP_v1(dungeon)
# jy: 1
print(res)
    
    