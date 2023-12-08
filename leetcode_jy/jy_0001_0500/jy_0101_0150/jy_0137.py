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
title_jy = "Single-Number-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an integer array ``nums`` where every element appears three times except
for one, which appears exactly once. Find the single element and return it. You
must implement a solution with a linear runtime complexity and use only constant
extra space.


Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99


Constraints:
1) 1 <= nums.length <= 3 * 10^4
2) -2^31 <= nums[i] <= 2^31 - 1
3) Each element in nums appears exactly three times except for one element which
   appears once.
"""


from typing import List


class Solution:
    """
题目中明确了数字的范围是 32 位整型(-2^31 <= nums[i] <= 2^31 - 1), 所以从低位遍历
到高位, 将所有数字的二进制对应位相加, 由于除了一个数字外其余数字都出现了 3 次, 故
所有数字的当前位之和与 3 求余所得数就是目标数字对应所在位的二进制结果;

JY: 执行效率也不比 以下方法高;
    """
    def singleNumber_v1(self, nums: List[int]) -> int:
        result = 0

        for i in range(32):
            sum = 0

            for num in nums:
                # jy: 左移 i 位后(最开始 i 为 0), 和 1 做与运算(得出最右侧一位的数值)
                sum += ((num >> i) & 1)

            if sum % 3 == 1:
                if i == 31:
                    # jy: 1 << 31 表示 1 左移 31 位(即 2^31);
                    # print(result - (1 << 31))
                    print("result============== ", bin(result))
                    print("1 << 31 (2^31) ============== ", bin(1 << 31))
                    print("result - (1 << 31) ============== ", bin(result - (1 << 31)))
                    result -= (1 << 31)
                # jy: 如果所有数第 i 位上的二进制结果不是 3 的倍数, 即表明仅出现一次的那个
                #     数在第 i 位的二进制结果是 1, 则将 1 左移 i 位后加上上一轮 result 结
                #     果(即出现一次的数的第 i 位之前的结果)即为该数到当前位的真正结果;
                else:
                    result |= 1 << i
        return result

    def singleNumber_v2(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)

    def singleNumber_v2_2(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans


    """
解法3: 性能极佳;
https://leetcode-cn.com/problems/single-number-ii/solution/single-number-ii-mo-ni-san-jin-zhi-fa-by-jin407891/

https://leetcode-cn.com/problems/single-number-ii/solution/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetc-23t6/
    """
    def singleNumber_v3(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones

    def singleNumber_jy(self, nums: List[int]) -> int:
        str_ = ""
        for i in range(32):
            sum = 0
            for num in nums:
                # jy: 左移 i 位后(最开始 i 为 0), 和 1 做与运算(得出最右侧一位的数值)
                sum += ((num >> i) & 1)

            if sum % 3 == 1:
                str_ = "1" + str_
            else:
                str_ = "0" + str_
        print("====str_=====", str_)
        # jy: 如果二进制结果最高位是 1, 则对应为负数(此时对于的 str_ 为该负数的补码表示形
        #     式), 将 str_ 对于的二进制表示取反加 1 后对应的数值(即为该负数去掉最高位的符
        #     号位后的原码表示)即为该负数的绝对值; 二进制数取反加 1 对应的数值等同于先求得
        #     二进制对应的数值后再加 1;
        if str_[0] == "1":
            tmp_str = ""
            for i in str_:
                if i == "0":
                    tmp_str += "1"
                else:
                    tmp_str += "0"
            return - (int(tmp_str, 2) + 1)
        else:
            return int(str_, 2)


nums = [2, 2, 3, 2]
# Output: 3
res = Solution().singleNumber_v1(nums)
print(res)


nums = [0, 1, 0, 1, 0, 1, 99]
# Output: 99
res = Solution().singleNumber_jy(nums)
print(res)


nums = [-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]
# Output: -4
# res = Solution().singleNumber_jy(nums)
res = Solution().singleNumber_v2(nums)
print(res)


print(len("1111111111111111111111111111100"))


