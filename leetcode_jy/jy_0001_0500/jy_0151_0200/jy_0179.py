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
title_jy = "Largest-Number(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 
Example 1:
Input: nums = [10, 2]
Output: "210"

Example 2:
Input: nums = [3, 30, 34, 5, 9]
Output: "9534330"
 

Constraints:
1) 1 <= nums.length <= 100
2) 0 <= nums[i] <= 10^9
"""


class Solution(object):
    """
解法 1: 
输入数组的长度会达到 100, 如果你想用 DFS 找出所有可以拼接的结果然后求最大, 那么就走偏了, 一定会超时, 而且会超出空间限制

分析一下规律：
当 nums = [10, 2] 时, 结果是 210; 其实我们就是在比较 [10, 2] 这两个数字能组合成的 210 和 102 哪个数字更大, 显然 210 更大, 所以需要把 2 放在前面;
为了避免用 int 型或 long 型越界, 需要把数字先转成字符串; 然后可以把待比较的两个数字 x, y 组合成两个新的数字 string(x) + string(y) 和 string(y) + string(x), 比较一下哪种组合构成的数字更大。
你可能会有疑问：如果拼接得到的字符串结果更大的话，那原本的整型的数字拼接结果也一定更大吗? 
答案是肯定的：首先拼接成的两个字符串一定是等长的; 等长的字符串在比较时是按照字符串的各个字符从前向后逐个比较的, 所以相当于先比较了百分位, 然后比较十分位, 最后比较个位; 所以在字符串等长的情况下, 字符串大, 对应的整型也更大; 但两个不等长的字符串就没有这个结论了, 比如 "2" > "10", 但是 2 < 10

综上, 按照下面的步骤:
1) 先把 nums 中的所有数字转字符串, 形成字符串数组 nums_str
2) 比较两个字符串 x, y 拼接的结果 x + y 和 y + x 哪个更大, 从而确定 x 和 y 谁排在前面; 将 nums_str 降序排序
3) 把整个数组排序的结果拼接成一个字符串, 并返回

注意: 如果输入的 nums 中只有 0 时, 上面的结果会返回 "00" 这样的全零字符串; 因此可以提前判断 nums 是否全为零, 或可以判断最终拼接完成的字符串中首位是不是 "0", 因为如果 nums 至少有一个数字不是 0, 那么该数字一定都会排在所有的 0 的前面

    """
    def largestNumber_v1(self, nums):
        nums_str = map(str, nums)
        compare = lambda x, y: 1 if x + y < y + x else -1
        nums_str.sort(cmp=compare)
        res = "".join(nums_str)
        if res[0] == "0":
            res = "0"
        return res

    
    
nums = [10, 2]
res = Solution().largestNumber_v1(nums)
# jy: "210"
print(res)


nums = [3, 30, 34, 5, 9]
res = Solution().largestNumber_v1(nums)
# jy: "9534330"
print(res)