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
title_jy = "Restore-IP-Addresses(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""



"""
A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but 
"0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string `s` containing only digits, return all possible valid IP 
addresses that can be formed by inserting dots into `s`. You are not allowed
to reorder or remove any digits in `s`. You may return the valid IP addresses
in any order.

 

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
 

Constraints:
1) 1 <= s.length <= 20
2) `s` consists of digits only.
"""


class Solution:
    """
解法 1: 回溯（Bachtracking）
    """
    def restoreIpAddresses_v1(self, s: str) -> List[str]:
        # 特殊情况处理
        if not s or len(s) < 4:
            return []
        # 初始化结果列表
        res = list()
        # DFS递归，需要传入字符串s，对s的分割次数（初始为0），划分的中间（最终）结果，最终结果列表res
        self.dfs(s, 0, '', res)
        # 返回结果列表
        return res
    
    # DFS递归，s为目标字符串，idx为对s的分割次数（也是递归深度），path为划分的中间（最终）结果字符串，res为结果列表
    def dfs(self, s: str, idx: int, path: str, res: List[str]):
        # 如果idx大于4，那么说明字符串s已经被分割的次数大于4，此时直接返回
        if idx > 4:
            return 
        # 如果idx等于4，那么还要继续判断递归传入的s是否已经为空，如果s为空则说明字符串已经被完全分割为IP地址的形式，此时将该分割方法（路径）存储到结果列表res中，然后返回
        if idx == 4 and not s:
            # 这里符合条件的path的形式应该是"xxx.xxx.xxx.xxx."，因此path[:-1]是为了舍弃最后的'.'字符
            res.append(path[:-1])
            return
        # 对s的下标进行遍历
        for i in range(len(s)):
            # 后面的if语句用于处理以下两种情况：
            # （1）当s的首字符为'0'时，可以直接将'0'作为IP地址中四个整数之一
            # （2）当s的首字符不为'0'时，需要保证s[:i+1]处于IP地址整数的范围之内
            if s[:i+1] == '0' or (s[0] != '0' and 0 < int(s[:i+1]) < 256):
                # DFS递归调用的参数需要进行以下操作：
                # （1）将下标i之后的s[i+1:]字符串作为新的s进行递归参数传入
                # （2）分割次数idx+1
                # （3）将中间字符串结果path后连接下标i之前的s[:i+1]字符串，并在最后加入'.'
                # （4）结果列表res依然原封不动的传入下次递归
                self.dfs(s[i+1:], idx+1, path+s[:i+1]+'.', res)




s = "25525511135"
res = Solution().restoreIpAddresses_v1(s)
# jy: ["255.255.11.135", "255.255.111.35"]
print(res)


s = "0000"
res = Solution().restoreIpAddresses_v1(s)
# jy: ["0.0.0.0"]
print(res)


s = "101023"
res = Solution().restoreIpAddresses_v1(s)
# jy: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
print(res)



