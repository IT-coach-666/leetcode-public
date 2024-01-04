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
title_jy = "Remove-Duplicates-from-Sorted-Array-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "单指针 + 统计变量 | IMP"



"""
Given an integer array `nums` sorted in non-decreasing order, remove some
duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array 
`nums`. More formally, if there are `k` elements after removing the 
duplicates, then the first `k` elements of `nums` should hold the final 
result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

Do not allocate extra space for another array. You must do this by modifying
the input array in-place with O(1) extra memory.


Custom Judge:
The judge will test your solution with the following code:
int[] nums = [...];             // Input array
int[] expectedNums = [...];     // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation
assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}


If all assertions pass, then your solution will be accepted.


Example 1:
Input: nums = [1, 1, 1, 2, 2, 3]
Output: 5, nums = [1, 1, 2, 2, 3]
Explanation: Your function should return length = 5, with the first five
             elements of `nums` being 1, 1, 2, 2 and 3 respectively. It
             doesn't matter what you leave beyond the returned length.

Example 2:
Input: nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
Output: 7, nums = [0, 0, 1, 1, 2, 3, 3]


Constraints:
1) 1 <= nums.length <= 3 * 10^4
2) -10^4 <= nums[i] <= 10^4
3) `nums` is sorted in non-decreasing order.
"""


class Solution:
    """
解法 1: 单指针 + 变量计数

和 0026 (remove-duplicates-from-sorted-array) 类似, 在其基础上定义一个 
duplicates 变量, 标记当前数字重复的次数, 初始值为 1; 从第二个数开始遍历
数组, 如果 nums[tail] != nums[i], 说明遇到了新的数字, 将 duplicates 置
为 1, 否则 duplicates 加 1, 如果 duplicates <= 2, 则对 tail 加 1, 并更
新 nums[tail] 为当前数字
    """
    def removeDuplicates_v1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # jy: tail 指针用于记录当前统计的最新数值的下标, tail 指针及其
        #     之前的部分为已符合要求的结果
        tail = 0
        # jy: 统计当前最新元素 (即 tail 指针所指元素) 出现的次数
        duplicates = 1
        # jy: 从数组的第 2 个元素开始遍历
        for i in range(1, len(nums)):
            # jy: 如果数值 nums[i] 与 tail 指针对应的数值不等, 表明当前最
            #     新元素 (即 tail 指针所指元素) 需更新为 nums[i], 对应的
            #     重复次数 duplicates 重新初始化为 1
            if nums[tail] != nums[i]:
                duplicates = 1
            # jy: 如果 nums[i] 与 tail 指针对应的数值相等, 则 tail 指针对
            #     应的数值的统计量加 1
            else:
                duplicates += 1

            # jy: 如果 tail 指针对应的数值的出现次数 duplicates 小于等于 2,
            #     则将 tail 前进一位、用于存放最新的遍历数值 nums[i]; 如果
            #     nums[i] 与 tail 相等, 且使得重复次数大于 2 了, 则表明最新
            #     的 nums[i] 不能再纳入 tail 之后的位置, 直接跳过, 待后续遍
            #     历寻找到其它与当前 tail 指针的值不等的结果后, 再将其纳入
            #     tail 之后的位置
            if duplicates <= 2:
                tail += 1
                nums[tail] = nums[i]
        # jy: 最终返回去重后的长度, 即尾部下标加 1
        return tail + 1


    """
解法 2: 统计待删除的元素下标 (需额外分配空间), 最后删除 (列表删除操作需产生
移位, 时间复杂度也有所增加)
    """
    def removeDuplicates_v2(self, nums: List[int]) -> int:
        d = []
        if not nums:
            return 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            if count > 2:
                d.append(i)
        # jy: 需要从下标大的元素开始删除 (防止错删)
        for i in d[::-1]:
            del nums[i]
        return len(nums)


    """
解法 3: 改写解法 1 (更通俗易懂, 适合允许重复次数较少的场景)

初始化 nums 的前两个数值, 从第三个数值开始循环遍历, 当所遍历的数值等于 tail
指针以及其前一个的值时, 跳过忽略, 否则 tail 指针前进一步并记录遍历的数值
    """
    def removeDuplicates_v3(self, nums: List[int]) -> int:
        tail = 1
        for num in nums[2:]:
            if num == nums[tail] and num == nums[tail-1]:
                continue
            else:
                tail += 1
                nums[tail] = num
        return tail + 1


nums = [1, 1, 1, 2, 2, 3]
# Output: 5, nums = [1, 1, 2, 2, 3]
res = Solution().removeDuplicates_v1(nums)
print(res, nums)

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# Output: 7, nums = [0, 0, 1, 1, 2, 3, 3]
res = Solution().removeDuplicates_v1(nums)
print(res, nums)

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# Output: 7, nums = [0, 0, 1, 1, 2, 3, 3]
res = Solution().removeDuplicates_v2(nums)
print(res, nums)

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# Output: 7, nums = [0, 0, 1, 1, 2, 3, 3]
res = Solution().removeDuplicates_v3(nums)
print(res, nums)


