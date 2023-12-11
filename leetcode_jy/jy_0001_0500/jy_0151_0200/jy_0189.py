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
title_jy = "Rotate-Array(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given an array, rotate the array to the right by k steps, where k is non-negative.



Example 1:
Input:  [1, 2, 3, 4, 5, 6, 7] and k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
Explanation:
rotate 1 steps to the right: [7, 1, 2, 3, 4, 5, 6]
rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5]
rotate 3 steps to the right: [5, 6, 7, 1, 2, 3, 4]

Example 2:
Input:  [-1, -100, 3, 99] and k = 2
Output: [3, 99, -1, -100]
Explanation:
rotate 1 steps to the right: [99, -1, -100, 3]
rotate 2 steps to the right: [3, 99, -1, -100]



Note: Try to come up as many solutions as you can, there are at least 3 different ways to
solve this problem. Could you do it in-place with O(1) extra space?
"""


from typing import List
class Solution:
    """
解法1(超时): 这道题和 061_Rotate-List.py 核心思想一样, 也是将数组想象成首尾相连的环, 记数组的长度
为 L, 则旋转数组等价于将数组末尾 k mod L 个元素移动到数组的开头; 由于移动一个数组元素会造成其他元
素的移动, 所以整体的算法复杂度为 (k mod L)*(L - (k mod L)), 对于给定的 L, 记 k mod L = x, 则复杂度为
x(L-x), 是一个抛物线, 当 x = L/2 时函数有最大值, 所以最坏的情况下解法1有 O(n^2) 的复杂度, 故此解
法会导致超时;
    """
    def rotate_v1(self, nums: List[int], k: int) -> None:
        # jy: 求出 k mod L 的值(因为 K 有可能比 L 大, 故结果不一定总等于 K)
        step = k % len(nums)
        length = len(nums)
        # jy: 总共需要移动 step 步, 每次循环移动 1 步; 以 [1, 2, 3, 4, 5, 6, 7] and k = 3 为例:
        #    第一次循环的结果为 [5, 1, 2, 3, 4, 6, 7]
        #    第二次循环的结果为 [5, 6, 1, 2, 3, 4, 7]
        #    第三次循环的结果为 [5, 6, 7, 1, 2, 3, 4]
        #    可以通过第二个 for 循环中 print 打印输出查看;
        for i in range(step):
            # jy: temp 最开始指向数组末尾 step 个要移动的元素的第一个对应的下标;
            # temp = nums[length - step + i]  # jy: 不需要此部分逻辑, 见 for 循环后的代码注释;
            # jy: j 从数组末尾 step 个要移动的元素的第一个对应的下标开始逐渐递减到 i+1 (每次递
            #    减 1; 注意, range(n, i , -1) 时, 最终 i 是取不到的, 最小值为 i+1); 经过一轮
            #    循环后, 末尾 step 个要移动的元素的第一个元素将被移动到数组首位(即最终该数的
            #    目标位置); 随后下一轮循环时, 将数组末尾 step 个要移动的元素的第二个移动到数
            #    组的第二位, 也即该数值的最终目标位置; 如此经过 step 次循环, step 个元素也即
            #    都被移动到目标位置上(原先的元素都将后移 step 步);
            for j in range(length - step + i, i, -1):
                # jy: 将下标为 j 和 j-1 的值进行互换;
                nums[j], nums[j-1] = nums[j-1], nums[j]
            # nums[i] = temp   # jy: 经过以上循环后, nums[i] 已经是 temp 所指的元素了;
            # print(nums)


    """
