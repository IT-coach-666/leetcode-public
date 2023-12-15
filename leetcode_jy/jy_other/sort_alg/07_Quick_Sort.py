
"""
快速排序:  代码容易出 bug, 排查较困难
"""


from typing import List
from verify_sort_algorithm import *


def quick_sort_v1(nums: List[int]) -> List[int]:
    _quick_sort_v1(nums, 0, len(nums) - 1)
    return nums

def _quick_sort_v1(nums, low, high):
    # jy: 如果 low 大于或等于 high, 则返回, 终止递归;
    if low >= high:
        return
    # jy: 先将数组的 low 和 high 分成两部分, low 到 pivot-1 (注意不是 low 到 pivot; 只能确保
    #     是 low 到 pivot-1 对应的元素是最终有序时这几个元素所处的位置, 其不可能经过排序后会
    #     被安排到 pivot 到 high 之间); 同理 pivot 到 high 对应的元素是最终排序后这几个元素所
    #     在的位置, 其不可能会在是 low 到 pivot-1 之间; 对这两部分进行排序即为最终有序数组(注
    #     意这两部分并非局部有序, 还需要进一步排序)
    pivot = _partition_v1(nums, low, high)
    # print(pivot, " === ", nums)

    _quick_sort_v1(nums, low, pivot - 1)
    _quick_sort_v1(nums, pivot, high)


def _partition_v1(nums, low, high):
    """
    以 nums 列表的某个位置的值为 pivot (此处以 low 与 high 的中间位置 middle 为 pivot), 将小于
    等于 pivot 的值放置到 pivot 的左边, 大于 pivot 的值放置到 pivot 的右边, 并最终返回 pivot 的位置
    下标;

    JY: 该方式代码逻辑不好理解, 待重新整理, 依旧基于 middle 值作为 pivot, 目标: 实现把小于等于 pivot
    放到其左边, 大于 pivot 的放到右边, 并返回 pivot 下标;
    """
    middle = low + (high - low) // 2
    pivot = nums[middle]
    # jy: 注意, 此处的条件不能仅仅是 low < high;
    # while low < high:
    while low <= high:
        # jy: 如果 nums[low] 小于 pivot, 则 low 不断进 1, 直到 nums[low] 大于等于 pivot 为止;
        while nums[low] < pivot:
            low += 1
        # jy: 如果 nums[high] 大于 pivot, 则 high 不断左移一位, 直到 nums[high] 小于等于 pivot 为止;
        while nums[high] > pivot:
            high -= 1
        # jy: 如果 low 小于等于 high
        if low <= high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
    # print(low, " ===== ", nums)
    return low


def quick_sort_v2(nums: List[int]) -> List[int]:
    # nums = [7, 3, 2, 8, 1, 9, 5, 4, 6]
    # nums = [0, 7, 3, 2, 8, 1, 9, 5, 4, 6, 0]
    nums = [7, 3, 2, 6, 8, 1, 9, 5, 4, 10]
    # nums = [4, 6]
    _quick_sort_v2(nums, 0, len(nums) - 1)
    print(nums)
    return nums


def _quick_sort_v2(nums, low, high):
    if low >= high:
        return
    # jy: pivot_idx 位置(其对应的值记为 pivot)的左边均是小于或等于 pivot 的, 右边均是
    #    大于 pivot 的值;
    pivot_idx = _partition_v2(nums, low, high)
    _quick_sort_v2(nums, low, pivot_idx - 1)
    _quick_sort_v2(nums, pivot_idx + 1, high)

