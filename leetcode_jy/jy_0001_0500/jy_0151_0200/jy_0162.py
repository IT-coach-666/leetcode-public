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
title_jy = "Find-Peak-Element(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
A peak element is an element that is strictly greater than its neighbors. Given an integer array 
nums, find a peak element, and return its index. If the array contains multiple peaks, return the
index to any of the peaks. You may imagine that nums[-1] = nums[n] = -∞.


Example 1:
Input: nums = [1, 2, 3, 1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1, 2, 1, 3, 5, 6, 4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index
             number 5 where the peak element is 6.


Constraints:
1 <= nums.length <= 1000
-2^31 <= nums[i] <= 2^31 - 1
nums[i] != nums[i+1] for all valid i.


Follow up: Could you implement a solution with logarithmic complexity?
"""

from typing import List

class Solution:
    """
解法1: 直接循环, 依次判断每个元素是否比它左右两边的元素大;

jy: 如果使用一个列表保存符合要求的结果(该题解中的 "return i" 部分), 最终再返回列表, 则
    该方法能找出列表中的所有 peak element;
    """
    def findPeakElement_v1(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # jy: 如果是第一个元素, 默认其比左边的元素大; 同理, 如
            #    果是最后一个元素, 默认其比右边的元素大; 即列表中
            #    如果只有一个元素, 也可认为其属于 peak element;
            larger_than_left = (i-1 >= 0 and nums[i-1] < nums[i]) or i == 0
            larger_than_right = (i+1 < len(nums) and nums[i+1] < nums[i]) or i+1 == len(nums)

            if larger_than_left and larger_than_right:
                return i

        return -1

    """
解法2: 在解法 1 的基础上优化, 不需要每次比较当前元素和左右两边的元素; 遍历数组, 只要
当前元素大于后面的元素就说明找到了 peak, 因为当第一次遇到 nums[i] 大于 nums[i+1] 时, 说
明 nums[0...i] 是升序的,  nums[i] 处为 peak, 注意最后返回 len(nums)-1, 用于处理数组始终
升序的场景, 此时最后一个元素是 peak;

jy: 第一个元素默认为比左边元素大, 最后一个元素默认比右边元素大; 因此, 当第一个元素大于第
    二个元素时, 即可认为第一个元素为 peak element; 同理, 当最后一个元素大于倒数第二个元素
    时, 也可认为最后一个元素为 peak element;
    """
    def findPeakElement_v2(self, nums: List[int]) -> int:
        # jy: 此部分 for 循环只判断到倒数第二个元素, 如果该 for 循环中没有 return 返回, 表明
        #    最后一个元素是大于倒数第二个元素的, 即最后一个元素为 peak element, for 循环结束
        #    后直接返回最后一个元素就可以(如果 for 循环中会返回, 则表明已经找到, 结束运行);
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return i

        return len(nums) - 1

    """
jy: 如果依据 v2 的思路想找出所有 peak element, 则可以在原有基础上引入一个中间变量 unvalid_idx,
    用来保存找到的符合要求的 nums[i] 的下一个元素的下标 i+1,
    """
    def findPeakElement_v2_jy(self, nums: List[int]) -> int:
        ls_peak_idx = []
        unvalid_idx = None
        # jy: 此部分循环只判断到倒数第二个元素是否符合要求;
        for i in range(len(nums) - 1):
            # jy: 即如果 i 为非 unvalid_idx, 表明 unvalid_idx 到 i 对应的元素是升序的, 此时如果
            #    nums[i] 大于 nums[i+1], 表明 i 符合要求, 同时表明 i+1 不符合要求, 记录起来;
            if unvalid_idx != i and nums[i] > nums[i+1]:
                ls_peak_idx.append(i)
                unvalid_idx = i+1
            # jy: 当以上找到一个 unvalid_idx 后, 并不代表该 unvalid_idx 之后的 i 就又是新阶段的
            #    升序了, 新阶段的 nums[i] 还是一直在降序, 则要更新 unvalid_idx 为对应的值更小的
            #    那个 i 值, 确保针对以上逻辑, 使得新阶段的 unvalid_idx 到 i 是升序, 这样只要再
            #    次碰到新的 nums[i] > nums[i+1], 则就可以肯定新的 i 是 peak element 了;
            elif nums[i] < nums[unvalid_idx]:
                unvalid_idx = i

        # jy: 以上 for 没有对最后一个元素进行处理, 此处补充最后一个元素的处理;
        if nums[len(nums)-1] > nums[len(nums)-2]:
            ls_peak_idx.append(len(nums)-1)

        return ls_peak_idx

    """
解法3: 使用二分查找求解, 如果 nums[middle] 小于 nums[middle+1], 则说明 nums[middle...n] 存在 peak, 如
果 nums[middle...n] 一直升序, 则 numz[n] 是 peak, 否则 nums[middle+1] 到 nums[n] 之间的某个数必然存
在 peak, 此时 low 移动到 middle+1; 反之, 则说明 nums[0...middle] 存在 peak, 如果 nums[0...middle] 一直
降序, 则 nums[0] 是 peak, 否则 nums[0] 到 nums[middle] 必然存在 peak;

jy: 由于题目中要求找出一个符合要求的即可, 该方式可以找出符合要求的值; 当要找出所有 peak element 时, 该
    方法的思路则不再合适;
    """
    def findPeakElement_v3(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            middle = low + (high - low) // 2
            if nums[middle] < nums[middle + 1]:
                low = middle + 1
            else:
                high = middle

        return low


nums = [1, 2, 3, 1]
# Output: 2
res = Solution().findPeakElement_v1(nums)
print(res)

nums = [1, 2, 1, 3, 5, 6, 4]
# Output: 5
res = Solution().findPeakElement_v2(nums)
print(res)


res = Solution().findPeakElement_v3(nums)
print(res)


