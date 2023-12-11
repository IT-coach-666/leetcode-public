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
title_jy = "Random-Pick-with-Weight(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
You are given an array of positive integers ``w`` where ``w[i]`` describes the weight
of i-th index (0-indexed). We need to call the function ``pickIndex()`` which randomly
returns an integer in the range [0, w.length - 1]. ``pickIndex()`` should return the
integer proportional to its weight in the ``w`` array. For example, for w = [1, 3], the
probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability
of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).


Example 1:
Solution solution = new Solution([1]);
solution.pickIndex();   # return 0. Since there is only one single element on the array
                        # the only option is to return the first element.

Example 2:
Solution solution = new Solution([1, 3]);
solution.pickIndex();   # return 1. It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex();   # return 1
solution.pickIndex();   # return 1
solution.pickIndex();   # return 1
solution.pickIndex();   # return 0. It's returning the first element (index = 0) that has probability of 1/4.
Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.


Constraints:
1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
"""


from random import randint
from typing import List


"""
新建一个数组 accumulated_weight_sum, 对于该数组中位置 i 处的元素有:
accumulated_weight_sum[i] = w[0] + w[1] + ... + w[i]

随后, 在 1 到所有权重和(即 accumulated_weight_sum[-1])之间生成一个随机数, 在
accumulated_weight_sum 中找该随机数的插入位置 (即为了维持数组有序性插入的位置,
即 035_Search Insert Position);
"""
class Solution:

    def __init__(self, w: List[int]):
        # jy: 新建一个数组 accumulated_weight_sum, 对于该数组中位置 i 处的元素有:
        #    accumulated_weight_sum[i] = w[0] + w[1] + ... + w[i]
        self.accumulated_weight_sum = [i for i in w]
        for i in range(1, len(w)):
            self.accumulated_weight_sum[i] += self.accumulated_weight_sum[i-1]

    def pickIndex(self) -> int:
        low, high = 0, len(self.accumulated_weight_sum) - 1
        # jy: 在 1 到所有权重和之间生成一个随机数, 根据这个随机数在 accumulated_weight_sum 找
        #    到所属的位置 (即为了维持数组有序性插入的位置, 即 035_Search Insert Position);
        #    如 ``w`` 为 [1, 3] 时, 对应的 accumulated_weight_sum 为 [1, 4], 此时生成的随机数
        #    randint(1, 4), 会随机生成 [1, 4] 之间的数值(包含 1 和 4 在内, 每个数值生成的概率
        #    均相同), 则生成的随机数大于 1 的概率为 3/4, 等于 1 的概率为 1/4, 而对于 ``035``
        #    题中的逻辑, 如果数值等于 1, 会返回原先 1 对应的位置, 如果大于 1 , 则返回其后一位;
        target = randint(1, self.accumulated_weight_sum[-1])

        while low < high:
            middle = low + (high - low) // 2

            if self.accumulated_weight_sum[middle] == target:
                return middle
            elif self.accumulated_weight_sum[middle] < target:
                low = middle + 1
            else:
                high = middle

        return low


solution = Solution([1])
print(solution.pickIndex())   # return 0. Since there is only one single element on the array
                              # the only option is to return the first element.
print("="*88)
solution = Solution([1, 3])
print(solution.pickIndex())   # return 1. It's returning the second element (index = 1) that has probability of 3/4.
print(solution.pickIndex())   # return 1
print(solution.pickIndex())   # return 1
print(solution.pickIndex())   # return 1
print(solution.pickIndex())   # return 0. It's returning the first element (index = 0) that has probability of 1/4.


