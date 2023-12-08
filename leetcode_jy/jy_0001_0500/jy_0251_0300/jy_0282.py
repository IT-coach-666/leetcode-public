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
title_jy = "Expression-Add-Operators(number)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string num that contains only digits and an integer target, return all
possibilities to add the binary operators '+', '-' ,or '*' between the digits
of num so that the resultant expression evaluates to the target value.


Example 1:
Input: num = "123", target = 6
Output: ["1*2*3", "1+2+3"]

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Example 3:
Input: num = "105", target = 5
Output: ["1*0+5", "10-5"]

Example 4:
Input: num = "00", target = 0
Output: ["0*0", "0+0", "0-0"]

Example 5:
Input: num = "3456237490", target = 9191
Output: []


Constraints:
1 <= num.length <= 10
num consists of only digits.
-2^31 <= target <= 2^31- 1
"""



from typing import List



class Solution:
    """
在 494_Target-Sum.py 的基础上更进一步, 引入了乘号, 由于乘号的存在, 会改变运算的优先级,
基本思路参考 494_Target-Sum.py 的解法 2, 为了处理乘法, 在搜索时增加额外的参数表示上一个
数字, 那么对于乘法来说, 表达式的值等于当前表达式的值减去上一个数字, 加上上一个数字乘以
当前数字;

因为最终表达式中的数字可能有多位, 所以搜索时需要尝试所有长度的数字, 需要注意的是如果当
前起始搜索位置上的数字是 0, 那么后面数字组合就无需尝试, 因为类似 0x 的数字属于非法数字;
    """
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        self._dfs(num, '', 0, 0, 0, target, result)

        return result


    def _dfs(self, num, expression_so_far, current_value, last_digit, position, target, result):
        # jy: 如果当前位置等于字符串长度, 则判断当前值是否等于目标值, 如果等于, 则将当前构造的表达
        #    式字符串加入 result 列表中;  expression_so_far 表示当前表达式的字符串形式, current_value
        #    为当前表达式得到的数值, last_digit 为上一个数值;
        if position == len(num):
            if current_value == target:
                result.append(expression_so_far)

        # jy: 从 position 开始遍历至 num 字符串末尾;
        for i in range(position, len(num)):
            if i != position and num[position] == '0':
                break

            # jy: 获取数值
            digit_str = num[position: i+1]
            digit = int(digit_str)
            # jy: 如果是从字符串的第一个数值字符开始, 则 digit_str 前面没有运算符, current_value (当前数值) 和
            #    last_digit (上一个数值) 均为 digit;
            # jy: 每次递归调用 _dfs 时, 最后的三个参数传递的均为 (i+1, target, result)
            if position == 0:
                self._dfs(num, expression_so_far + digit_str, digit, digit, i+1, target, result)
            else:
                # jy: 当使用 "+" 号时, 当前表达式字符串格式更新为 "+" 当前数值的字符串格式; 当前数值更新为原表达式数
                #    值加上遍历得到的数值; 上一个数值即更新为 "+" 号后面的数值字符对应的数值(注意带符号, 此处为正);
                self._dfs(num, expression_so_far + '+' + digit_str, current_value + digit, digit, i+1, target, result)
                # jy: 当使用 "-" 号时, 当前表达式字符串格式更新为 "-" 当前数值的字符串格式; 当前数值更新为原表达式数
                #    值减去遍历得到的数值; 上一个数值即更新为 "-" 号后面的数值字符对应的数值(注意带符号, 此处为负);
                self._dfs(num, expression_so_far + '-' + digit_str, current_value - digit, -digit, i+1, target, result)
                # jy: 当使用 "*" 号时, 当前表达式字符串格式更新为 "*" 当前数值的字符串格式; 当前数值更新为原表达式数
                #    值减去上一个数值(由于 "*" 优先级更高, 该数值需要与当前遍历得到的数值做乘法运算) 再加上上一个数
                #    值与当前遍历得到的数值的相乘运算的结果; 上一个数值即更新为原上一个数值与当前遍历得到的数值的相
                #    乘运算的结果;
                self._dfs(num, expression_so_far + '*' + digit_str, current_value - last_digit + last_digit * digit,
                                                                               last_digit * digit, i+1, target, result)


num = "123"
target = 6
# Output: ["1*2*3", "1+2+3"]
res = Solution().addOperators(num, target)
print(res)


num = "232"
target = 8
# Output: ["2*3+2", "2+3*2"]
res = Solution().addOperators(num, target)
print(res)


num = "105"
target = 5
# Output: ["1*0+5", "10-5"]
res = Solution().addOperators(num, target)
print(res)


num = "00"
target = 0
# Output: ["0*0", "0+0", "0-0"]
res = Solution().addOperators(num, target)
print(res)


num = "3456237490"
target = 9191
# Output: []
res = Solution().addOperators(num, target)
print(res)


