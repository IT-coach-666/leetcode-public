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
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Find-Smallest-Letter-Greater-Than-Target(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a list of sorted characters letters containing only lowercase letters, and given a
target letter target, find the smallest element in the list that is larger than the given
target. Letters also wrap around. For example, if the target is target = 'z' and
letters = ['a', 'b'], the answer is 'a'.


Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"


Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""


from typing import List
import bisect


class Solution:
    """
解法1: 首先处理边界情况, 如果最后一个元素比 target 小或等于, 直接返回数组的第一个元素,
如果不是, 则对数组进行二分查找;
    """
    def nextGreatestLetter_v1(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters) - 1
        # jy: 处理边界情况: 如果最后一个字符都比 target 小或等于, 则直接返回
        #     数组的第一个元素;
        if letters[-1] <= target:
            return letters[0]

        # jy: 二分查找
        while low <= high:
            # jy: middle = (low + high) // 2 同样能计算出中值, 但有风险(low 和 high 过大
            #     时, 相加可能超出数值范围; python 中不会出现该问题)
            middle = low + (high - low) // 2
            letter = letters[middle]
            # jy: 目标是要找比 target 大的最小元素, 所以如果当前的中间字符小于或等于 target,
            #     则 low 更新为 middle+1
            if letter <= target:
                low = middle + 1
            # jy: 如果当前中间字符大于 target, 则 high 更新为 middle-1 (更新后, 此时的 letters[high]
            #     可能已经小于 target 了, 不过不要紧, 这种情况下后续的循环中会使得 low 不断更新为
            #     middle+1, 直到 low == high 时, 做最后一次更新, 即更新为 high 后面的一位, 即为目
            #     标所求的值)
            else:
                high = middle - 1

        return letters[low]

    """
JY: 基于已有的 bisect 包实现; 前提是列表中的元素是有序的, 且通过比较运算符能判断
(如果比较运算符不能判断, 则需对列表元素进行类封装, 并重写 __ge__ 方法(__gt__ 或
__lt__ 或 __le__), 使得能通过比较运算符判断大小)
    """
    def nextGreatestLetter_jy(self, letters: List[str], target: str) -> str:
        idx = bisect.bisect_right(letters, target)
        if idx == len(letters):
            return letters[0]
        return letters[idx]


letters = ["c", "f", "j"]
target = "a"
# Output: "c"
res = Solution().nextGreatestLetter_v1(letters, target)
print(res)


letters = ["c", "f", "j"]
target = "c"
# Output: "f"
res = Solution().nextGreatestLetter_v1(letters, target)
print(res)


letters = ["c", "f", "j"]
target = "d"
# Output: "f"
res = Solution().nextGreatestLetter_jy(letters, target)
print(res)


letters = ["c", "f", "j"]
target = "g"
# Output: "j"
res = Solution().nextGreatestLetter_jy(letters, target)
print(res)


letters = ["c", "f", "j"]
target = "j"
# Output: "c"
res = Solution().nextGreatestLetter_v1(letters, target)
print(res)


letters = ["c", "f", "j"]
target = "k"
# Output: "c"
res = Solution().nextGreatestLetter_jy(letters, target)
print(res)



