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
title_jy = "Restore-IP-Addresses(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归 | IMP"



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
解法 1: 递归
    """
    def restoreIpAddresses_v1(self, s: str) -> List[str]:
        # jy: 特殊情况处理
        if not s or len(s) < 4 or len(s) > 12:
            return []

        ls_res = []
        self.dfs(s, 0, "", ls_res)
        return ls_res
    
    def dfs(self, s: str, sep_count: int, path: str, ls_res: List[str]):
        """
        s: 剩余待划分的字符串
        sep_count: 分割次数 (即递归深度), 相当于 path 中包含 "." 的个数
        path: 划分后的中间 (最终) 字符串
        ls_res: 存放结构的列表
        """
        # jy: 如果分割次数已经大于 4 了, 则返回, 终止递归 (此处逻辑去除不
        #     影响最终结果, 但会存在多余的处理逻辑)
        if sep_count > 4:
            return

        # jy: 如果分割次数 sep_count 等于 4, 且已经没有剩余待划分的字符串,
        #     则表明 path 中已经包含 4 个 "." 且囊括了所有数值, 即找到了一
        #     组有效结果, 将其加入结果列表中; 注意: 此时的 path 的最后一个
        #     字符也是 ".", 有效 IP 中只需要 3 个 "." 进行分割, 因此加入时
        #     不会将最后一个字符加入
        if sep_count == 4 and not s:
            ls_res.append(path[: -1])
            return

        # jy: 遍历剩余待划分的字符的每个下标位置 i, 不断尝试将 s[ :i+1] 加
        #     入到 path 中, 递归看是否能获得有效解
        for i in range(len(s)):
            # jy: s[: i+1] 是即将加入到 path 的部分, 当该部分为 "0" 时, 可
            #     以直接将 "0" 作为 IP 地址中四个整数之一; 如果该部分不为
            #     "0", 则需确保该部分的首字符不为 "0", 且对应的数值在有效范
            #     围内, 才能将其加入到 path 中
            if s[: i+1] == "0" or (s[0] != "0" and 0 < int(s[:i+1]) < 256):
                # jy: 将 s[ :i+1] 加入到 path 中, 并在最后补充 ".", 同时将
                #     sep_count 加 1 后继续递归, 后续递归过程的候选字符即
                #     为 s[i+1: ]
                self.dfs(s[i+1: ], sep_count + 1, path + s[: i+1] + ".", ls_res)


    """
解法 2: 递归的另一种写法
    """
    def restoreIpAddresses_v2(self, s: str) -> List[str]:
        ls_res = []
        def dfs(sep_count, path, s): 
            """
            sep_count: "." 的个数
            path: 划分后的中间 (最终) 字符串
            s: 剩余待划分的字符串
            """
            if sep_count == 4:
                if s == "":
                    ls_res.append(path[: -1])
                return

            if len(s) > 0:
                dfs(sep_count + 1, path + s[0] + ".", s[1:])

            if len(s) > 1 and s[0] != "0":
                dfs(sep_count + 1, path + s[:2] + ".", s[2:])

            if len(s) > 2 and s[0] != "0" and int(s[0:3]) < 256:
                dfs(sep_count + 1, path + s[:3] + ".", s[3:])
        dfs(0, "", s)
        return ls_res


    """
解法 3: 递归另一种写法 (需回溯)

一共四位, 每一位都可以取 0 - 255 之间这些数字, 即每一位都可以取 1 - 3 位, 也
就是每一位都有三种取法; 抽象出来就是四层, 三叉树, 从中去掉不符合规则的就可以
    """
    def restoreIpAddresses_v3(self, s: str) -> list:
        if len(s) < 4: 
            return []
        
        def getIP(s, idx, ls_ip_num, ls_res):
            """
            从 s[idx: ] 中取数加入到 ls_ip_num 中, 并将有效的结果 IP 记录
            到 ls_res
            """
            # jy: 以下逻辑中 ls_ip_num 是逐个添加元素的, 因此长度也逐渐增加,
            #     当长度达到 4 时, 即可终止递归, 此时如果发现正好遍历到 s 的
            #     末尾, 表明完成一个完整且有效的拆分, 将其加入结果列表
            if len(ls_ip_num) == 4:
                if idx == len(s):
                    ls_res.append(".".join(ls_ip_num))
                return 
                
            # jy: 基于 s 的当前下标 idx 进行取数, 最少取 1 位, 最多取 3 位
            for i in range(1, 4):
                # jy: 如果无法进一步取数, 则直接返回终止递归
                if idx + i > len(s):
                    break

                str_num = s[idx: idx + i]
                # jy: 如果数值不止一位, 则要求第一位不为 0, 否则不满足要求, 跳过
                if len(str_num) > 1 and str_num[0] == "0":
                    continue
                # jy: 如果数值大于 255, 则不满足要求, 直接跳过
                if int(str_num) > 255:
                    continue

                # jy: 执行到此处时即可确保当前数值为一个有效数值, 加入数值后递归
                ls_ip_num.append(str_num)
                getIP(s, idx + i, ls_ip_num, ls_res)
                # jy: 回溯, 防止以上往 ls_ip_num 中加入的 str_num 影响到
                #     下一个同层级的递归调用
                ls_ip_num.pop()
            
        ls_res = []
        getIP(s, 0, [], ls_res)
        return ls_res
                



s = "25525511135"
res = Solution().restoreIpAddresses_v1(s)
# jy: ["255.255.11.135", "255.255.111.35"]
print(res)


s = "0000"
res = Solution().restoreIpAddresses_v2(s)
# jy: ["0.0.0.0"]
print(res)


s = "101023"
res = Solution().restoreIpAddresses_v3(s)
# jy: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
print(res)



