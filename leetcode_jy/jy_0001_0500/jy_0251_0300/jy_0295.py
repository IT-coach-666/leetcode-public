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
title_jy = "Find-Median-from-Data-Stream(class)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
The median is the middle value in an ordered integer list. If the size of the list is
even, there is no middle value and the median is the mean of the two middle values.
For example, for arr = [2,3,4], the median is 3, for arr = [2,3], the median is
(2 + 3) / 2 = 2.5. Implement the ``MedianFinder`` class:
MedianFinder() : initializes the MedianFinder object.
void addNum(int num) : adds the integer num from the data stream to the data structure.
double findMedian() : returns the median of all elements so far. Answers within 10^-5 of
                      the actual answer will be accepted.


Example 1:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:
-10^5 <= num <= 10^5
There will be at least one element in the data structure before calling findMedian.
At most 5 * 10^4 calls will be made to ``addNum`` and ``findMedian``.


Follow up:
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""


import bisect
from heapq import heappush, heappushpop


"""
解法1: 直接的解法是在添加数字时对底层数组排序, 取中位数时直接取中间的数字

JY: 性能差, 内存占用低;
"""
class MedianFinder_v1:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.numbers = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.numbers, num)

    def findMedian(self) -> float:
        size = len(self.numbers)

        return self.numbers[size // 2] if size & 1 == 1 else (self.numbers[size // 2 - 1] + self.numbers[size // 2]) / 2


"""
解法2: 使用 self.small 最小堆保存数组的前半部分(保存时将用原数值的相反数进行保存, 这样就能确
保堆顶的元素值对应的相反数为数组前半部分的最大值), 使用 self.large 保存数组的后半部分(保存时
基于数组后半部分的原数值进行保存, 这样就能确保堆顶的元素值是数组后半部分中的最小值); 那么中位
数就是两个堆顶的元素之和的一半;

JY: Python 默认的是小顶堆, 所以为了获取数组前半部分的最大值, 需将前半部分的相反数加入 self.small
中, 此时的堆顶数值对应的相反数即为数组前半部分的最大值;

JY: 性能极高
"""
class MedianFinder_v2:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # jy: self.small 用于保存数组的前半部分(入堆时采用数值的相反数入堆, 确保堆顶元素对应的数
        #     值的相反数即为原先前数组半部分的最大数值);
        self.small = []
        # jy: self.large 用于保存数组的后半部分(入堆时基于数组后半部分的原数值入堆, 确保堆顶即为
        #     原先数组后半部分的最小数值;
        self.large = []

    def addNum(self, num: int) -> None:
        # jy: 如果 self.small 与 self.large 中数值个数相等, 则将当前元素的相反数加入 self.small,
        #     同时从 self.small 中出堆一个元素, 该元素的相反数即为 self.small 中对应的原数组的前
        #     半部分的最大值, 将其加入 self.large 中; 该操作确保 self.large 中的元素个数总是大于
        #     或等于 self.small 中的元素个数(大于时比 self.small 多 1 个元素), 且确保 self.large
        #     中对应的原数值均是大于 self.small 中对应的原数值的;
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        # jy: 如果当 self.small 与 self.large 中数值个数不等时(即 self.large 的个数比 self.small
        #     的多 1 个), 此时需要从当前数值 num 和 self.large 中的数值中找出一个最小数值(通过先
        #     将 num 入 self.large 堆, 在从该堆顶出一数值的方式找到)加入到 self.small 中(加入时以
        #     相反数的形式加入, 确保 self.small 的堆顶对应的数值的相反数是原先数组前半部分的最大值)
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        # jy: self.large 中元素的个数总是比 self.small 的个数多 1 个或相等; 且 self.small 存放的是
        #     数据流的前半部分的相反数(确保堆顶的数值的相反数是前半部分的最大值), self.large 存放的
        #     是数据流的后半部分(存放原值), 其堆顶即为后半部分的最小值;
        # jy: 当 self.small 和 self.large 个数相等时, median 值为两个堆的堆顶元素值之和除以 2 (其中
        #     self.small 的堆顶值为原数据流前半部分的最大值的相反数, 因此需要再取相反数恢复原值),
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2
        # jy: 当 self.large 比 self.small 的个数多 1 个时, 直接返回 self.large 的堆顶值即可;
        else:
            return float(self.large[0])


medianFinder = MedianFinder_v1()
medianFinder.addNum(1)                # arr = [1]
medianFinder.addNum(2)                # arr = [1, 2]
print(medianFinder.findMedian())      # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)                # arr[1, 2, 3]
print(medianFinder.findMedian())      # return 2.0


medianFinder = MedianFinder_v2()
medianFinder.addNum(1)                # arr = [1]
medianFinder.addNum(2)                # arr = [1, 2]
print(medianFinder.findMedian())      # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)                # arr[1, 2, 3]
print(medianFinder.findMedian())      # return 2.0


