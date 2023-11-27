# M0018_4Sum.py-U

"""
Given an array nums of n integers and an integer target, are there elements a, b, c, 
and d in nums such that a + b + c + d = target? Find all unique quadruplets in the 
array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[ [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]]
"""



from typing import List
class Solution:
    """
有了 3Sum 的经验, 此题等价于遍历数组, 然后在其余的元素中求解 3Sum, 算法的时间复杂度是 O(n^3);
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # jy: 对列表进行排序;
        nums.sort()
        sums = []
        # jy: 遍历数组, 即第一个数(最后 3 个数值不遍历, 用于求 3Sum)
        for i in range(len(nums)-3):
            # jy: 碰到相同的值不再进行计算, 避免重复;
            if i-1 >= 0 and nums[i] == nums[i-1]:
                continue
            # jy: 遍历数组, 从第一个数的下标之后开始遍历, 即第二个数;
            for j in range(i+1, len(nums)-2):
                # jy: 碰到相同的值不再进行计算, 避免重复;
                if j-1 >= i+1 and nums[j] == nums[j-1]:
                    continue
                # jy: 找出两数之和为 k 的结果;
                k = target - nums[i] - nums[j]
                # jy: 两数的范围由第二个数的后一个开始算起(下标为 j+1), 到最后一个;
                low, high = j+1, len(nums)-1
                while low < high:
                    if nums[low] + nums[high] == k:
                        sums.append([nums[i], nums[j], nums[low], nums[high]])
                        # jy: 碰到相同的值不再进行计算, 避免重复;
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < k:
                        low += 1
                    else:
                        high -= 1
        return sums


nums = [1, 0, -1, 0, -2, 2]
target = 0
res = Solution().fourSum(nums, target)
print(nums, " === ", target, " === ", res)



