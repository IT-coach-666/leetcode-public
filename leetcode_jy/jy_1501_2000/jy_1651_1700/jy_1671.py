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
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Minimum-Number-of-Removals-to-Make-Mountain-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You may recall that an array arr is a mountain array if and only if:
1) arr.length >= 3
2) There exists some index i(0-indexed) with 0 < i < arr.length - 1 such that:
3) arr[0] < arr[1] < ... < arr[i-1] < arr[i]
4) arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Given an integer array ``nums``, return the minimum number of elements to remove to
make ``nums`` a mountain array.


Example 1:
Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.

Example 2:
Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].

Example 3:
Input: nums = [4,3,2,1,1,2,3,1]
Output: 4

Example 4:
Input: nums = [1,2,3,4,4,3,2,1]
Output: 1



Constraints:
3 <= nums.length <= 1000
1 <= nums[i] <= 10^9
It is guaranteed that you can make a mountain array out of nums.
"""


from typing import List
import bisect

class Solution:
    """
一座山由上坡和下坡组成, 寻找上坡的过程等同于 300_Longest-Increasing-Subsequence.py, 记:
longest_increasing_sequence[i] 记录以 nums[i] 结尾的最大增序子序列的长度(允许间断);
longest_mountain[i] 记录以 nums[i] 为结尾(即 nums[i] 是山右侧的最后一个值)的最长的山的长度;

两层循环遍历数组更新 longest_increasing_sequence 和 longest_mountain (其中 i > j):
1) 如果 nums[j] < nums[i], 表明以 nums[i] 结尾的最长增长序列必定大于 1, 更新 longest_increasing_sequence[i]
2) 如果 nums[j] > nums[i], 表明以 nums[i] 结尾可能可以构成一座山, 需进一步判断:
   a) 如果 longest_increasing_sequence[j] > 1, 说明以 nums[j] 结尾存在不仅包含自己的升序子序
      列(即最长升序子序列的长度至少是 2; 因为如果是 1, 则表明只包含当前元素 nums[j], 而当前元
      素是需要当做山顶的, 故仅包含当前元素是不能满足条件的), 而 nums[j] > nums[i], 说明 nums[j]
      是山顶, 且以 nums[i] 结尾可以组成一座山, 更新 longest_mountain[i]
   b) 如果 longest_mountain[j] > 1 , 说明以 nums[j] 结尾可以组成一座山, 而 nums[j] > nums[i], 说
      明这座山可以延续到 nums[i], 更新 longest_mountain[i]
3) 如果 nums[i] == nums[j], 则忽略跳过(此处没有该条件成立下的代码逻辑), 因为一座山的两侧均不会包含有相等的数值;

最后返回 length - max(longest_mountain) 就是需要移除的数字的个数;

