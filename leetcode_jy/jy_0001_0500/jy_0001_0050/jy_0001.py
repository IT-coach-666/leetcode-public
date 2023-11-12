# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *

#from leetcode_jy.jy_utils import test_name
#print("============= ", test_name)


"""
Given an array of integers, return indices of the two numbers such that they 
add up to a specific target.  You may assume that each input would have exactly 
one solution, and you may not use the same element twice.


Example:
nums = [2, 7, 11, 15]
target = 9
output: [0, 1] (Because nums[0] + nums[1] = 2 + 7 = 9)
"""


from typing import List


class Solution:
    """
解法1: 假设 n + m = target, 如果 n 在数组中, 且 m 也在数组中, 则有对应的一组数满足条件;

因此可以遍历数组中的每一个元素 n, 判断 ``target - n`` 是否在数组中, 如果存在则返回
``target - n`` 与 n 的下标;

算法的复杂度: ``f(n) * O(n)``, 其中 f(n) 为判断 ``target - n`` 是否在数组中的复杂度; 
为了降低整体的复杂度, f(n) 最好是 O(lg(n)) 甚至 O(1); 哈希表获取元素的复杂度是 O(1), 因
此使用哈希表可以将整个算法的复杂度可以降为 O(n);
    """
    def twoSum_v1(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for index, num in enumerate(nums):
            if target - num in mapping:
                # jy: 如果有多组满足条件的组合, 则可以定义一个列表存放相应的组合, 最后再
                #     返回相应列表(此处的 return 需要修改)
                return [mapping[target - num], index]
            # jy: 以下 else 语句可以简化: 由于以上的 if 语句会直接 return, 故以下没必要
            #     有 else 逻辑存在, 直接 ``mapping[num] = index`` 即可(需回退一次原先
            #     的缩进);
            else:
                mapping[num] = index
        # jy: 如果不存在满足要求的两个数, 则返回 [-1, -1] (如果确定是存在的, 则这部分代
        #     码可省略)
        return [-1, -1]

    """
解法2: 不使用字典的方式(性能下降, 非空间换时间)
    """
    def twoSum_v2(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            if target - num in nums and nums.index(target - num) != idx:
                return [idx, nums.index(target - num)]

    """
题目变换: 找出 nums 列表中所有和为 target 的二元组组合 (要求组合不重复)

以下解法复杂化了, 更优解思路同解法 1: 在解法 1 的基础上, 碰到符合要求的一对数
后将其加入二元组列表, 并将对应的数值加入集合(该集合可用于限制同样的一组数重复出
现, 如果没有该限制, 可以不使用该集合), 为了防止数值的重复使用, 再将原先添加入
到 mapping 字典的数值剔除; 直到遍历完整个数组为止;
    """
    def twoSum_v3(self, nums, target):
        # jy: 统计数值以及其出现的次数;
        dict_num_count = {}
        dict_pair_count = {}
        is_visited = set()
        for num in nums:
            if num in dict_num_count:
                dict_num_count[num] += 1
            else:
                dict_num_count[num] = 1

        for i, count in dict_num_count.items():
            j = target - i
            if j in dict_num_count and j not in is_visited:
                if i == j:
                    if dict_num_count[i] >= 2:
                        dict_pair_count[(i, j)] = dict_num_count[i] // 2
                else:
                    dict_pair_count[(i, j)] = min(dict_num_count[i], 
                                                  dict_num_count[j])
            # jy: 以下代码可以再缩进, 不会产生影响;
            is_visited.add(i)
            is_visited.add(j)
        return dict_pair_count

    def twoSum_2022_02_27(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for idx, num in enumerate(nums):
            if target - num in dict_:
                return [idx, dict_[target - num]]
            # jy: 以下 else 语句可以简化: 由于以上的 if 语句会直接 return, 故以下的没
            #     必要有 else 逻辑存在, 直接 ``dict_[num] = idx`` 即可(需回退一次原先
            #     的缩进);
            else:
                dict_[num] = idx


nums = [2, 7, 11, 15]
target = 9
res = Solution().twoSum_v1(nums, target)
print(res)


nums = [1, 8, 2, 7, 11, 15]
target = 9
res = Solution().twoSum_v2(nums, target)
print(res)


nums = [1, 8, 2, 7, 11, 5, 4, 5, 4, 15, 9, 0, 9, 0]
target = 9
res = Solution().twoSum_v3(nums, target)
print(res)

nums = [1, 5, 2, 4, 3, 3, 3, 5, 4, 3, 3]
target = 6
res = Solution().twoSum_v3(nums, target)
print(res)



