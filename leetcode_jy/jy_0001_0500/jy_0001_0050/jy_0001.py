# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
# jy: 记录该题的难度系数
type_jy = "S"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Two-Sum(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "巧用字典"


"""
Given an array of integers, return indices of the two
numbers such that they add up to a specific target.  You
may assume that each input would have exactly one solution,
and you may not use the same element twice.


Example:
nums = [2, 7, 11, 15]
target = 9
output: [0, 1] (Because nums[0] + nums[1] = 2 + 7 = 9)
"""


from typing import List


class Solution:
    """
解法1: 假设 n + m = target, 如果 n 在数组中, 且 m 也在数组中, 则
有对应的一组数满足条件

因此可以遍历数组中的每一个元素 n, 判断 ``target - n`` 是否在数组中,
如果存在则返回 ``target - n`` 与 n 的下标

哈希表获取元素的复杂度是 O(1), 算法整体的复杂度为 O(n)

    """
    def twoSum_v1(self, nums: List[int],
                  target: int) -> List[int]:
        mapping = {}
        for index, num in enumerate(nums):
            if target - num in mapping:
                # jy: 如果有多组满足条件的组合, 则可以定义一个列表
                #     存放相应的组合, 最后再返回相应列表(此处的
                #     return 需要修改)
                return [mapping[target - num], index]
            # jy: 以下 else 语句可以简化: 由于以上的 if 语句会直
            #     接 return, 故以下没必要有 else 逻辑存在, 直
            #     接 ``mapping[num] = index`` 即可(需回退一次
            #     原先的缩进)
            else:
                mapping[num] = index
        # jy: 如果不存在满足要求的两个数, 则返回 [-1, -1] (如果确
        #     定是存在的, 则这部分代码可省略)
        return [-1, -1]

    """
解法2: 不使用字典的方式(性能下降, 非空间换时间)
    """
    def twoSum_v2(self, nums: List[int],
                  target: int) -> List[int]:
        for idx, num in enumerate(nums):
            if target - num in nums and nums.index(target - num) != idx:
                return [idx, nums.index(target - num)]
                
    """
找出 nums 列表中所有和为 target 的二元组组合 (要求组合中同一
个数值不重复使用)

在解法 1 的基础上, 碰到符合要求的一对数后将其加入列表, 并将其从
mapping 中剔除, 防止重复使用

如果进一步要求符合要求的一对数不能相同, 则可进一步定义一个集合,
用于存储满足要求的一对数, 后续再次碰到满足要求的一对数的其中一个
数时, 只需判断该数是否在该集合中, 如果已经在该集合中, 表明基于该
数构成的一对满足要求的数已经存在, 直接跳过即可
    """
    def twoSum_v3(self, nums: List[int], target: int,
                  deduplicate=True) -> List[int]:
        mapping = {}
        ls_res = []
        # jy: 用于记录已经确认过满足要求的一对数(记录之后, 后续方便去重)
        set_done = set()
        for index, num in enumerate(nums):
            #if target - num in mapping:
            if target - num in mapping and target - num not in set_done:
                # jy: 将目标下标值存储到 ls_res, 并从 mapping 中剔除
                #     防止相同数值后续重复使用
                ls_res.append([mapping.pop(target - num), index])
                # jy: 如果要求去重, 则已经得到过的一对数要添加
                #     到 set_done 集合中
                if deduplicate:
                    set_done.add(target - num)
                    set_done.add(num)
            else:
                mapping[num] = index
        return ls_res


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
# jy: [[0, 1], [2, 3], [5, 6], [10, 11]]
print(res)

res = Solution().twoSum_v3(nums, target, False)
# jy: [[0, 1], [2, 3], [5, 6], [7, 8], [10, 11], [12, 13]]
print(res)


nums = [1, 5, 2, 4, 3, 3, 3, 5, 4, 3, 3]
target = 6
res = Solution().twoSum_v3(nums, target)
# jy: [[0, 1], [2, 3], [4, 5]]
print(res)


res = Solution().twoSum_v3(nums, target, False)
# jy: [[0, 1], [2, 3], [4, 5], [6, 9]]
print(res)



