
"""
通常有序条件下可以进行二分查找
无序条件下特殊任务也可以采用二分查找, 如查找数组中的局部最小值;
"""


def get_leftest_target(ls_, target):
    """
    查找有序数组中大于或等于目标值 target 的最左侧下标【undo】
    """
    left, right = 0, len(ls_) - 1
    idx = -1
    while left <= right:
        mid = left + (right - left) >> 1
        if ls_[mid] >= target:
            idx = mid
            right = mid - 1
        else:
            left = mid + 1
    return idx


def get_local_minimum_idx(ls_):
    """
    查找数组中的局部最小值
    """
    if not ls_:
        return -1
    if len(ls_) == 1 or ls_[0] < ls_[1]:
        return 0
    if ls_[-1] < ls_[-2]:
        return len(ls_) - 1

    left = 1
    right = len(ls_) - 2
    while left < right:
        mid = left + (right - left) // 2
        if ls_[mid] > ls_[mid - 1]:
            right = mid - 1
        elif ls_[mid] > ls_[mid + 1]:
            left = mid + 1
        else:
            return mid
    return left


# ls_ = [1, 2, 2, 3, 4, 4, 4, 5, 6]
# print(get_leftest_target(ls_, 3))


# ls_ = [2, 1, 0, 4, 5]
# print(get_local_minimum_idx(ls_))






