
"""
参考: https://www.runoob.com/python3/python-shellsort.html
https://www.runoob.com/data-structures/shell-sort.html

gap 的选择:
Knuth 序列:
h(1) = 1
h(n) = 3 * h(n-1) + 1  (n > 1)

还有其它序列, 希尔排序用的不多;
"""

from verify_sort_algorithm import *


"""
改进的插入排序: 对数组的指定间隔为 gap 的元素做插入排序，随后 gap 减半后不断重
复，直到 gap 为 1 (gap 为 1 时其实就是真正的插入排序);
"""
def shell_sort_v1(ls_):
    # jy: gap 值取列表长度的一半;
    gap = len(ls_) // 2
    while gap > 0:
        # jy: version-1: 插入排序逻辑(原始插入排序即 gap 为 1 时的以下逻辑) ----- Begin
        '''
        for i in range(gap, len(ls_)):
            tmp_i = ls_[i]
            j = i
            while j - gap >= 0 and ls_[j - gap] > tmp_i:
                ls_[j] = ls_[j - gap]
                j -= gap
            ls_[j] = tmp_i
        '''
        # jy: version-1: 插入排序逻辑(原始插入排序即 gap 为 1 时的以上逻辑) ----- End

        # jy: version-2: 插入排序逻辑(原始插入排序即 gap 为 1 时的以下逻辑) ----- Begin
        for i in range(gap, len(ls_)):
            j = i
            while j > 0 and ls_[j - gap] > ls_[j]:
                ls_[j - gap], ls_[j] = ls_[j], ls_[j - gap]
                j -= gap
        # jy: version-2: 插入排序逻辑(原始插入排序即 gap 为 1 时的以上逻辑) ----- End

        gap >>= 1

    return ls_


"""
gap 基于 Knuth 序列; Kunth 序列:
h(1) = 1
h(n) = 3 * h(n-1) + 1  (n > 1)
"""
def shell_sort_v2(ls_):
    h = 1
    while h <= len(ls_) // 3:
        h = h * 3 + 1
    gap = h
    while gap > 0:
        # jy: version-1: 插入排序逻辑(原始插入排序即 gap 为 1 时的以下逻辑) ----- Begin
        '''
        for i in range(gap, len(ls_)):
            tmp_i = ls_[i]
            j = i
            while j - gap >= 0 and ls_[j - gap] > tmp_i:
                ls_[j] = ls_[j - gap]
                j -= gap
            ls_[j] = tmp_i
        '''
        # jy: version-1: 插入排序逻辑(原始插入排序即 gap 为 1 时的以上逻辑) ----- End

        # jy: version-2: 插入排序逻辑(原始插入排序即 gap 为 1 时的以下逻辑) ----- Begin
        for i in range(gap, len(ls_)):
            j = i
            while j > 0 and ls_[j - gap] > ls_[j]:
                ls_[j - gap], ls_[j] = ls_[j], ls_[j - gap]
                j -= gap
        # jy: version-2: 插入排序逻辑(原始插入排序即 gap 为 1 时的以上逻辑) ----- End

        gap = (gap - 1) // 3

    return ls_


ls_ = [3, 5, 2, 1, 4]
shell_sort_v1(ls_)
print(ls_)

arr = [12, 11, 13, 5, 6, 7]
shell_sort_v2(arr)
print(arr)


print(is_sort_algorithm_correct(1000, shell_sort_v1))

print(is_sort_algorithm_correct(1000, shell_sort_v2))

