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
title_jy = "Continuous-Subarray-Sum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a list of non-negative numbers and a target integer k, write a function to check if the
array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is,
sums up to n*k where n is also an integer.


Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.


Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""

from typing import List

class Solution:
    """
这道题和 560_Subarray-Sum-Equals-K.py 类似, 但是需要额外一个数学知识支撑:
如果 a % k = b % k, 则 (a-b) % k = 0, 也就是 a-b 是 k 的倍数, 证明如下:
令 a % k = b % k = c, 则:
a = a'k + c
b = b'k + c
a-b = a'k + c - (b'k + c) = k(a' - b')
所以 a-b 能被 k 整除;

在这道题中, a 就是 sums[i], b 就是 sums[j] (关于 sums 的定义可参考 560_Subarray-Sum-Equals-K.py),
当 sums[i] % k == sums[j] % k 时, sums[i] - sums[j] 能够被 k 整除, 即 sums[j+1] + sums[j+2] + ... + sums[i]
能被 k 整除, 由于题中需要满足条件的子数组的长度至少为 2, 所以 i-(j+1) >= 1, 也就是 i-j >= 2;

所以, 我们只需要遍历数组, 并将当前累加的和 sums[i] 与 k 取模, 将其放入一个哈希表中作为键,
哈希表的值为当前数组的下标, 如果哈希表中已经存在了该键, 则判断当前数组下标与该键对应的值的
差是否大于等于 2;

同样的, 当 sums[i] % k == 0 时, 满足条件的子数组正好是 nums[0], nums[1], ..., nums[i], 此时不需要
找 j 使得 sums[j] % k == 0, 所以需要初始化 0 作为 key 值记录到哈希表中, 这种情况下为了保证满足条件
的子数组长度至少为 2, 则 i 需要大于等于 1, 为了使表达式 i - mapping[key] >= 2 成立(mapping[key] 对
应的值即表示与 k 取模后值为 key 的值对应的所在下标), 故选用 -1 作为哈希表初始键的值;
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum = 0
        # jy: 初始化 mapping, key 为 0 的位置下标置为 -1 (并不代表数组最后一位数值, 而是为了使得当
        #    sums[i] % k == 0 时, 可以通过 i - mapping[0] >= 2 这个条件确保 i 是 >=1 的数值)
        mapping = {0: -1}
        # jy: 遍历列表,
        for i, n in enumerate(nums):
            # jy: 求截止当前元素的累加和;
            sum += n
            # jy: 如果 k 为 0, 则 key 一直都是截止当前为止的 sum 值; 否则 key 为 sum % k;
            key = sum if k == 0 else sum % k
            # jy: 如果 key 已经在 mapping 中存在, 则表明 当前的 sum_new % k 与之前的 sum_old % k
            #    的值相等, 表明 sum_new - sum_old 是 k 的倍数, 进一步根据当前 sum_new 的下标 i
            #    与 sum_old 的下标 mapping[key] 判断两者之间是否是至少两个数值, 如果是则直接返
            #    回 True;
            if key in mapping:
                if i - mapping[key] >= 2:
                    return True
            # jy: 如果 key 不在 mapping 中, 则将其作为 key 加入, value 为当前 sum 值对应的 n 的坐标位置;
            else:
                mapping[key] = i

        return False


nums = [23, 2, 4, 6, 7]
k=6
# Output: True
res = Solution().checkSubarraySum(nums, k)
print(res)


nums = [23, 2, 6, 4, 7]
k=6
# Output: True
res = Solution().checkSubarraySum(nums, k)
print(res)


nums = [23, 2, 6, 4, 7]
k=0
# Output: False
res = Solution().checkSubarraySum(nums, k)
print(res)


nums = [23, 2, 0, 0, 7]
k=0
# Output: True
res = Solution().checkSubarraySum(nums, k)
print(res)


# nums = [0, 2, 0, 2, 7]
nums = [2, 0, 2, 0, 7]
k=0
# Output: False
res = Solution().checkSubarraySum(nums, k)
print(res)