def _partition_v2(nums, low, high):
    """
    以 nums 列表的某个位置的值为 pivot (此处以 high 为 pivot), 将小于等于 pivot 的值
    放置到 pivot 的左边, 大于 pivot 的值放置到 pivot 的右边, 并最终返回 pivot 的位置
    下标;
    """
    pivot_idx = high
    high -= 1
    # jy: 为了避免 nums = [4, 6] 的情况下输出结果为 [6, 4], 需要将 while 循环的判断逻辑修改
    #    为 low <= high; 否则如果还是 low < high, 则 nums = [4, 6] 的情况下, 以最后一个数为
    #    pivot 之后, low == high == 0, 此时不会进入 while 循环, 最后还对 low 和 pivot 进行
    #    交换, 导致了非预期结果
    while low <= high:
    # while low < high:
        #jy: 以 nums = [7, 3, 2, 8, 1, 9, 5, 4, 6, 10] 为例进行说明:
        #    1) 为了防止该情况下 low 值不断更新越界问题, 应补充逻辑 (low < high), 否则
        #       该情况下 low 会更新到 10, 越界;
        #    2) 在补充 low < high 逻辑后, 需进一步补充 low == high 的情况, 即补充逻辑应
        #       更新为 low <= high, 否则仅仅是 low < high 时, 结果会是(即 low 的最终值会
        #       更新为倒数第二个数值的下标(即没经过更新的 high 值), 此时 low 和 pivot_idx
        #       发生了交换导致的; 但 low 等于 high 的情况下, 如果 nums[low] <= nums[pivot_idx]
        #       时, 是不需要交换两个元素的; 在此处加上 low <= high 即可避免, 使得最终的 low
        #       会更新为 high+1, 即 pivot_idx, 使得其自身交换自身):
        #       [7, 3, 2, 8, 1, 9, 5, 4, 10, 6]
        while low <= high and nums[low] <= nums[pivot_idx]:
        # while nums[low] <= nums[pivot_idx]:
            low += 1
            # print("low=== ", low)
        #jy: 1) 为了防止 nums = [7, 3, 2, 8, 1, 9, 5, 4, 6, 0] 的情况下 high 值不断更新
        #       越界问题, 应补充逻辑 (low < high), 否则该情况下 high 会更新到 -11, 越界;
        #    2) 为了防止 nums = [7, 3, 2, 6, 8, 1, 9, 5, 4, 6, 10, 6] 情况下输出如下(即
        #       与 pivot_idx 交换后的 6 的右边仍有等于 6 的情况):
        #       [4, 3, 2, 6, 5, 1, 6, 8, 7, 6, 10, 9]
        #       需将 nums[high] >= nums[pivot_idx] 修改为 nums[high] > nums[pivot_idx], 即
        #       high 位置的值等于 pivot_idx 位置的值时也需要与目标 low 位置交换, 确保相等的
        #       值也都会被置于左侧;
        #    3) nums = [7, 3, 2, 6, 8, 1, 9, 5, 4, 10] 时, 如果条件是 low < high, 则会死循环;
        while low <= high and nums[high] > nums[pivot_idx]:
        # while low < high and nums[high] >= nums[pivot_idx]:
        # while nums[high] >= nums[pivot_idx]:
            high -= 1
            # print("high== ", high)

        if low < high:
            nums[low], nums[high] = nums[high], nums[low]

    nums[low], nums[pivot_idx] = nums[pivot_idx], nums[low]
    return low



def quick_sort_jy(nums: List[int]) -> List[int]:
    _quick_sort_jy(nums, 0, len(nums) - 1)
    return nums

def _quick_sort_jy(nums, low, high):
    #jy: 如果 low 大于或等于 high, 则返回, 终止递归;
    if low >= high:
        return

    # pivot = _partition_jy(nums, low, high)
    pivot = _partition_jy_low(nums, low, high)    #【undo】
    # print(pivot, "pivot === nums", nums)

    _quick_sort_jy(nums, low, pivot - 1)
    _quick_sort_jy(nums, pivot + 1, high)


