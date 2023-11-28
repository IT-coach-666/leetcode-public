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
title_jy = "Generate-Parentheses(string)"
# jy: 记录不同解法思路的关键词
tag_jy = "递归（注意递归调佣过程中的细节）"


"""
Given `n` pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.


For example, given n = 3, a solution set is:
[ "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"]
"""


class Solution:
    """
解法 1: 递归求解

左括号和右括号各自只能使用 n 个, 每次递归记录当前可用的左、右括号的个数, 当
左右括号数都等于 0 时, 表示收集到了一个匹配的括号组合

递归时的细节: 如果可用的左括号数量大于 0, 则尝试加入左括号, 如果可用的右括号
的数量大于可用的左括号的数量, 则加入一个右括号
    """
    def generateParenthesis_v1(self, n: int) -> List[str]:
        result = []
        self._generate(n, n, '', result)
        return result

    def _generate(self, left: int, right: int,
                  parenthesis: str, result: List[str]) -> None:
        """
        left: 剩余可用的左括号数
        right: 剩余可用的右括号数
        parenthesis: 左右括号组合的字符串结果
        result: 结果列表
        """
        # jy: 如果左右括号均无剩余, 表明左右括号均已加入到 parenthesis 字符
        #     串中, 此时将该字符串加入结果列表, 并终止递归
        if left == 0 and right == 0:
            result.append(parenthesis)
            return

        # jy: 如果左括号剩余可用个数大于 0, 则优先添加左括号 (因为左括号无论
        #     什么情况下均可加入到 parenthesis 字符串中)
        if left > 0:
            # jy: 往 parenthesis 加入左括号后, 左括号剩余个数减 1, 右括号剩余
            #     个数仍为当前传入该函数时的个数
            self._generate(left - 1, right, parenthesis + '(', result)

        # jy: 只有在右括号剩余个数大于左括号时, 才能添加右括号 (小于或等于时
        #     不能添加, 否则会导致括号无法配对)
        if left < right:
            # jy: 往 parenthesis 加入右括号后, 右括号剩余个数减 1, 左括号剩余
            #     个数仍为当前传入该函数时的个数
            self._generate(left, right - 1, parenthesis + ')', result)

    """
解法 2: 递归, 统计括号时是做加法 (解法 1 中是做减法)
    """
    def generateParenthesis_v2(self, n: int) -> List[str]:
        res = []
        cur_str = ''

        def dfs(cur_str, left, right, n):
            """
            cur_str: 当前子串 (从根结点到叶子结点的路径字符串)
            left: 左括号已经使用的个数
            right: 右括号已经使用的个数
            """
            if left == n and right == n:
                res.append(cur_str)
                return

            # jy: 剪枝, 确保添加的左括号数大于右括号数 (可以将该判断放到最
            #     后一个 if 语句)
            if left < right:
                return

            if left < n:
                dfs(cur_str + '(', left + 1, right, n)

            # jy: 如果此处限定 `left > right`, 则以上不需要进行剪枝操作;
            #if left > right:
            if right < n:
                dfs(cur_str + ')', left, right + 1, n)

        dfs(cur_str, 0, 0, n)
        return res

    def generateParenthesis_v3(self, n: int) -> List[str]:
        if n == 0:
            return []
        total_l = []
        total_l.append([None])    # 0组括号时记为None
        total_l.append(["()"])    # 1组括号只有一种情况
        for i in range(2,n+1):    # 开始计算i组括号时的括号组合
            l = []        
            for j in range(i):    # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
                now_list1 = total_l[j]    # p = j 时的括号组合情况
                now_list2 = total_l[i-1-j]    # q = (i-1) - j 时的括号组合情况
                for k1 in now_list1:  
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        l.append(el)    # 把所有可能的情况添加到 l 中
            total_l.append(l)    # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_l[n]


    """
解法 4: 暴力法

可以生成所有 2^(2n) 个 "(" 和 ")" 字符构成的序列, 然后过滤掉无效的部分

可以使用递归生成所有序列; 长度为 n 的序列就是在长度为 n−1 的序列前加一
个 "(" 或 ")"

检查序列是否有效: 遍历这个序列, 并使用一个变量 bal 表示左括号的数量减去
右括号的数量; 如果在遍历过程中 bal 的值小于零, 或结束时 bal 的值不为零,
则该序列无效, 否则有效
    """
    def generateParenthesis_v4(self, n: int) -> List[str]:
        def generate(A):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                # jy: 回溯
                A.pop()
                A.append(')')
                generate(A)
                # jy: 回溯
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': 
                    bal += 1
                else: 
                    bal -= 1

                if bal < 0: 
                    return False
            return bal == 0

        ans = []
        generate([])
        return ans


n = 3
res = Solution().generateParenthesis_v1(n)
print(n, " === ", res)

res = Solution().generateParenthesis_v2(n)
print(n, " === ", res)


res = Solution().generateParenthesis_v3(n)
print(n, " === ", res)


res = Solution().generateParenthesis_v4(n)
print(n, " === ", res)

