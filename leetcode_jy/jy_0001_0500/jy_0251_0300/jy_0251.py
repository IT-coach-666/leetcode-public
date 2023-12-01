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
title_jy = "Flatten-2D-Vector(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.

Implement the Vector2D class:
Vector2D(int[][] vec): initializes the object with the 2D vector vec.
next():   returns the next element from the 2D vector and moves the pointer one step forward.
          You may assume that all the calls to next are valid.
hasNext(): returns true if there are still some elements in the vector, and false otherwise.


Example 1:
Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
vector2D.next();      # return 1
vector2D.next();      # return 2
vector2D.next();      # return 3
vector2D.hasNext();   # return True
vector2D.hasNext();   # return True
vector2D.next();      # return 4
vector2D.hasNext();   # return False


Constraints:
0 <= vec.length <= 200
0 <= vec[i].length <= 500
-500 <= vec[i][j] <= 500
At most 10^5 calls will be made to next and hasNext.


Follow up: As an added challenge, try to code it using only iterators in C++ or iterators in Java.
"""




from typing import List

"""
解法1: 使用 row 和 column 标记当前矩阵中有效数字的位置, 注意空列表的存在;
"""
class Vector2D_v1:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        # jy: 用 row 标记当前矩阵中有效数字的所在行; 初始化时, 从 vec 的下标为 0 的
        #    行开始找, 找到一个有效的行(如果下标为 0 的行是空行, 则会进一步找下标
        #    为 1 的行, 如果已经都是空行, 则会返回 -1);
        self.row = self._get_next_row(vec, 0)
        # jy: 用 column 标记当前矩阵中有效数字的所在列; 如果有效数字的行不为 -1, 表
        #    明存在有效数值, 列则初始化为该行的首列(即下标为 0 的列);
        self.column = 0 if self.row != -1 else -1
        self.total_row = len(vec)



    def next(self) -> int:
        # jy: 下一个数值即当前 row 和 column 对应的值, 该值获取之后, 会将 row 和 column 更
        #    新为下一个值, 等待被获取;
        value = self.vec[self.row][self.column]
        # jy: 更新下一个值的 row 和 column; 如果当前列已经是该行的最后一列了, 则下一个值在
        #    新行中的, 需要同时更新 row 和 column 的值;
        if self.column == len(self.vec[self.row]) - 1:
            # jy: 如果 row 已经是最后一行, 则更新 row 和 column 为 -1;
            if self.row == self.total_row - 1:
                self.row = -1
                self.column = -1
            # jy: 如果 row 非最后一行, 则先判断后续的行中是否存在有效行, 如果存在, 则将行更
            #    新为有效行对应的下标, 并将列更新为 0; 如果不存在, 则均更新为 -1;
            else:
                self.row = self._get_next_row(self.vec, self.row + 1)
                self.column = 0 if self.row > -1 else -1
        # jy: 如果当前列并非该行的最后一列, 则下一个值依然在该行中, 只要更新列的值即可;
        else:
            self.column += 1

        return value



    def hasNext(self) -> bool:
        # jy: 如果行和列的下标均有效, 表明存在有效数值;
        return self.row != -1 and self.column != -1


    def _get_next_row(self, vec, row):
        # jy: 从下标为 row 的行开始, 找到存在有效数值的行;
        for i in range(row, len(vec)):
            if vec[i]:
                return i
        return -1


"""
解法2: 精简代码;
"""
class Vector2D_v2:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.row = 0
        self.column = 0

    def next(self) -> int:
        # jy: 如果存在下一个数值(在此判断中, 如果确认存在, 会将下一个值的 row 和 column 设
        #    置下一个有效值对应的 row 和 column), 则直接获取下一个数值; 获取后 colume 直
        #    接加 1 (更新为下一个数值的对应列, 该列值是否有效会再获取下一个数值时进行判
        #    断, 如果判断无效会进行相应修改使其有效化);
        if self.hasNext():
            value = self.vec[self.row][self.column]
            self.column += 1

            return value


    def hasNext(self) -> bool:
        # jy: 在判断有下一个数值时, 判断当前列是否超出了当前行的最后一列的范围(下标是否为最
        #    后一列的下标加 1), 如果是, 则行加 1, 列为第一列; 更新后继续判断当前对应的 row
        #    和 column 是否指向有效的下一个值, 如果无效, 则更新至有效为止;
        while self.row < len(self.vec) and self.column == len(self.vec[self.row]):
            self.row += 1
            self.column = 0
        # jy: 判断是否有下一个值, 则看更新后的行是否有效即可;
        return self.row < len(self.vec)


vector2D = Vector2D_v1([[1, 2], [3], [4]]);
print(vector2D.next())      # return 1
print(vector2D.next())      # return 2
print(vector2D.next())      # return 3
print(vector2D.hasNext())   # return True
print(vector2D.hasNext())   # return True
print(vector2D.next())      # return 4
print(vector2D.hasNext())   # return False


vector2D = Vector2D_v2([[1, 2], [3], [4]]);
print(vector2D.next())      # return 1
print(vector2D.next())      # return 2
print(vector2D.next())      # return 3
print(vector2D.hasNext())   # return True
print(vector2D.hasNext())   # return True
print(vector2D.next())      # return 4
print(vector2D.hasNext())   # return False


