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
title_jy = "Single-Number-III(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array ``nums``, in which exactly two elements appear only once and all
the other elements appear exactly twice. Find the two elements that appear only once.
You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only
constant extra space.


Example 1:
Input: nums = [1, 2, 1, 3, 2, 5]
Output: [3, 5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1, 0]
Output: [-1, 0]

Example 3:
Input: nums = [0, 1]
Output: [1, 0]


Constraints:
2 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""


from typing import List


class Solution:
    """
jy: 位运算(异或运算和与运算)的特点:
相同数值进行异或运算结果为 0;
x &= -x: 将 x 的最低位的 1 之前的位全置为 0;

在 136_Single-Number.py 的基础上, 首先对所有数字异或, 得到两个只出现一次的数字
的异或值(相同数字异或的结果均为 0), 因为这两个数字不同, 所以两者的异或值一定不
为 0, 其二进制中必然存在 1, 假设异或值为 ???10...0, 需要将其转变为 0...010...0,
即将最低位的 1 之前的位全置为 0, 这个值可通过 x &= -x 求得, 记为 mask;

记这两个不同的数为 a 和 b, 则 a xor b 后最低位的 1 (用 mask 表示) 只可能来自于 a
或 b 中的一个, 因此可以用 mask 对数组中的值进行划分(通过与运算结果是否为 0 即可划
分开), 继而将问题分为两个相同的子问题, 即找出在子数组中只出现一次的数值(其余数值均
出现两次);
    """
    def singleNumber_v1(self, nums: List[int]) -> List[int]:
        mask = 0
        result = [0, 0]
        # jy: 对所有数字进行异或操作(相同数值的异或操作结果为 0), 得到两个不同数值的
        #     异或操作结果
        for n in nums:
            mask ^= n
        # jy: 获取两个不同异或操作结果的二进制表示中的最右侧的 1, 其余位全置为 0;
        #     (其实并非一定要获取最右侧的 1, 只要获取位置为 1 的, 且将剩余位置置为 0 也
        #      可以, 因为通过该位置为 1 的二进制表示可以将两个不同的数值进行区分开, 通过
        #      其与对应数值进行与运算即可区分, 与运算的结果肯的是有一个为 0, 一个为非 0)
        mask &= -mask

        for n in nums:
            # jy: 基于 mask 将所有数值分为两派: 和 mask 进行与运算后结果为 0 的分为一派, 结果
            #     不为 0 的分为另一派, 此时两个仅出现过一次的数字就会被分隔开, 且属于同一派的
            #     其它数均出现偶数次(2 次), 故分别对两派中的所有数进行异或运算, 最终得到的结果
            #     就是只出现过一次的数字;
            if n & mask == 0:
                result[0] ^= n
            else:
                result[1] ^= n

        return result

    """
解法2: 思路同解法 1, 简化代码;
运行效率实际上也不比解法 1 强;
    """
    def singleNumber_v2(self, nums: List[int]) -> List[int]:
        num1 = 0
        xor_sum = 0
        for n in nums:
            xor_sum ^= n

        # jy: 找出 xor_sum 的最右侧一位的 1, 其它位置为 0;
        # mask = xor_sum & -xor_sum
        mask = 1
        while mask & xor_sum == 0:
            mask <<= 1

        for n in nums:
            if n & mask == 0:
                num1 ^= n
        return [num1, xor_sum ^ num1]


nums = [1, 2, 1, 3, 2, 5]
# Output: [3, 5]
res = Solution().singleNumber_v1(nums)
print(res)


nums = [-1, 0]
# Output: [-1, 0]
res = Solution().singleNumber_v1(nums)
print(res)


nums = [0, 1]
# Output: [1, 0]
res = Solution().singleNumber_v2(nums)
print(res)


# jy: 获取数值 n 的二进制表示的最右侧的 1, 其余位置均置为 0;
n = 3
print(n & -n)


