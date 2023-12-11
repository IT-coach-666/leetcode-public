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
title_jy = "Circular-Array-Loop(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are playing a game involving a circular array of non-zero integers ``nums``. Each
``nums[i]`` denotes the number of indices forward/backward you must move if you are
located at index ``i``:
If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.

Since the array is circular, you may assume that moving forward from the last element puts
you on the first element, and moving backwards from the first element puts you on the last
element.

A cycle in the array consists of a sequence of indices ``seq`` of length ``k`` where:
1) Following the movement rules above results in the repeating index sequence:
   seq[0] -> seq[1] -> ... -> seq[k-1] -> seq[0] -> ...
2) Every ``nums[seq[j]]`` is either all positive or all negative.
3) k > 1

Return true if there is a cycle in ``nums``, or false otherwise.


Example 1:
Input: nums = [2,-1,1,2,2]
Output: true
Explanation: There is a cycle from index 0 -> 2 -> 3 -> 0 -> ...
             The cycle's length is 3.

Example 2:
Input: nums = [-1,2]
Output: false
Explanation: The sequence from index 1 -> 1 -> 1 -> ... is not a cycle because the sequence's length
             is 1. By definition the sequence's length must be strictly greater than 1 to be a cycle.

Example 3:
Input: nums = [-2,1,-1,-2,-2]
Output: false
Explanation: The sequence from index 1 -> 2 -> 1 -> ... is not a cycle because nums[1] is positive, but
             nums[2] is negative. Every nums[seq[j]] must be either all positive or all negative.


Constraints:
1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
nums[i] != 0


Follow up: Could you solve it in O(n) time complexity and O(1) extra space complexity?
"""


from typing import List


class Solution:
    """
题解: 使用一个 Map 保存下标和起点位置的映射, 遍历数组, 以当前位置为起点, 依
次跳到下一个位置, 如果下一个位置在 Map 中, 进一步判断下一个位置对应的起点是
否是当前位置, 如果是则找到了环, 否则跳出循环, 说明该位置已经被访问过(从该位
置开始不会找到环, 不然之前就返回 True 了)  由于遍历数组时会判断当前位置是否
在 Map 中, 所以每个位置至多被访问一次, 算法时间复杂度是O(n), 但空间复杂度也
是O(n)
    """
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = {}
        n = len(nums)

        for i in range(n):
            if i in visited:
                continue

            current = i

            while self._is_valid_cycle(i, current, nums):
                visited[current] = i

                current = (current + nums[current]) % n

                if current in visited:
                    if visited[current] == i:
                        return True

                    break

        return False

    def _is_valid_cycle(self, start, current, nums):
        return nums[current] % len(nums) != 0 \
               and ((nums[start] > 0 and nums[current] > 0)
                    or (nums[start] < 0 and nums[current] < 0))


nums = [2, -1, 1, 2, 2]
# Output: true
res = Solution().circularArrayLoop(nums)
print(res)


nums = [-1, 2]
# Output: false
res = Solution().circularArrayLoop(nums)
print(res)


nums = [-2, 1, -1, -2, -2]
# Output: false
res = Solution().circularArrayLoop(nums)
print(res)


