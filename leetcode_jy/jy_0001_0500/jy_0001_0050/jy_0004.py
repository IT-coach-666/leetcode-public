# jy: 以下的设置使得能正常在当前文件中基
#     于 leetcode_jy 包导入相应模块
import os
import sys
abs_path = os.path.abspath(__file__)
dir_project = os.path.join(abs_path.split("leetcode_jy")[0], "leetcode_jy")
sys.path.append(dir_project)
from leetcode_jy import *
from typing import List
# jy: 记录该题的难度系数
type_jy = "H"
# jy: 记录该题的英文简称以及所属类别
title_jy = "Median-of-Two-Sorted-Arrays(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "问题等价转换（求第 k 大的数）+ 递归/循环/双指针 | 中位数含义深刻理解 + 问题等价转换 + 二分查找"



"""
There are two sorted arrays ``nums1`` and ``nums2`` of size ``m`` and ``n``
respectively. Find the median of the two sorted arrays. 

The overall run time complexity should be O(log(m+n)). 

You may assume ``nums1`` and ``nums2`` cannot be both empty.


Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""


class Solution:
    """
解法1: 技巧性解法(实际应用中排序算法需自己实现), 时间复杂度为 O(m+n)
将两个数组合并后排序, 如果有序数组长度是奇数则返回新数组中间的元
素, 否则返回新数组中间的两个元素的均值
    """
    def findMedianSortedArrays_v1(self, 
                                  nums1: List[int], 
                                  nums2: List[int]) -> float:
        # jy: 求解中间元素的下标位置
        n = len(nums1) + len(nums2)
        middle = n // 2
        # jy: 将两个数组整合并排序
        sorted_list = sorted(nums1 + nums2)
        # jy: 如果有序数组长度是奇数, 则返回新数组中间的元素; 
        #     则返回新数组中间的两个元素的均值
        median = sorted_list[middle] if n % 2 == 1 else \
                (sorted_list[middle-1] + sorted_list[middle]) / 2
        return median


    """
解法2: 递归, 时间复杂度为 O(log(m+n))
假设两有序数组的长度分别为 m 和 n, 求中位数等价于求合并后数组的
第 (m+n+1) // 2 和第 (m+n+2) // 2 个元素的平均值, 继而将问题转化为
求第 k 大的问题（无论 m+n 上奇数还是偶数均是如此, 可自行举例思考）