def _partition_jy(nums, low, high):
    """
    基于 middle 值作为 pivot, 目标: 实现把小于等于 pivot 放到其左边, 大于 pivot 的放到右边, 并返回 pivot 下标;
    """
    #jy: 以中间数值作为 pivot, 先将中间数值与 high 位置替换, 即变成以 high 对应的数值为 pivot, 同理解法 2;
    middle = low + (high - low) // 2
    nums[middle], nums[high] = nums[high], nums[middle]
    pivot_idx = high
    high -= 1
    # jy: 为了避免 nums = [4, 6] 的情况下输出结果为 [6, 4], 需要将 while 循环的判断逻辑修改
    #    为 low <= high; 否则如果还是 low < high, 则 nums = [4, 6] 的情况下, 以最后一个数为
    #    pivot 之后, low == high == 0, 此时不会进入 while 循环, 最后还对 low 和 pivot 进行
    #    交换, 导致了非预期结果
    while low <= high:
        # while low < high:
        # jy: 以 nums = [7, 3, 2, 8, 1, 9, 5, 4, 6, 10] 为例进行说明:
        #    1) 为了防止该情况下 low 值不断更新越界问题, 应补充逻辑 (low < high), 否则
        #       该情况下 low 会更新到 10, 越界;
        #    2) 在补充 low < high 逻辑后, 需进一步补充 low == high 的情况, 即补充逻辑应
        #       更新为 low <= high, 否则仅仅是 low < high 时, 结果会是(即 low 的最终值会
        #       更新为倒数第二个数值的下标(即没经过更新的 high 值), 此时 low 和 pivot_idx
        #       发生了交换导致的; 但 low 等于 high 的情况下, 如果 nums[low] <= nums[pivot_idx]
        #       时, 是不需要交换两个元素的; 在此处加上 low <= high 即可避免, 使得最终的 low
        #       会更新为 high+1, 即 pivot_idx, 使得其自身交换自身):
        #       [7, 3, 2, 8, 1, 9, 5, 4, 10, 6]
        while low <= high and nums[low] <= nums[pivot_idx]:
            # while nums[low] <= nums[pivot_idx]:
            low += 1
            # print("low=== ", low)
        # jy: 1) 为了防止 nums = [7, 3, 2, 8, 1, 9, 5, 4, 6, 0] 的情况下 high 值不断更新
        #       越界问题, 应补充逻辑 (low < high), 否则该情况下 high 会更新到 -11, 越界;
        #    2) 为了防止 nums = [7, 3, 2, 6, 8, 1, 9, 5, 4, 6, 10, 6] 情况下输出如下(即
        #       与 pivot_idx 交换后的 6 的右边仍有等于 6 的情况):
        #       [4, 3, 2, 6, 5, 1, 6, 8, 7, 6, 10, 9]
        #       需将 nums[high] >= nums[pivot_idx] 修改为 nums[high] > nums[pivot_idx], 即
        #       high 位置的值等于 pivot_idx 位置的值时也需要与目标 low 位置交换, 确保相等的
        #       值也都会被置于左侧;
        #    3) nums = [7, 3, 2, 6, 8, 1, 9, 5, 4, 10] 时, 如果条件是 low < high, 则会死循环;
        while low <= high and nums[high] > nums[pivot_idx]:
            # while low < high and nums[high] >= nums[pivot_idx]:
            # while nums[high] >= nums[pivot_idx]:
            high -= 1
            # print("high== ", high)

        if low < high:
            nums[low], nums[high] = nums[high], nums[low]

    nums[low], nums[pivot_idx] = nums[pivot_idx], nums[low]
    return low



#jy: 【undo】
def _partition_jy_low(nums, low, high):
    """
    基于 low 值作为 pivot, 目标: 实现把小于等于 pivot 放到其左边, 大于 pivot 的放到右边, 并返回 pivot 下标;
    """
    pivot_idx = low
    low += 1
    while low < high:
        while low <= high and nums[low] <= nums[pivot_idx]:
            low += 1
        while low <= high and nums[high] > nums[pivot_idx]:
            high -= 1

        if low < high:
            nums[low], nums[high] = nums[high], nums[low]
    # print(low, " ==== ", pivot_idx)
    nums[high], nums[pivot_idx] = nums[pivot_idx], nums[high]
    return high



nums = [5,1,1,2,0,0]
#Output: [0,0,1,1,2,5]
res = quick_sort_v1(nums)
print(res)


nums = [-1,2,-8,-10]
#Output: [-10,-8,-1,2]
res = quick_sort_v2(nums)
print(res)


# nums = [5,1,1,2,0,0]
# nums = [5, 2, 3, 1]
nums = [1, 2, 3]
# Output: [0,0,1,1,2,5]
res = quick_sort_jy(nums)
print(res)
print("=" * 88)
print(is_sort_algorithm_correct(1000, quick_sort_v1))
print(is_sort_algorithm_correct(1000, quick_sort_v2))
print(is_sort_algorithm_correct(1000, quick_sort_jy))