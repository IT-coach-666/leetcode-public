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
title_jy = "Combination-Sum-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination
twice, and the combinations may be returned in any order.


Example 1:
Input: k = 3, n = 7
Output: [[1, 2, 4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. Using 4 different numbers in the range [1, 9],
             the smallest sum we can get is 1 + 2 + 3 + 4 = 10 and since 10 > 1, there are
             no valid combination.

Example 4:
Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.

Example 5:
Input: k = 9, n = 45
Output: [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
Explanation:  1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
There are no other valid combinations.


Constraints:
2 <= k <= 9
1 <= n <= 60
"""


from typing import List
class Solution:
    """
题解在 039_Combination-Sum.py 的基础上限制了组合的数字个数, 递归终止条件增加判断 k 是否等于 0;
    """
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self._dfs(1, 9, k, n, [], result)
        return result

    def _dfs(self, start, end, k, target, combination, result):
        """从 start 到 end 中找出 k 个不重复的数, 使得之和为 target 的所有组合, 放入 result 列表中"""
        # jy: 如果 k == 0, 且 target == 0, 表明要找的组合 combination 已经满足 k 个值且和为原先的目标值了;
        if k == 0 and target == 0:
            result.append(combination)
            return
        # jy: 先找出组合中的第一个数值: 从 start 开始循环遍历, 遍历至 end-k+2(不需遍历至末尾, 因为组合
        #    要有 k 个元素组成, 找到第一个之后还要有 k-1 个, 即组合中的第一个值在前 end - (k-1) 中找
        #    就可以, 即在前 end-k+1 个元素中遍历查找, 以下 range(start, end-k+2) 的最大值也即 end-k+1)
        for n in range(start, end - k + 2):
            if n > target:
                break
            # jy: 将 n 作为组合中的一个元素后, 即可从 n+1 后开始查找, 因为组合中的元素不会重复;
            self._dfs(n+1, end, k-1, target - n, combination[:] + [n], result)

k = 3
n = 7
# Output: [[1, 2, 4]]
res = Solution().combinationSum3(k, n)
print(res)


k = 3
n = 9
# Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
res = Solution().combinationSum3(k, n)
print(res)


k = 4
n = 1
# Output: []
res = Solution().combinationSum3(k, n)
print(res)


k = 3
n = 2
# Output: []
res = Solution().combinationSum3(k, n)
print(res)


k = 9
n = 45
# Output: [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
res = Solution().combinationSum3(k, n)
print(res)