JY: 算法复杂度较高, 待寻找更优解;
    """
    def minimumMountainRemovals_v1(self, nums: List[int]) -> int:
        length = len(nums)
        # jy: longest_increasing_sequence[i] 记录以 nums[i] 结尾的最大升序子序列的长度(允许间断);
        #    初始化值均为 1(以 nums[i] 结尾的升序子序列至少有当前 1 个元素);
        longest_increasing_sequence = [1] * length
        # jy: 以
        longest_mountain = [1] * length
        # jy: 从数组的第二位开始遍历, 求出 longest_increasing_sequence[i] 和 longest_mountain[i]
        #    以 [2, 4, 3] 为例进行思考;
        for i in range(1, length):
            # jy:【需结合具体实例强化理解以下更新逻辑】
            for j in range(i):
                # jy: 1) 如果 nums[i] > nums[j], 表明以 nums[i] 结尾的最长升序子序列的长度 (即
                #       longest_increasing_sequence[i]) 至少是以 nums[j] 结尾的最长升序子序列
                #       长度 (即 longest_increasing_sequence[j]) 加 1;
                if nums[j] < nums[i]:
                    longest_increasing_sequence[i] = max(longest_increasing_sequence[i], 1 + longest_increasing_sequence[j])
                # jy: 2) 如果 nums[i] < nums[j], 表明以 nums[i] 结尾可能可以构成一座山, 需进一步判断:
                #       a) 如果 longest_increasing_sequence[j] > 1, 说明以 nums[j] 结尾存在不仅包含
                #          自己的升序子序列(即最长升序子序列的长度至少是 2; 因为如果是 1, 则表明只包
                #          含当前元素 nums[j], 而当前元素是需要当做山顶的, 故仅包含当前元素是不能满足
                #          条件的), 而 nums[j] > nums[i], 说明 nums[j] 是山顶, 且以 nums[i] 结尾可以组
                #          成一座山, 更新 longest_mountain[i]
                #       b) 如果 longest_mountain[j] > 1 , 说明以 nums[j] 结尾可以组成一座山, 而
                #          nums[j] > nums[i], 说明这座山可以延续到 nums[i], 更新 longest_mountain[i]
                #    3) 如果 nums[i] == nums[j], 则忽略跳过(此处没有该条件成立下的代码逻辑), 因为一座
                #       山的两侧均不会包含有相等的数值;
                elif nums[j] > nums[i]:
                # if nums[j] > nums[i]:
                    if longest_increasing_sequence[j] > 1:
                        longest_mountain[i] = max(longest_mountain[i], 1 + longest_increasing_sequence[j])

                    if longest_mountain[j] > 1:
                        longest_mountain[i] = max(longest_mountain[i], 1 + longest_mountain[j])
        # jy: 数组长度减去最长 mountain 的长度, 即为需要删除的最少个数;
        return length - max(longest_mountain)


    def minimumMountainRemovals_v2(self, nums: List[int]) -> int:

        def get_len_longestsubseq_of_arr_i(arr):
            """
            返回一个数组 res, res[i] 记录从 arr[0] 到 arr[i] 中以 arr[i] 结尾的子数组中的最长升
            序子序列的长度;
            """
            ls_tmp = []
            res = []
            # jy: 遍历数组, 找出数组中的值插入到 ls_tmp 中的位置(保证插入后有序, 如果有相同值, 尽
            #    可能插入到左侧);
            for i, val in enumerate(arr):
                idx = bisect.bisect_left(ls_tmp, val)
                # jy: 如果插入位置 idx 上有数值(即对应的下标对于原 ls_tmp 来说是有效下标), 则将该
                #    位置上的数值进行更新, 并在 res 列表中加入该插入位置的坐标加 1, 表示以当前位
                #    置 i 对应的值结尾的前面序列中的最长升序子序列(注意一定要是以当前值结尾)
                if idx < len(ls_tmp):
                    ls_tmp[idx] = val
                    res.append(idx + 1)
                else:
                    ls_tmp.append(val)
                    res.append(len(ls_tmp))
            # print(ls_tmp)
            return res

        # jy: arr1[i] 记录 nums[0] 到 nums[i] 中, 以 nums[i] 结尾的最长升序子数组的长度;
        arr1 = get_len_longestsubseq_of_arr_i(nums)
        # jy: 对 nums 进行反转后求 nums[i] 结尾的最长升序子数组的长度, 用 arr2[i] 记录; 则
        #    反转 arr2 后对应的新 arr2[i] 表示以 nums[i] 开头至数组结尾中最长降序子数组的
        #    长度;
        arr2 = get_len_longestsubseq_of_arr_i(nums[::-1])
        # print(arr1, " ==== ", arr2)
        # print(arr1)


        max_val = 0
        n = len(nums)

        # jy: version-1 ---------------------------------------------------
        # for i in range(1, n-1):
        #     if arr1[i] > 1 and arr2[n-i-1] > 1:
        #         max_val = max(max_val, arr1[i] + arr2[n-i-1] - 1)

        # jy: version-2 ---------------------------------------------------
        # jy: 反转 arr2 后对应的新 arr2[i] 表示以 nums[i] 开头至数组结尾中最长降序子数组的
        #    长度;
        arr2.reverse()
        # print("arr1 =======================:", arr1)
        # print("arr2 =======================:", arr2)
        for i in range(1, n-1):
            # jy: 1) 如果以 nums[i] 结尾的数组中, 最长升序子序列的长度(即 arr1[i])大于 1, 表明
            #       nums[i] 之前有比其小的元素;
            #    2) 如果以 nums[i] 开头至结尾的数组中, 最长降序子序列的长度(即 arr2[i])大于 1,
            #       表明 nums[i] 之后存在比其小的元素;
            #    以上条件均满足的情况下, 表明 nums[i] 可作为一座山顶构成一座山, 该山的最长跨度
            #    为 arr1[i] + arr2[i] -1 (因为 nums[i] 被重复算了一次, 故需要减 1)
            if arr1[i] > 1 and arr2[i] > 1:
                max_val = max(max_val, arr1[i] + arr2[i] - 1)

        return n - max_val

    """
