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
title_jy = "Longest-Consecutive-Sequence(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an unsorted array of integers nums, return the length of the longest consecutive
elements sequence. You must write an algorithm that runs in O(n) time.


Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


from typing import List


class Solution:
    """
解法1: 首先将 nums 放入 Set, 然后遍历 nums, 对当前数 x, 判断 x-1 是否在 Set 中, 如果
不在, 说明 x 有可能是某个连续子序列的第一个数字, 所以一直遍历 x+1, x+2, ...,
直到 x + k 不在 Set 中, 说明连续子序列的终结, 求出该子序列的长度;

虽然用到了双重循环, 但是整体算法的复杂度依然是O(n), 因为每个连续子序列最多只处
理一次, 所有连续子序列的长度加起来不超过 n, 在不处理连续子序列的情况下单次循环
的时间复杂度是O(1), 所以整体的时间复杂度是O(n)
    """
    def longestConsecutive_v1(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        # jy: 遍历数字集合, 判断当前数值 x 是否有可能是某个连续子序列的第一个数值;
        #     (如果 x-1 也在集合 nums 中, 则 x 肯定不是连续子序列的第一个数值)
        for x in nums:
            # jy: 如果 x-1 不在 nums 集合中, 表明其可能是连续子序列的第一个数字, 则
            #     不断在该 x 的基础上加 1, 找出连续子序列的最后一个数值, y 最终会是
            #     比连续子序列的最后一个数值大 1 的数值(该数值不在 nums 集合中);
            if x-1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                # jy: 由于 y 总是比连续子序列的最后一个数值大于 1(不在 nums 集合中),
                #     故 y - x 即为连续子序列的长度;
                max_length = max(max_length, y - x)
        return max_length

    """
解法2: 用哈希表存储每个值对应连续区间的长度;
遍历数组中的每个数值, 若数值已在哈希表中, 则跳过不做处理; 若数值不在哈希表中,
则取出该数值左右相邻数的已有连续区间长度 left 和 right, 并计算当前数的区间长
度, 为: cur_length = left + right + 1, 根据 cur_length 更新最大长度 max_length,
同时更新区间最左以及最右两端点的所在子序列的长度值(每次确保最左和最右两个值得
到正确更新即可, 因为下一轮循环中只会利用到这两端值的其中一个)

JY: LeetCode 上运行时间比解法 1 差些;
    """
    def longestConsecutive_v2(self, nums: List[int]) -> int:
        dict_ = {}
        max_length = 0
        for num in nums:
            if num not in dict_:
                # jy: 以 nums = [2, 1, 3] 为例进行思考, 每次循环后都会确保连续子序
                #     列区间的最左和最右侧的值得到更新, 更新为截止当轮循环时的连续
                #     子序列的长度(每次确保最左和最右两个值得到正确更新即可, 因为下
                #     一轮循环中只会利用到这两端值的其中一个)
                left = dict_.get(num - 1, 0)
                right = dict_.get(num + 1, 0)
                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length

                # jy: 对 num 的赋值不能忽略, 否则 [-4, -2, 0, 5, -1, 7, 6, 6, -3] 会返回 7 (实际
                #     应该返回 5); 因为当 5 和 7 均遍历得到后, 继续遍历 6 时, 5 和 7 对应的哈希表
                #     值会被更新为 3, 而此时 6 没被记录入哈希表, 下一轮重复遍历 6 时, 由于 6 不再
                #     哈希表中, 则会继续更新 5 和 7 的值为 7; 因此该项不能注释掉, 目的是确保遍历到
                #     相同数值时不会被重复计算; 其实只要该项遍历到后, 加入哈希表即可, 不要求其值对
                #     应值是否等于 cur_length, 因为只要确保连续子序列的两端的数值对应的哈希值正确即
                #     可, 当 num 是属于两端的数值时, 即使此处没正确赋值, 但由于这种情况下, 后续 left
                #     或 right 至少是有一个是 0 的, 也会将其纠正为正确的数值;
                dict_[num] = cur_length

                dict_[num - left] = cur_length
                dict_[num + right] = cur_length

        return max_length

"""
nums = [100, 4, 200, 1, 3, 2]
# Output: 4
res = Solution().longestConsecutive_v1(nums)
print(res)


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9
res = Solution().longestConsecutive_v1(nums)
print(res)
"""


nums = [-4, -2, 0, 5, -1, 7, 6, 6, -3]
# 5
res = Solution().longestConsecutive_v2(nums)
print(res)


