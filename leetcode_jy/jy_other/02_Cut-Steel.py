
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
title_jy = "Cut-Steel(number)"
# jy: 记录不同解法思路的关键词
tag_jy = "钢条切割"


"""
钢条切割, 参考:
https://www.cnblogs.com/tgycoder/p/4980655.html
"""

class Solution:
    def __init__(self, dict_len_price):
        """
        dict_len_price 记录钢条的长度以及相应长度对应的价格; 以下解法 1 到解法 3 中, 所求
        的钢条长度 length 局限于 dict_len_price 中的最大长度;
        """
        self._len = [0]
        self._price = [0]
        for _len, _price in dict_len_price.items():
            self._len.append(_len)
            self._price.append(_price)
        self.dp = {}

    """
解法1: 普通递归;
    """
    def max_profit_cut_v1(self, length):
        if length == 0:
            return 0
        max_ = 0
        # jy: 遍历钢条的长度(每段长度都会有一个该长度对应的价格); 如果将钢条
        #     的切分为包含长度为 i 的一段, 则剩余的钢条的最大利润为对剩余长度 
        #     length - i 进行最大化价值切割的结果;
        for i in range(1, length + 1):
            max_ = max(max_, self._price[i] + self.max_profit_cut_v1(length - i))
        return max_

    """
解法2: 带缓存的递归(减少原递归中的重复运算); 其中缓存机制也可以使用 @lru_cache(None) 实现;
    """
    def max_profit_cut_v2(self, length):
        if length == 0:
            return 0
        if length in self.dp:
            return self.dp[length]

        max_ = 0
        for i in range(1, length + 1):
            max_ = max(max_, self._price[i] + self.max_profit_cut_v1(length - i))
        self.dp[length] = max_
        return max_

    """
解法3: 动态规划
    """
    def max_profit_cut_v3(self, length):
        dp = [i for i in self._price]
        for i in range(1, length + 1):
            
            #for j in range(1, i + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], dp[j] + dp[i - j])
        return dp[length]

    """
JY: 当钢条的长度超出 "长度-价格" 表中的最大长度时, 使用该方法;
    """
    def max_profit_cut(self, length):
        known_len = len(self._price) - 1
        multiply_ = length // known_len
        remain_ = length % known_len
        return multiply_ * self.max_profit_cut_v3(known_len) + self.max_profit_cut_v3(remain_)


dict_len_price = {
1: 1,
2: 5, #2,
3: 8,
4: 9,
5: 10,
6: 17,
7: 17,
8: 20,
9: 24,
10: 30
}
length = 10
for len_ in range(1, length+1):
    print("-"*66)
    res = Solution(dict_len_price).max_profit_cut_v1(len_)
    print("V1: original length: %d, maximun profit: %d" % (len_, res))
    res = Solution(dict_len_price).max_profit_cut_v2(len_)
    print("V2: original length: %d, maximun profit: %d" % (len_, res))
    res = Solution(dict_len_price).max_profit_cut_v3(len_)
    print("V3: original length: %d, maximun profit: %d" % (len_, res))
    
print("="*66)
len_ = 20
res = Solution(dict_len_price).max_profit_cut(len_)
print("Longer length: %d, maximun profit: %d" % (len_, res))





