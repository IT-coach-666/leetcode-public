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
title_jy = "Max-Consecutive-Ones(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a binary array, find the maximum number of consecutive 1s in this array.


Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
             The maximum number of consecutive 1s is 3.


Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""



from typing import List



class Solution:
    """
JY: 引入累赘变量 consecutive_and (解法 2 中将其去除)

记 max_length 为最长连续的 1 的长度, length_so_far 为当前连续的 1 的长度, consecutive_and 为
length_so_far 对应子数组的起始位置至当前数字的连续与运算, 初始值为 1; 遍历数组, 将 consecutive_and
与当前数字进行与运算, 如果结果为 1, 说明当前数字是 1, 则 length_so_far 加 1, 并更新 max_length 的
值; 否则说明当前数字为 0, length_so_far 和 consecutive_and 都重置为 0, 最后返回 max_length;
    """
    def findMaxConsecutiveOnes_v1(self, nums: List[int]) -> int:
        # jy: 记录最长长度
        max_length = 0
        # jy: 记录截止当前为止的连续 1 的长度
        length_so_far = 0
        # jy: 用于判断当前值是否为 1 (值为 1 表示当前值为 1, 值为 0 表示当前值为 0);
        #    该变量可以直接去掉, 直接用遍历时的当前值进行判断即可(见解法2);
        consecutive_and = 1
        for n in nums:
            consecutive_and &= n
            if consecutive_and == 1:
                length_so_far += 1
                max_length = max(length_so_far, max_length)
            else:
                length_so_far = 0
                consecutive_and = 1
        return max_length


    """
解法 2: 解法 1 中引入 consecutive_and 属于多余, 直接遍历数组, 如果当前数字是 1, 则
length_so_far 加 1, 并更新 max_length 的值; 否则 length_so_far 重置为 0, 最后返回 max_length;
    """
    def findMaxConsecutiveOnes_v2(self, nums: List[int]) -> int:
        max_length = 0
        length_so_far = 0
        # jy-version-1: 该版本中, 如果遍历到 1 时, 每次加 1 后都进行了 max() 调用获取最大
        #               值, 实际上并非每次加 1 后都要如此操作, 只需要再次碰到 0 时, 对上次
        #               的连续加 1 结果进行判断即可(见 version-2);
        """
        for n in nums:
            if n == 1:
                length_so_far += 1
                max_length = max(length_so_far, max_length)
            else:
                length_so_far = 0
        """
        # jy-version-1: End
        # jy-version-2: 对 version-1 的优化, LeetCode 上显示执行效率大大好于 version-1;
        for n in nums:
            if n == 1:
                length_so_far += 1
            else:
                # jy: 只有当碰到值为 0 时, 才对之前连续加 1 的结果进行判断;
                max_length = max(length_so_far, max_length)
                length_so_far = 0
        # jy: 由于可能是最后一个片段是连续的 1, 而不再出现 0, 因此以上逻辑欠缺覆盖这种情况下
        #    的连续值为 1 的判断, 在此补充上;
        max_length = max(length_so_far, max_length)
        # jy-version-2: End

        return max_length


    """
解法3: 和解法 2 思想一样, 但是巧妙的运用了 0 和 1 的性质省略了 if 的判断;
如果当前数字为 0, 则 length_so_far *= n 相当于重置 length_so_far 为 0, length_so_far += n 也不会影响重置的结果;
如果当前数字为 1, 则 length_so_far *= n 不会改变 length_so_far 本身的值, length_so_far += n 正好将当前连续 1 的个数加 1;

JY: 该方案每轮循环都要进行 max() 判断, 效率较低;
    """
    def findMaxConsecutiveOnes_v3(self, nums: List[int]) -> int:
        max_length = 0
        length_so_far = 0

        for n in nums:
            length_so_far *= n
            length_so_far += n
            max_length = max(max_length, length_so_far)

        return max_length


nums = [1,1,0,1,1,1]
# Output: 3
res = Solution().findMaxConsecutiveOnes_v1(nums)
print(res)


res = Solution().findMaxConsecutiveOnes_v2(nums)
print(res)


res = Solution().findMaxConsecutiveOnes_v3(nums)
print(res)


