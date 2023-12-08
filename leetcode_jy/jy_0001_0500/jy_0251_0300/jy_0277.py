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
title_jy = "Find-the-Celebrity(array_dim_2)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Suppose you are at a party with n people (labeled from 0 to n-1) and among them, there
may exist one celebrity. The definition of a celebrity is that all the other n-1 people
know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only
thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get
information of whether A knows B. You need to find out the celebrity (or verify there is
not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function ``bool knows(A, B)`` which tells you whether A knows B.
Implement a function ``int findCelebrity(n)``. There will be exactly one celebrity if he/she
is in the party. Return the celebrity's label if there is a celebrity in the party. If there
is no celebrity, return -1.


Example 1:
Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows
person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the
person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:
Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]]
Output: -1
Explanation: There is no celebrity.


Note:
1) The directed graph is represented as an adjacency matrix, which is an n x n matrix where
   a[i][j] = 1 means person i knows person j while a[i][j] = 0 means the contrary.
2) Remember that you won't have direct access to the adjacency matrix.
"""




class Solution:
    """
解法1: 首先遍历所有人, 找出不认识其他人的人, 然后遍历这些人, 判断其他人是否都认识这个人, 如果
都认识则表示找到了名人;
    """

    def __init__(self, know_graph):
        self.know_graph = know_graph

    def knows(self, i, j):
        return self.know_graph[i][j] == 1

    def findCelebrity_v1(self, n: int) -> int:
        possible_celebrities = []
        # jy: 遍历所有人;
        for i in range(n):
            know_someone = False

            # jy: 判断 i 是否认识除了自己以为的其他人;
            for j in range(n):
                if i == j:
                    continue
                # jy: 判断 i 是否认识 j, 即传入;
                if self.knows(i, j):
                    know_someone = True
                    break
            # jy: 如果 i 除了自己以外, 均不认识其他人, 则其可能是名人, 将其加入候选列表;
            if not know_someone:
                possible_celebrities.append(i)

        # jy: 遍历名人候选列表, 判断其他人是否均认识候选名人, 如果均认识, 则其为名人;
        for i in possible_celebrities:
            is_celebrity = True
            # jy: 如果其他人有不认识 i 的, 则 i 不是名人;
            for j in range(n):
                if not self.knows(j, i):
                    is_celebrity = False
                    break
            # jy: 如果 i 是名人, 则直接返回(因为只有一个名人)
            if is_celebrity:
                return i

        return -1



    """
解法2: 解法 1 可以优化为 1 个循环, 首先假设所有人都是名人, 然后遍历所有人, 如果 i 认识 j 或者 j 不认
识 i, 则 i 不可能是名人;
    """
    def findCelebrity_v2(self, n: int) -> int:
        # jy: 假设所有人都可能是名人;
        possible_celebrities = [True] * n

        # jy: 每一轮外循环, 都可以判断 i 是否是名人;
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # jy: 如果 i 认识 j 或者 j 不认识 i, 则 i 不可能是名人
                if self.knows(i, j) or not self.knows(j, i):
                    possible_celebrities[i] = False
                    break

            # jy: 经过以上, 如果 possible_celebrities[i] 仍为 True, 表明 i 是名人;
            if possible_celebrities[i]:
                return i

        return -1



    """
解法3: 首先假设第一个人是名人, 然后遍历所有人, 如果这个假定的名人认识当前的人, 则将当前
的人设置为假定的名人, 假设最后假定的名人为 k, 则 k 不认识 [k+1, n] 范围内的任何一个人,
有没有可能是 k 之后的人是名人? 不可能, 如果是 k 之后的人, 则 k 必然认识这个人, 循环时就
会跳过 k, 第一次遍历的结果也就不是 k 了; 最后再遍历一次所有人判断 k 是否是真的名人;
    """
    def findCelebrity_v3(self, n: int) -> int:
        # jy: 假设第一个人是名人, 然后遍历所有人, 如果这个假定的名人认识当前的人, 则将
        #    当前的人设置为假定的名人;
        possible_celebrity = 0
        for i in range(1, n):
            # jy: 如果 possible_celebrity 认识 i, 则 i 可能是名人; 否则 i 不可能是名人;
            if self.knows(possible_celebrity, i):
                possible_celebrity = i

        # jy: 最后再遍历一次所有人, 判断 possible_celebrity 是否是真正的名人;
        for i in range(n):
            if possible_celebrity == i:
                continue
            # jy: 如果 possible_celebrity 认识 i 或者 i 不认识 possible_celebrity, 表明 possible_celebrity
            #    不是名人;
            if self.knows(possible_celebrity, i) or not self.knows(i, possible_celebrity):
                return -1

        return possible_celebrity


graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]]
# Output: 1
res = Solution(know_graph=graph).findCelebrity_v1(n=3)
print(res)


graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]]
# Output: -1
res = Solution(know_graph=graph).findCelebrity_v2(n=3)
print(res)

res = Solution(know_graph=graph).findCelebrity_v3(n=3)
print(res)


