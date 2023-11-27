# M0022_Generate-Parentheses.py

"""
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:
[ "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"]
"""


from typing import List


class Solution:
    """
递归求解, 左括号和右括号各自只能使用 n 个, 每次递归记录当前可用的左, 右括号的个数, 当
左右括号数都等于 0 时, 表示收集到了一个匹配的括号组合; 递归时, 如果可用的左括号数量大
于 0, 则尝试加入左括号, 如果可用的右括号的数量大于可用的左括号的数量, 则加入一个右括号;
    """
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self._generate(n, n, '', result)
        return result

    def _generate(self, left_parenthesis_count: int, right_parenthesis_count: int, parenthesis: str, result: List[str]) -> None:
        """
        left_parenthesis_count: 剩余可用的左括号数;
        right_parenthesis_count: 剩余可用的右括号数;
        parenthesis: 左右括号组合的字符串结果;
        result: 结果列表;
        """
        # jy: 如果左右括号均无剩余, 表明左右括号均已加入到 parenthesis 字符串中, 此时将该字符串加入结果列表, 并终止递归;
        if left_parenthesis_count == 0 and right_parenthesis_count == 0:
            result.append(parenthesis)
            return

        # jy: 如果左括号剩余可用个数大于 0, 则添加左括号(因为左括号无论什么情况下均可加入
        #    到 parenthesis 字符串中);
        if left_parenthesis_count > 0:
            # jy: 往 parenthesis 加入左括号后, 左括号剩余个数减 1, 右括号剩余个数仍为当前传入该函数时的个数;
            self._generate(left_parenthesis_count-1, right_parenthesis_count, parenthesis + '(', result)

        # jy: 只有在右括号剩余个数大于左括号时, 才能添加右括号(小于或等于时不能添加, 否则会导致括号无法配对);
        if left_parenthesis_count < right_parenthesis_count:
            # jy: 往 parenthesis 加入右括号后, 右括号剩余个数减 1, 左括号剩余个数仍为当前传入该函数时的个数;
            self._generate(left_parenthesis_count, right_parenthesis_count-1, parenthesis + ')', result)


n = 3
res = Solution().generateParenthesis(n)
print(n, " === ", res)