在两个有序数组中求第 k 大的数时, 首先各自求第 k // 2 大的数, 如果 nums1
的第 k // 2 大的数比 nums2 的第 k // 2 大的数小, 说明两个数组的第 k 大
的数不可能在 nums1[0] 到 nums1[k // 2 - 1] 中 (因为即使 nums2 的第 
k//2 大的数之前的数都比 nums1 的第 k // 2 大的数小, nums1[0: k//2 - 1]
和 nums2[0: k//2 - 2] 加起来总共也只有 k//2 + k//2 - 1 = k-1 个数, 这
些数必然不会是两个数组第 k 大的数), 此时就可以过滤掉 nums1[0] 到 
nums1[k//2 - 1] 这 k // 2 个数, 然后在剩下的数组区间中递归查找第 k - k//2
大的数即可

注意: nums1 中第 k//2 大的数的下标为 k//2 - 1, 即 nums1[k // 2 - 1]

其它两种实现方法:
    基于循环实现（method_type="loop" 时对应的逻辑）; 逻辑类似递归(即对递归进行改写)
    基于双指针进行实现（method_type="bi-needle" 时对应的逻辑）
    """
    def findMedianSortedArrays_v2(self, 
                                  nums1: List[int], 
                                  nums2: List[int],
                                  method_type="recurse") -> float:
        """
        method_type="recurse":   基于递归的思路实现
        method_type="loop":      基于循环实现
        method_type="bi-needle": 基于双指针实现
        """
        assert method_type in ["recurse", "loop", "bi-needle"]
        # jy: 确定 k1 和 k2 (代表中间值属于第几个数, 非下标概念)
        total_num = len(nums1) + len(nums2)
        k1 = (total_num + 1) // 2
        #k2 = (total_num + 2) // 2
        # jy: total_num 为偶数时（此时 total_num & 1 为 0）, k2 会比 k1 大 1
        #     total_num 为基数时 k2 和 k1 的值相等
        k2 = k1 if total_num & 1 else k1 + 1

        # jy: 基于递归实现
        if method_type == "recurse":
            if k1 != k2:
                # jy: 其实 k1 与 k2 相等时也可以通过以下方式得到相同结果, 但
                #     这样产生了一次重复计算
                return (self._find_kth_recurse(nums1, 0, nums2, 0, k1) + 
                        self._find_kth_recurse(nums1, 0, nums2, 0, k2)) / 2
            return self._find_kth_recurse(nums1, 0, nums2, 0, k1)
        # jy: 基于循环实现
        else:
            fun_find_kth = self._find_kth_loop if method_type == "loop" \
                                               else self._find_kth_bineedle
            if k1 != k2:
                return (fun_find_kth(nums1, nums2, k1) +
                        fun_find_kth(nums1, nums2, k2)) / 2
            else:
                return fun_find_kth(nums1, nums2, k1)


    def _find_kth_recurse(self,
                  nums1: List[int], i: int, 
                  nums2: List[int], j: int, 
                  k: int) -> int:
        """
        找出两个有序数组 nums1[i:] 和 nums2[j:] 中的第 k 大数值

        递归实现; i, j, k 可变, 方便后续递归实现
        """
        # jy: 如果 nums1[i:] 已经没有有效数值, 则只能从 nums2[j: ] 中查找第
        #     k 大的值 (下标位置 j 算 1 个, 故第 k 个的下标位置为 j+k-1)
        if i >= len(nums1):
            return nums2[j+k-1]
            
        # jy: 如果 nums2[j:] 已经没有有效数值, 则只能从 nums1[i: ] 中查找第
        #     k 大的值 (下标位置 i 算 1 个, 故第 k 个的下标位置为 i+k-1)
        if j >= len(nums2):
            return nums1[i+k-1]
            
        # jy: 代码执行到此时, i 和 j 均为 nums1 和 nums2 的有效下标, 如果
        #     k 为 1, 则返回 nums1[i] 和 nums2[j] 的较小值即可
        if k == 1:
            return min(nums1[i], nums2[j])

        # jy: 求解有序数组 nums1[i:] 和 nums2[j:] 中求第 k 大的数时, 首先各
        #     自求第 k//2 大的数
        # jy: nums1[i:] 的第 k//2 大的数即为 nums1[i + k//2 - 1], 取数时需
        #     确保下标位置有效, 如果不存在, 则需取一个大的值, 确保数组左侧
        #     数据不被过滤掉
        middle_value1 = nums1[i + k//2 - 1] if i + k//2 - 1 < len(nums1) \
                                            else sys.maxsize
        # jy: nums2[j:] 的第 k//2 大的数即为 nums2[j + k//2 - 1], 取数时需
        #     确保下标位置有效
        middle_value2 = nums2[j + k//2 - 1] if j + k//2 - 1 < len(nums2) \
                                            else sys.maxsize
        # jy: 如果 nums1[i:] 中的第 k//2 大的数比 nums2[j:] 的第 k//2 大的
        #     数小, 说明两个数组的第 k 大的数不可能在 nums1[i] 到
        #     nums1[i + k//2 - 1] 中, 因此可以过滤掉这 k//2 个数, 然后在剩
        #     下的数组区间中递归查找第 k - k//2 大的数即可
        if middle_value1 < middle_value2:
            return self._find_kth_recurse(nums1, i + k//2, nums2, j, k - k//2)
        # jy: 如果 nums1[i:] 中的第 k//2 大的数比 nums2[j:] 的第 k//2 大的
        #     数大, 说明两个数组的第 k 大的数不可能在 nums2[j] 到
        #     nums2[j + k//2 - 1] 中, 因此可以过滤掉这 k//2 个数 (即从
        #     nums1[i:] 和 nums2[j + k//2: ] 中找第 k - k//2 大的数值)
        else:
            return self._find_kth_recurse(nums1, i, nums2, j + k//2, k - k//2)


    def _find_kth_loop(self, nums1, nums2, k):
        """
        找出有序数组 nums1 和 nums2 中的第 k 大的数

        基于循环实现(思路类似递归实现方式, 即对递归实现的改写)
        """
        m, n = len(nums1), len(nums2)
        idx_1, idx_2 = 0, 0
        # jy: while 循环中求解有序数组 nums1[idx_1: ] 和 nums2[idx_2: ] 中第
        #     k 大的数值; idx_1、idx_2、k 在循环过程中会不断更新变化
        while True:
            # jy: 如果 nums1 中的下标位置 idx_1 超出范围, 则第 k 大的数值直接
            #     从 nums2 中取
            if idx_1 == m:
                return nums2[idx_2 + k - 1]
            # jy: 如果 nums2 中的下标位置 idx_2 超出范围, 则第 k 大的数值直接
            #     从 nums1 中取
            if idx_2 == n:
                return nums1[idx_1 + k - 1]

            # jy: 执行到此处, nums1 和 nums2 对应的位置下标 idx_1 和 idx_2 均
            #     有效, 此时如果 k 为 1, 则直接返回 nums1[idx_1] 和
            #     nums2[idx_2] 中的较小值
            if k == 1:
                return min(nums1[idx_1], nums2[idx_2])

            # jy: 尝试将 nums1[idx_1: ] 向前移动 k//2 位, 对应的下标为
            #     idx_1 + k//2 - 1 (如果该位置下标越界, 则最多只推进到最
            #     后一个下标位置 m-1)
            new_idx_1 = min(idx_1 + k // 2 - 1, m-1)
            # jy: 尝试将 nums2[idx_2: ] 向前移动 k//2 位, 对应的下标为
            #     idx_2 + k//2 - 1 (如果该位置下标越界, 则最多只推进到
            #     最后一个下标位置 n-1)
            new_idx_2 = min(idx_2 + k // 2 - 1, n-1)
            # jy: 如果 nums1 移动下标位置后对应值小于或等于 nums2 推进后
            #     的下标位置对应值, 则第 k 大的值不可能在 nums1[new_idx_1]
            #     之前, 因此可以过滤掉下标为 idx_1 至 new_idx_1 的数, 即
            #     从 new_idx_1 + 1 位置开始, k 也相应地减去过滤掉的个数
            if nums1[new_idx_1] <= nums2[new_idx_2]:
                k -= new_idx_1 - idx_1 + 1
                idx_1 = new_idx_1 + 1
            # jy: 反之同理
            else:
                k -= new_idx_2 - idx_2 + 1
                idx_2 = new_idx_2 + 1

    def _find_kth_bineedle(self,
                           nums1: List[int],
                           nums2: List[int],
                           k: int) -> int:
        """
        从两个有序数组中找第 k 大的数, 时间复杂度: O(m+n)

        双指针法实现: i 和 j 分别指向 nums1 和 nums2 的初始位置, 不断逐一遍
        历较小值, 直到找到第 k 大值
        """
        # jy: i 和 j 分别指向 nums1 和 nums2 的初始位置
        i, j = 0, 0
        # jy: 记录已遍历的个数
        k_th = 0
        # jy: 不断逐一遍历较小值, 直到找到第 k 大值
        while i < len(nums1) and j < len(nums2):
            k_th += 1
            if nums1[i] > nums2[j]:
                if k_th == k:
                    return nums2[j]
                j += 1
            else:
                if k_th == k:
                    return nums1[i]
                i += 1

        # jy: 经过以上遍历后, 以下两个 while 循环仅有一个会被执行
        while i < len(nums1):
            k_th += 1
            if k_th == k:
                return nums1[i]
            i += 1

        while j < len(nums2):
            k_th += 1
            if k_th == k:
                return nums2[j]
            j += 1


    """
解法3: 基于对中位数的含义的深刻理解, 时间复杂度: O(log min(m, n))
在统计中, 中位数被用来将一个集合划分为两个长度相等的子集, 其中一个子
集中的元素总是大于另一个子集中的元素

假设 nums1 和 nums2 中元素个数分别为 m 和 n, 且 m <= n 
(当 m > n 时, 调换 nums1 和 nums2 即可)


1）划分两有序数组 ---------------------------------
在任一下标位置 i 将 nums1 划分为 left_nums1 和 right_nums1 两部分:
  a) len(left_nums1) 为 i (下标为 i 的元素不包含在 left_nums1)
  b) len(right_nums1) 为 m-i (下标为 i 的元素包含在 right_nums1) 
