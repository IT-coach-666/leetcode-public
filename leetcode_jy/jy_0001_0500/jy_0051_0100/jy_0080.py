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
tag_jy = ""



"""
Given a sorted array nums, remove the duplicates in-place such that duplicates
appeared at most twice and return the new length. Do not allocate extra space
for another array; you must do this by modifying the input array in-place
with O(1) extra memory.


Clarification:
Confused why the returned value is an integer, but your answer is an array?
Note that the input array is passed in by reference, which means a modification
to the input array will be known to the caller.


Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}


Example 1:
Input: nums = [1, 1, 1, 2, 2, 3]
Output: 5, nums = [1, 1, 2, 2, 3]
Explanation: Your function should return length = 5, with the first five elements of
nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the
returned length.

Example 2:
Input: nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
Output: 7, nums = [0, 0, 1, 1, 2, 3, 3]


Constraints:
• 1 <= nums.length <= 3 * 10^4
• -10^4 <= nums[i] <= 10^4
• nums is sorted in ascending order.
"""



from typing import List
class Solution:
    """
解法1: 和 026_remove-duplicates-from-sorted-array.py 类似, 在其基础上定义一个 duplicates 变量,
标记当前数字重复的次数, 初始值为 1; 从第二个数开始遍历数组, 如果 nums[tail] != nums[i], 说明遇
到了新的数字, 将 duplicates 置为 1, 否则 duplicates 加 1, 如果 duplicates <= 2, 则对 tail 加 1,
并更新 nums[tail] 为当前数字;
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # jy: 以 tail 指针结尾的数组(tail 表示数组下标)表示去重的结果;
        tail = 0
        duplicates = 1
        # jy: 从数组中的第 2 个元素开始遍历;
        for i in range(1, len(nums)):
            # jy: 统计数值 nums[i] 的出现次数
            if nums[tail] != nums[i]:
                duplicates = 1
            else:
                duplicates += 1
            # jy: 如果当前 nums[i] 出现的次数(当前值算1次)小于或等于 2, 则 tail
            #    前进 1 位, 并将当前 tail 值设置为 nums[i]
            if duplicates <= 2:
                tail += 1
                nums[tail] = nums[i]
        # jy: 最终返回去重后的长度, 即尾部下标加 1;
        return tail + 1

    """
JY: 统计待删除的元素下标, 最后删除(由于不能边循环边删除, 需要额外分配空间, 不如解法 1);
    """
    def removeDuplicates_jy(self, nums: List[int]) -> int:
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
        # jy: 需要从下标大的元素开始删除(防止错删);
        for i in d[::-1]:
            del nums[i]
        return len(nums)

    """
JY: 初始化 nums 的前两个数值, 从第三个数值开始循环遍历, 只有当第三个数值等于其
前两位数值时, 跳过忽略, 否则将第三个数值加入到末尾(tail 记录末尾下标);
    """
    def removeDuplicates_jy2(self, nums: List[int]) -> int:
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
res = Solution().removeDuplicates(nums)
print(res, nums)

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# Output: 7, nums = [0, 0, 1, 1, 2, 3, 3]
res = Solution().removeDuplicates(nums)
print(res, nums)

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# Output: 7, nums = [0, 0, 1, 1, 2, 3, 3]
res = Solution().removeDuplicates_jy(nums)
print(res, nums)

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# Output: 7, nums = [0, 0, 1, 1, 2, 3, 3]
res = Solution().removeDuplicates_jy2(nums)
print(res, nums)


