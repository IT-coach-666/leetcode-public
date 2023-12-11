
"""
归并排序; 比较重要的一种排序算法, 实际应用中比较多, python 对象中的排序也是用归
并排序(对象排序一般要求稳定)

时间复杂度: O(n * log(n)),
空间复杂度: O(n)

JY: 相关应用: 待整理
"""


from typing import List
from verify_sort_algorithm import *


"""
解法1: 合并过程中不返回数组, 直接在原数组基础上进行更新;
"""
def merge_sort_v1(nums: List[int]) -> List[int]:
    _merge_sort(nums, 0, len(nums) - 1)
    return nums


def _merge_sort(nums, low, high):
    # jy: 如果 low 大于或等于 high, 则终止递归;
    if low >= high:
        return
    # jy: 将数组分为两部分;
    middle = low + (high - low) // 2
    # jy: 先对数组的前半部分(下标为 low 到 middle)进行排序;
    _merge_sort(nums, low, middle)
    # jy: 再对数组的后半部分(下标为 middle+1 到 high)进行排序;
    _merge_sort(nums, middle + 1, high)
    # jy: 再对整个数组进行排序(数组的 low 到 middle, 以及 middle+1 到 high 已经有序)
    _merge(nums, low, middle, high)


def _merge(nums, low, middle, high):
    # jy: 由于数组的 low 到 middle 部分已经有序, middle+1 到 high 也已经有序,
    #     如果 middle 小于 middle+1, 表明数组已经整体有序, 无需再次排序;
    if nums[middle] <= nums[middle + 1]:
        return
    # jy: 记录左半部分有序数组的起始位置;
    left = low
    # jy: 记录右半部分有序数组的起始位置;
    right = middle + 1
    # jy: 一个临时数组, 用于存放左半部分和右半部分有序数组排序后的结果;
    merged = []

    while left <= middle or right <= high:
        if left <= middle and right <= high:
            # jy: 注意, 当 nums[left] 值等于 nums[right] 时进行也优先将 nums[left] 加入
            #     已有序的数组中, 这样才能确保算法是稳定的;
            if nums[left] <= nums[right]:
                merged.append(nums[left])
                left += 1
            else:
                merged.append(nums[right])
                right += 1
        elif left <= middle:
            merged.append(nums[left])
            left += 1
        else:
            merged.append(nums[right])
            right += 1

    # jy: 将对 nums 的 low 到 high 部分进行排序后的结果(暂存于 merged 临时数组中, 起始
    #     下标总是为 0)更新到 nums 中(更新的部分的 nums 的起始下标为 low);
    for i in range(low, high + 1):
        nums[i] = merged[i - low]


"""
解法2: 每次局部合并后返回已排序的数组, 然后对已排序的数组进行合并;
LeetCode (912) 上运行结果表明时间和空间复杂度均差于解法 1;
"""
def merge_sort_v2(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    middle = len(nums) // 2
    left = merge_sort_v2(nums[: middle])
    # jy: 再对数组的后半部分(下标为 middle+1 到 high)进行拍戏;
    right = merge_sort_v2(nums[middle:])
    # jy: 再对整个数组进行排序(数组的 low 到 middle, 以及 middle+1 到 high 已经有序)
    return _merge_v2(left, right)


def _merge_v2(left, right):
    # jy: left 和 right 数组已经有序;
    if not left or not right:
        return left or right

    i = 0
    j = 0
    tmp_sorted = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            tmp_sorted.append(left[i])
            i += 1
        else:
            tmp_sorted.append(right[j])
            j += 1

    while i < len(left):
        tmp_sorted.append(left[i])
        i += 1
    while j < len(right):
        tmp_sorted.append(right[j])
        j += 1

    return tmp_sorted


nums = [5, 2, 3, 1]
# Output: [1,2,3,5]
res = merge_sort_v1(nums)
print(res)


nums = [5, 2, 3, 1]
# Output: [1,2,3,5]
res = merge_sort_v2(nums)
print(res)

print(is_sort_algorithm_correct(1000, merge_sort_v1))
print(is_sort_algorithm_correct(1000, merge_sort_v2))