i 的范围为 [0, m], 有 m+1 种分法:
  a) 当 i 为 0 时, left_nums1 为空集
  b) 当 i 为 m 时, right_nums1 为空集

同理将 nums2 进行划分为 left_nums2 和 right_nums2
j 的范围为 [0, n], 有 n+1 种分法:
  a) 当 j 为 0 时, left_nums2 为空集
  b) 当 j 为 n 时, right_nums2 为空集
len(left_nums2) 为 j, len(right_nums2) 为 n-j

left_nums1 和 left_nums2 归为 left_part
right_nums1 和 right_nums2 归为 right_part 

注意: i 和 j 代表左侧部分元素的个数


2) m+n 的奇偶性 ----------------------------------
当 m+n 为偶数时, 如果确保以下两个条件均成立:
    a) nums1 和 nums2 中的所有元素被分为相同长度的两部分 (i+j = m−i + n−j):
       len(left_part) = len(right_part)
    b) 左侧部分的最大值 <= 右侧部分的最小值: 
       max(left_part) <= min(right_part)
则中位数为: [max(left_part) + min(right_part)] // 2

当 m+n 为奇数时, 如果确保以下两个条件均成立:
    a) 左侧部分比右侧部分多一个元素 (i+j = m−i + n−j + 1):
       len(left_part) = len(right_part) + 1
    b) 左侧部分的最大值 <= 右侧部分的最小值:
       max(left_part) <= min(right_part)
