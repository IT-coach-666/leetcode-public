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
title_jy = "Beautiful-Arrangement(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Suppose you have ``n`` integers labeled 1 through ``n``. A permutation of those ``n``
integers ``perm`` (1-indexed) is considered a beautiful arrangement if for every
``i`` (1 <= i <= n), either of the following is true:
1) ``perm[i]`` is divisible by ``i``.
2) ``i`` is divisible by ``perm[i]``.

Given an integer n, return the number of the beautiful arrangements that you can construct.


Example 1:
Input: n = 2
Output: 2
Explanation: The first beautiful arrangement is [1,2]:
                 - perm[1] = 1 is divisible by i = 1
                 - perm[2] = 2 is divisible by i = 2
             The second beautiful arrangement is [2,1]:
                 - perm[1] = 2 is divisible by i = 1
                 - i = 2 is divisible by perm[2] = 1

Example 2:
Input: n = 1
Output: 1


Constraints:
1 <= n <= 15
"""


class Solution:
    """
对数组每个位置, 依次遍历 1 到 n 个数字, 同时使用 visited 标记当次使用过的数字

JY: 性能较差
    """
    def countArrangement_v1(self, n: int) -> int:
        return self._count_arrangement(n, 1, [False] * (n+1))

    def _count_arrangement(self, n, start, visited):
        if start > n:
            return 1

        count = 0
        # jy: 遍历数值 1 至 n;
        for i in range(1, n+1):
            # jy: 如果数值已经被访问过, 则直接跳过当前循环;
            if visited[i]:
                continue
            # jy: 如果数值没有被访问过, 则将该数值设置为已访问;
            visited[i] = True
            if start % i == 0 or i % start == 0:
                count += self._count_arrangement(n, start + 1, visited)
            visited[i] = False

        return count

    """
解法2: 和回溯差不多, 每次填入一个合理的可选的数, 直到最终填出优美的排列, 才累加 1;
采用记忆化递归, 这样遇到相同位置剩余可选的数相同的情况时, 不需要再计算; (注意可以不
记录到达第几个数, 因为从 available 的长度即可推); 更新了最佳状态压缩, 按可填入个数
递归;

JY: 性能好
    """
    def countArrangement_v2(self, n: int) -> int:
        canFill = defaultdict(list)
        for i in range(1, n+1):
            for j in range(1, n+1):
                # jy: 用字典保存每个位置可以填入的数值;
                if j % i == 0 or i % j == 0:
                    canFill[i].append(j - 1)
        # jy: 根据可填入数字的个数排序, 优先填入个数少的;
        order = sorted(canFill.keys(), key=lambda x: len(canFill[x]))
        end = (1 << n) - 1

        @lru_cache(None)
        def dfs(state):
            # jy: 全部填入
            if state == end:
                return 1
            cnts = ans = 0
            # 当前该填第几个位置
            for i in range(n):
                if (1 << i) & state:
                    cnts += 1
            # 当前位置可以填哪些数
            for i in canFill[order[cnts]]:
                # 哪些数还没被填
                if not ((1 << i) & state):
                    ans += dfs(state ^ (1 << i))
            return ans

        return dfs(0)


n = 2
# Output: 2
res = Solution().countArrangement_v1(n)
print(res)


n = 1
# Output: 1
res = Solution().countArrangement_v2(n)
print(res)