解法3: 同理解法 2;
    """
    def minimumMountainRemovals_v3(self, nums: List[int]) -> int:

        def get_len_longestsubseq_of_arr_i(seq):
            """
            返回一个数组 res, res[i] 记录从 arr[0] 到 arr[i] 中以 arr[i] 结尾的子数组中 arr[i] 之前
            的最长升序子序列的长度(即以 arr[i] 结尾, 但计算最长升序子数组长度时 arr[i] 不计算在内);
            该方式返回的 res 中第一个元素 res[0] 必定是 0;
            """
            tmp = []
            res = []
            for L in seq:
                p = bisect.bisect_left(tmp, L)
                res.append(p)
                if p == len(tmp):
                    tmp.append(L)
                else:
                    tmp[p] = L
            return res
        # jy: inc[i] 记录 nums[0] 到 nums[i] 中, 以 nums[i] 结尾的子数组中 nums[i] 之前的最长升序子数
        #    组的长度(即以 nums[i] 结尾, 但计算最长升序子数组长度时 nums[i] 不计算在内); 该方式
        inc = get_len_longestsubseq_of_arr_i(nums)
        # print("inc ============ ", inc)
        # jy: 对 nums 进行反转后求 nums[i] 结尾的最长升序子数组的长度(计算长度时不将 nums[i] 包括在内),
        #    用 dec[i] 记录; 则反转 dec 后对应的新 dec[i] 表示以 nums[i] 开头至数组结尾中最长降序子数
        #    组的长度(计算长度时不将 nums[i] 包括在内);
        dec = get_len_longestsubseq_of_arr_i(reversed(nums))
        dec.reverse()
        # print("dec ============ ", dec)
        # jy: 如果以 nums[i] 结尾的最长升序子序列中, nums[i] 之前还有比其小的值(即 inc[i] 大于 0), 且
        #    以 nums[i] 开头到数组末尾的最长降序子序列中, nums[i] 之后还有比其小的值(即 dec[i] 大于 0),
        #    表明 nums[i] 可以作为山顶构成山, 山的最长跨度为 inc[i] + dec[i] + 1 (因为 nums[i] 作为山
        #    顶不包含在 inc[i] 和 dec[i] 中, 故需要额外补充加 1)
        return len(nums) - (max(inc[i] + dec[i] for i in range(len(inc)) if inc[i] > 0 and dec[i] > 0) + 1)
        # return len(nums) - (max(i + j for i, j in zip(inc, dec) if i > 0 and j > 0) + 1)
        # return len(nums) - (max(i + j for i, j in zip(inc[1:-1], dec[1:-1]) if i > 0 and j > 0) + 1)

nums = [1, 3, 1]
# Output: 0
res = Solution().minimumMountainRemovals_v1(nums)
print(res)


nums = [2, 1, 1, 5, 6, 2, 3, 1]
# Output: 3
res = Solution().minimumMountainRemovals_v1(nums)
print(res)


nums = [4, 3, 2, 1, 1, 2, 3, 1]
# Output: 4
res = Solution().minimumMountainRemovals_v2(nums)
print(res)


nums = [1, 2, 3, 4, 4, 3, 2, 1]
# Output: 1
res = Solution().minimumMountainRemovals_v3(nums)
print(res)