则中位数为: max(left_part)


3）条件转换表示 ------------------------------------
不管 m+n 为偶数还是奇数, 条件 a) 均可转换为 (将 i 和 j 全部移到等号左侧):
    i+j = (m+n+1) // 2  
解析: m+n 为奇数时可以直接这么表示; m+n 为偶数时, 由于 // 代表整除, 且
      m+n 本来就是偶数, 多加 1 也不影响整除的结果

因此 j 可以转换为: 
    j = (m+n+1) // 2 - i
由于 m < n, 且 i 取值范围为 [0, m], 因此必有 j > 0


以上两种情况下的条件 b): nums1 和 nums2 中左侧部分的最大值 <= 右侧部分的最小值
该条件可转换为:
    nums1[i−1] <= nums2[j] 且 nums2[j−1] <= nums1[i]
即:
    max(nums1[i−1], nums2[j−1]) <= min(nums1[i], nums2[j])


因此, 该问题转换为: 在 [0, m] 中找到满足如下条件的 i (二分查找):
    a) max(nums1[i−1], nums2[j−1]) <= min(nums1[i], nums2[j])
    b) j = (m+n+1) // 2 - i
由此可知当 i 确定后即可确定 j; 而目标是寻找 median 值, 因此要使得左半侧的最大
值要小于右半侧的最小值, 并不是随随便便确定 i (相应的 j 也因此确定) 都可以满足
该条件, 当满足该条件时, i 即为 nums1 的目标分割位置 (相应求得的 j 即为 nums2
的目标分割位置)
       
以上问题可进一步转换为: 在 [0, m] 中找到最大的 i (可基于二分查找), 使得:
    a) nums1[i−1] <= nums2[j]
    b) j = (m+n+1) // 2 - i
解析: 
    1) 当 i 从 0 到 m 递增时, nums1[i−1] 递增, nums2[j] 递减 (因为 j 递减),
       所以一定存在一个最大的 i 满足 nums1[i−1] <= nums2[j]
    2) 如果 i 是最大的满足以上条件的值, 则 i+1 不再满足, 将 i+1 代入有:
       nums1[i] > nums2[j−1]
       即满足以上等价变换中的 nums2[j−1] <= nums1[i] (此处取不到 "=", 效果更强)
注意: 是需要找到最大的 i 满足以上条件, 才符合题意, 如果不是最大的 i, 尽管满足
以上条件 a), 也可能因为不满足 nums2[j−1] <= nums1[i] 而不满足题目要求 

     
求解过程中假设 nums1[i−1], nums2[j−1], nums1[i], nums2[j] 均可取到有效值: 
a) 当 i=0 或 j=0 时（i 和 j 不可能同时为 0）对应的左侧部分包含 nums1[−1] 或
   nums2[−1] 已经产生逻辑上的越界, 由于左侧部分是要取最大值, 因此将 nums1[−1]
   和 nums2[−1] 设置为负极大值后就不会影响所取的最大值结果
