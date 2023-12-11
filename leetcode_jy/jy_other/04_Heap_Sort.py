
"""
参考: https://www.runoob.com/python3/python-heap-sort.html
"""


from heapq import *
from verify_sort_algorithm import *


def heap_sort_v1(ls_):
    # jy: 将列表堆化(默认为最小堆)
    heapify(ls_)
    res = []
    for i in range(0, len(ls_)):
        res.append(heappop(ls_))

    # jy: 将已排好序的结果 res 更新原有 ls_ 中, 使得 ls_ 有序
    #     (后续校验函数需要确保传入的参数列表 ls_ 最终有序, 才能正确校验)
    for i in res:
        ls_.append(i)


def heapify_v2(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        # jy: 交换
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_v2(arr, n, largest)


def heap_sort_v2(arr):
    n = len(arr)
    # jy: 构建最大堆;
    for i in range(n, -1, -1):
        heapify_v2(arr, n, i)

    # jy: 一个个交换元素
    for i in range(n-1, 0, -1):
        # jy: 交换
        arr[i], arr[0] = arr[0], arr[i]
        heapify_v2(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heap_sort_v1(arr)
print(arr)

ls_ = [3, 5, 2, 1, 4]
heap_sort_v2(ls_)
print(ls_)

print(is_sort_algorithm_correct(1000, heap_sort_v1))
print(is_sort_algorithm_correct(1000, heap_sort_v2))