解法2: 和解法 1 思想一样, 只是移动数组元素时使用额外的空间先暂存数组前 (L - k mod L) 个元素, 然后移动数组
尾 k mod L 个元素到数组头, 最后从辅助数组中将剩下的元素移回到原数组中, 整体时间复杂度降为 O(n), 空间复杂
度上升为 O(n);
    """
    def rotate_v2(self, nums: List[int], k: int) -> None:
        step = k % len(nums)
        length = len(nums)
        # jy: 先暂存数组前 (L - k mod L) 个元素
        temp = [nums[i] for i in range(length - step)]
        # jy: 先将后 step 个待反转的数值移动到数组的前 step 位置;
        for i in range(step):
            nums[i] = nums[length - step + i]
        # jy: 再将原先缓存的元素逐个添加到前 step 个元数之后;
        #    注意: 要把 temp 中的元数直接加 nums 的 step 下标开始之后; 有两种 for 循环写法:
        '''
        for i in range(step, length):
            # jy: i-step 最初为 0, 后续将逐渐递增, 最终为 length-1-step, 即 temp 的最后一个元素;
            nums[i] = temp[i - step]
        '''
        for i in range(len(temp)):
            nums[step + i] = temp[i]


    """
解法3: 当数组尾的 k mod L 个元素被移动到数组头后, 如果把数组头的 k mod L 个元素反转, 再把数组尾
的 L - k mod L 个元素反转, 则得到的数组等价于将原数组反转; 所以我们可以先将整个数组反转, 然后将
数组头的 k mod L 个元素反转, 接着将数组尾的 L - k mod L 个元素反转, 即得到最终旋转的数组;
    """
    def rotate_v3(self, nums: List[int], k: int) -> None:
        step = k % len(nums)
        length = len(nums)
        # jy: 将整个数组反转, 反转后, 原先末尾的 step 个元素即被反转到数组前 step 个, 但与原先的相比
        #    是倒序了; 同理, 原先前 length-step 个元素被反转到后 length-step 个, 但也倒序了;
        self._reverse(nums, 0, length - 1)
        # jy: 将前 step 个元素再反转一次, 即为旋转后的前 step 个元素的结果;
        self._reverse(nums, 0, step - 1)
        # jy: 将后 length-step 个元素再反转一次, 即为旋转后后 length-step 个元素的结果;
        self._reverse(nums, step, length - 1)

    def _reverse(self, nums: List[int], low: int, high: int) -> None:
        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1


    """
解法4: 当我们把数组尾的 (k mod L) 个元素移动到数组头后, 对于数组后 (L - k mod L) 个元素来说, 需要将
后 k mod L 个元素移动到 L - k mod L 这个子数组的头部, 即又变成了一个旋转数组的问题, 只是数组的大
小变成了 L - k mod L, 所以可以用递归来求解; 每次递归交换的元素个数是 k mod L', L' 是每次递归的子
数组的大小, 递归完成时, 总共交换的元素个数不超过 L, 所以算法的时间复杂度是 O(n), 空间复杂度是 O(1);

JY: 该算法本地测试样例测试结果不符合预期, 但 Leetcode 上提交成功;
    """
    def rotate_v4(self, nums: List[int], k: int) -> None:
        # jy: 旋转 nums[0, len(nums)] 中的后 k 个元素;
        self._rotate_v4(nums, k, 0, len(nums) - 1)

    def _rotate_v4(self, nums: List[int], k: int, low: int, high: int) -> None:
        # jy: 终止递归条件;
        if low >= high or k == 0:
            return

        size = high - low + 1
        step = k % size

        for i in range(step):
            nums[low + i], nums[high-step+1+i] = nums[high-step+1+i], nums[low + i]
        # print("====== %s" % str(nums))

        self._rotate_v4(nums, step, low + step, high)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
# Output: [5, 6, 7, 1, 2, 3, 4]
res = Solution().rotate_v1(nums, k)
print(nums)

nums = [1, 2, 3, 4, 5, 6, 7]
res = Solution().rotate_v2(nums, k)
print(nums)

nums = [-1, -100, 3, 99]
k = 2
# Output: [3, 99, -1, -100]
res = Solution().rotate_v3(nums, k)
print(nums)

nums = [-1, -100, 3, 99]
res = Solution().rotate_v4(nums, k)
print(nums)

nums = [1, 2, 3, 4, 5, 6, 7]
res = Solution().rotate_v4(nums, k)
print(nums)


