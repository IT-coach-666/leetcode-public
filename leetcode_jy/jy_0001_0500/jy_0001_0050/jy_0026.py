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
title_jy = "remove-duplicates-from-sorted-array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "双指针 | 巧用 python 内置函数"


"""
原地删除非严格递增排列的数组 nums 中重复出现的元素, 使每个元素只出现一次, 返
回删除后数组的新长度; 元素的相对顺序应该保持一致

考虑 nums 的唯一元素的数量为 k, 更改数组 nums, 使 nums 的前 k 个元素包含唯一
元素, 并按它们最初在 nums 中出现的顺序排列; nums 的其余元素与 nums 的大小不
重要; 返回 k


系统会用下面的代码来测试你的题解:
int[] nums = [...];             // 输入数组
int[] expectedNums = [...];     // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

 

示例 1:
输入: nums = [1, 1, 2]
输出: 2, nums = [1, 2, _]
解释: 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1 和 2;
      不需要考虑数组中超出新长度后面的元素

示例 2:
输入: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
输出: 5, nums = [0, 1, 2, 3, 4]
解释: 函数应该返回新的长度 5
 

Notes:
1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
"""


class Solution:
    """
解法 1: 基于数据结构, 时间复杂度 O(n), 空间复杂度 O(n)
    """
    def removeDuplicates_v1(self, nums: List[int]) -> int:
        # jy: col 记录去重后的结果, 最终返回的 k 值即 col 的长度,
        #     随后将 col 的元素重新填入 nums 中
        col = []
        for i in range(len(nums)):
            if nums[i] not in col:
                col.append(nums[i])
        
        k = len(col)
        nums[:k] = col
        return k


    """
解法 2: 双指针, 时间复杂度 O(n), 空间复杂度 O(1)

双指针在一个序列中同向变动
    """
    def removeDuplicates_v2(self, nums: List[int]) -> int:
        # jy: 双指针初始化为列表中的前两个位置
        left, right = 0, 1
        # jy: k 初始化为 1
        k = 1
        while right < len(nums):
            # jy: 如果右指针与左指针的值相同, 则右指针不断右移; 如果不同,
            #     则左指针后移一位, 并与右指针的值进行交换, 然后左右指针均
            #     加 1, k 也加 1
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left+1], nums[right] = nums[right], nums[left+1]
                left += 1
                right += 1
                k += 1
        return k


    """
解法 3: 巧用内置函数 set 和 sorted
    """
    def removeDuplicates_v3(self, nums: List[int]) -> int:
        # jy: 对 nums 中的元素去重后排序, 并将排序结果重新赋值给 nums 列表
        for i, x in enumerate(sorted(set(nums))):
            nums[i] = x
        return i + 1



nums = [1, 1, 2]
# jy: 2, nums = [1, 2, _]
res = Solution().removeDuplicates_v1(nums)
print(res)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# jy: 5, nums = [0, 1, 2, 3, 4]
res = Solution().removeDuplicates_v2(nums)
print(res)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# jy: 5, nums = [0, 1, 2, 3, 4]
res = Solution().removeDuplicates_v3(nums)
print(res)




