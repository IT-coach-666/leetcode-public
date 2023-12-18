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
title_jy = "count-and-say(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = "双指针 + 递归/循环 | 正则表达式 + 递归/迭代"



"""
The count-and-say sequence is a sequence of digit strings defined by the
recursive formula:
1) countAndSay(1) = "1"
2) countAndSay(n) is the way you would "say" the digit string from 
   countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number
of substrings such that each substring contains exactly one unique digit. 
Then for each substring, say the number of digits, then say the digit. 
Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":
图示参考: 

Given a positive integer `n`, return the `n-th` term of the count-and-say
sequence.

 

Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
  countAndSay(1) = "1"
  countAndSay(2) = say "1" = one 1 = "11"
  countAndSay(3) = say "11" = two 1's = "21"
  countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
 

Constraints:
1 <= n <= 30
"""


class Solution:
    """
解法 1: 循环 + 双指针法
    """
    def countAndSay_v1(self, n: int) -> str:
        # jy; 第一项为 "1", 而其前一项为空 (为什么要记录前一项? 因为后一项
        #     均是基于对前一项的描述得到)
        pre = ''
        cur = '1'

        # jy: 从第 2 项开始遍历
        for _ in range(1, n):
            # jy: 注意要将 cur 赋值给 pre, 因为当前项是基于上一个已表述完
            #     的项得到的
            pre = cur
            # jy: 重新初始化新的当前项 cur, 后续对前一项表述过程会不断更新
            cur = ''

            # jy: 定义双指针 start 和 end
            start = end = 0
            # jy: 开始遍历前一项, 并逐片段表述
            while end < len(pre):
                # jy: 统计重复元素的个数
                while end < len(pre) and pre[start] == pre[end]:
                    end += 1
                # jy: 表述方式: 元素出现次数与元素值拼接
                cur += str(end-start) + pre[start]
                # jy: 更新 start 为下一个待表述的开始位置
                start = end
        
        return cur


    """
解法 2: 递归 + 双指针
    """
    def countAndSay_v2(self, n: int) -> str:
        """
        n: 求外观数列的第 n 项
        """
        if n == 1:
            return "1"

        # jy: 求解前一项
        pre = self.countAndSay_v2(n - 1)

        # jy: 双指针法对前一项进行表述
        start = end = 0
        ans = ""
        # jy: 统计重复元素的个数
        while end < len(pre):
            while end < len(pre) and pre[start] == pre[end]:
                end += 1
            # jy: 表述方式: 元素出现次数与元素值拼接
            ans += str(end-start) + pre[start]
            # jy: 更新 start 为下一个待表述的开始位置
            start = end

        return ans


    """
解法 3: 递归 + 正则表达式

"(\d)\1*" 可以用来提取连在一块的元素, 如 '111221' 提取出的元素是 
['111', '22', '1'], 然后再返回要组装的字符串
    """
    def countAndSay_v3(self, n: int) -> str:
        import re

        if n == 1:
            return '1'
        pre = self.countAndSay_v3(n-1)

        pattern = r'(\d)\1*'
        re_compile = re.compile(pattern)
        # jy: 提取结果, 如 
        res = [_.group() for _ in re_compile.finditer(pre)]  
        # join 内部的 str(len(c)) + c[0] for c in res 是生成器类型
        return ''.join(str(len(c_num)) + c_num[0] for c_num in res)  


    """
解法 4: 正则表达式 + 循环
    """
    def countAndSay_v4(self, n: int) -> str:
        import re

        res = '1'
        pattern = r'(\d)\1*'
        re_compile = re.compile(pattern)
        for _ in range(n-1):
            # jy: 以 "111221" 为例, group() 匹配的是 "111" (全局匹配), 而
            #     group(1) 匹配到的是 "1" (第一个捕获组三个 1 中的第一个)
            res = re_compile.sub(lambda x: str(len(x.group())) + x.group(1), res) 
        return res


n = 1
res = Solution().countAndSay_v1(n)
# jy: "1"
print(res)


n = 4
res = Solution().countAndSay_v1(n)
# jy: "1211"
print(res)


n = 4
res = Solution().countAndSay_v2(n)
# jy: "1211"
print(res)


n = 4
res = Solution().countAndSay_v3(n)
# jy: "1211"
print(res)


n = 4
res = Solution().countAndSay_v4(n)
# jy: "1211"
print(res)


