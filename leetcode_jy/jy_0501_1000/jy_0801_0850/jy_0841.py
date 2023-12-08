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
title_jy = "Keys-and-Rooms(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
There are N rooms and you start in room 0. Each room has a distinct number in
0, 1, 2, ..., N-1, and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is
an integer in [0, 1, ..., N-1] where N = rooms.length. A key rooms[i][j] = v
opens the room with number v.

Initially, all the rooms start locked (except for room 0).
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.



Example 1:
Input: [[1],[2],[3],[]]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.

Example 2:
Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.


Note:
1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
"""


from collections import deque
from typing import List


class Solution:
    """
解法1: 从第一个房间开始搜索, 使用 visited 标记访问过的房间, 最后判断 visited 的
长度是否等于 rooms 即可;
    """
    def canVisitAllRooms_v1(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True
        # jy: 使用 visited 集合保存被访问的房间序号
        visited = set()
        self._dfs(0, rooms, visited)

        return len(visited) == len(rooms)


    def _dfs(self, i, rooms, visited):
        # jy: 如果房间 i 已经被访问过, 直接返回(终止递归)
        if i in visited:
            return
        # jy: 将当前未访问过的房间的标号加入集合中, 表示已访问, 并获取该房间中的
        #    其它房间的钥匙, 不断遍历访问;
        visited.add(i)
        for key in rooms[i]:
            self._dfs(key, rooms, visited)


    """
解法2: 广度优先搜索版本;
    """
    def canVisitAllRooms_v2(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True

        visited = set()
        # jy: 将有钥匙的房间号加入队列中;
        queue = deque([0])
        # jy: 如果队列不为空, 则出队(左或右侧出队均可)
        while queue:
            # jy: 出队后, 将出队的房间设置为已访问, 并将该房间中的所有其它房间的钥匙
            #    入队(如果其它房间还没被访问的话);
            room = queue.popleft()
            visited.add(room)
            for key in rooms[room]:
                if key in visited:
                    continue
                queue.append(key)
        # jy: 最终返回能访问的房间数是否等于总房间数即可;
        return len(visited) == len(rooms)



rooms = [[1],[2],[3],[]]
# Output: true
res = Solution().canVisitAllRooms_v1(rooms)
print(res)


rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
res = Solution().canVisitAllRooms_v1(rooms)
print(res)