b) 当 i=m 或 j=n 时（两个状态不可能同时成立）对应的右侧部分包含 nums1[m] 或
   nums2[n], 此时已经越界, 由于右侧部分是要取最小值, 因此将这两个边界值设置
   为极大值后就不会影响所取的最小值的结果
    """
    def findMedianSortedArrays_v3(self,
                                  nums1: List[int],
                                  nums2: List[int]) -> float:
        # jy: 确保调用时 nums1 元素个数小于 nums2 的元素个数
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays_v3(nums2, nums1)

        # jy: nums1 的元素个数必定小于或等于 nums2 的元素个数, 即 m <= n
        infinty = sys.maxsize
        m, n = len(nums1), len(nums2)
        # jy: 二分查找的首末下标位置 (边界情况会在 while 循环中的 if 判断
        #     中进行处理)
        low, high = 0, m
        # jy: 记录左侧部分的最大值和右侧部分的最小值 (最终需要基于这两个值
        #     算 median 值)
        left_max, right_min = 0, 0

        # jy: 二分查找: 在 [0, m] 中找到最大的 i, 使得 nums1[i−1] <= nums2[j]
        while low <= high:
            # jy: nums1 基于 i 进行分割, 左侧为 nums1[0: i], 右侧为 nums1[i: m]
            i = (low + high) // 2
            # jy: 基于 i 计算求得 nums2 的分割位置 j, 分割后, 左侧为: 
            #     nums2[0: j], 右侧为: nums2[j: n]
            j = (m + n + 1) // 2 - i

            # jy: nums_im1, nums_jm1 分别表示 nums1[i-1], nums2[j-1], 两者中的
            #     最大值即为左侧部分 (即 nums1[0: i] 和 nums2[0: j]) 的最大值;
            #     由于左侧部分是需要取最大值, 因此越界时的值赋予一个极小值, 确
            #     保对后续取最大值不受影响
            nums_im1 = nums1[i-1] if i != 0 else - infinty
            nums_jm1 = nums2[j-1] if j != 0 else - infinty
            # jy: nums_i, nums_j 分别表示 nums1[i], nums2[j], 两者中的最小值即
            #     为右侧部分 (即 nums1[i: m] 和 nums2[j: n]) 的最小值; 
            #     由于右侧部分是需要取最小值, 因此越界时的值赋予一个极大值, 确
            #     保对后续取最小值不受影响
            nums_i = nums1[i] if i != m else infinty
            nums_j = nums2[j] if j != n else infinty

            # jy: 如果 nums_im1 小于等于 nums_j (即 nums1[i−1] <= nums2[j]), 此
            #     时还不能确保 nums_jm1 小于等于 nums_i (即 nums2[j−1] <= nums1[i])
            #     当且仅当是找到最大的 i 满足 nums1[i−1] <= nums2[j] 时才能确保;
            #     因此需收缩 i 的查找范围继续二分查找(每次二分查找时 i 其实是该
            #     查找范围的中间值)
            #     当 i 不断增至最大且仍满足 nums1[i−1] <= nums2[j] 时, 开始出现
            #     临界状态, 使得此时也满足 nums2[j−1] <= nums1[i], 当 i 再大时又
            #     得不到满足 (参考解析 "3)" 中的 "1)" 和 "2)" 中的推理说明)
            if nums_im1 <= nums_j:
                # jy: 收缩查找范围
                low = i + 1
                # jy: 更新左侧部分的最大值和右侧部分的最大值 (其实循环过程的
                #     前期获取到的这两个值通常不满足 left_max <= right_min,
                #     只有在最后退出循环时获取到的这两个值才满足; 但又不太方
                #     便将这两个值的提取放置到循环外面, 因此最终退出循环时对
                #     应的 nums_im1 可能是大于 nums_j 的了, 不满足要求
                left_max, right_min = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                # jy: 查看确认 (循环前期输出的通常为 False)
                print(left_max <= right_min)
            else:
                high = i - 1

        return (left_max + right_min) / 2 if (m + n) % 2 == 0 else left_max



nums1 = [1, 3]
nums2 = [2]
res = Solution().findMedianSortedArrays_v1(nums1, nums2)
print(res)


nums1 = [1, 2]
nums2 = [3, 4]
print("递归实现:")
res = Solution().findMedianSortedArrays_v2(nums1, nums2)
print(res)
print("循环实现:")
res = Solution().findMedianSortedArrays_v2(nums1, nums2, method_type="loop")
print(res)
print("双指针实现:")
res = Solution().findMedianSortedArrays_v2(nums1, nums2, method_type="bi-needle")
print(res)

nums1 = [3, 5]
nums2 = [2, 10, 18, 99, 100, 10000]
res = Solution().findMedianSortedArrays_v3(nums1, nums2)
print(res)



