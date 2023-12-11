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
title_jy = "Guess-Number-Higher-or-Lower-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
We are playing the Guessing Game. The game will work as follows:
1) I pick a number between 1 and n.
2) You guess a number.
3) If you guess the right number, you win the game.
4) If you guess the wrong number, then I will tell you whether the number I picked is higher or
   lower, and you will continue guessing.
5) Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.

Given a particular n, return the minimum amount of money you need to guarantee a win
regardless of what number I pick.



Example 1:
Input: n = 10
Output: 16
Explanation: The winning strategy is as follows:
- The range is [1,10]. Guess 7.
    - If this is my number, your total is $0. Otherwise, you pay $7.
    - If my number is higher, the range is [8,10]. Guess 9.
        - If this is my number, your total is $7. Otherwise, you pay $9.
        - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
        - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
    - If my number is lower, the range is [1,6]. Guess 3.
        - If this is my number, your total is $7. Otherwise, you pay $3.
        - If my number is higher, the range is [4,6]. Guess 5.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
            - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
            - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
        - If my number is lower, the range is [1,2]. Guess 1.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
            - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.


Example 2:
Input: n = 1
Output: 0
Explanation: There is only one possible number, so you can guess 1 and not have to pay anything.


Example 3:
Input: n = 2
Output: 1
Explanation: There are two possible numbers, 1 and 2.
- Guess 1.
    - If this is my number, your total is $0. Otherwise, you pay $1.
    - If my number is higher, it must be 2. Guess 2. Your total is $1.
The worst case is that you pay $1.


Constraints:
1 <= n <= 200
"""


class Solution:
    """
动态规划: 记 dp[i][j] 为猜测 i 到 j 之间的数所需要的最少的钱(即最坏情况下需要的钱);
对于 dp[i][j] 来说, 假设我们猜的数字为 k, 其中 i <= k <= j, 当 k 不是正确的数值(即
没猜中)时, 要么继续在 [i, k-1] 中猜, 要么在 [k+1, j] 中猜(JY: 由于不会给定具体要猜
的数值, 所以考虑所有数值都可能是要被猜的数值, 因此不能很肯定地确保当前猜的数值是偏
大还是偏小了, 均有可能, 需要把两种情况都考虑进去), 所以猜测 k 的成本是(由于假设 k
没猜对, 所以需要付出数额为 k 的成本后继续猜; 由于目的是要求最坏情况下需要的成本, 即
至少得多少钱, 所以不能假设 k 一猜就对):
k + max(dp[i][k-1], dp[k+1][j])

故 dp[i][j] 的值就是 i 到 j-1 中所有数字都猜测一遍所产生成本中的最小值;

【JY】为什么是取 min 最小值? 因为假设猜的人是聪明的, 给定一个数 n 后, 就知道需要从哪
个数开始起猜, 比如给定的数为 10, 从 7 开始猜是最明智的; 如果给定的数是 12, 则从 9 开
始猜是最明智的; 如果给定的数是 21, 从 14 开始猜是最明智的(可见, 最明智的猜法并不总是
从倒数第 4 个数开始猜);
此处要求的是一个聪明的人根据 n 拟定了猜测策略, 假设猜测过程也都是聪明的, 猜某个数最不
理想的情况需要花的最少钱是多少, 如 n 为 3 时, 即从 [1, 3] 中猜某个数, 猜不对时会得到偏
高或偏低的反馈, 则最明智的就是猜中间值 2, 最理想的情况下就是 0 成本(即一次就猜对), 但
如果猜错了得到反馈后, 付出成本 2 接下来就能肯定的知道要猜的数值了; 明智的猜法总不是从
1 开始猜的, 因为如果猜错, 则还需要从 2 或 3 中再猜一次, 成本明显变高; 如果从 3 开始猜,
猜错 1 次就成本大于 2 了, 且后续还要再猜一次, 还可能会再有成本;
    """
    def getMoneyAmount(self, n: int) -> int:
        # jy: 初始化 dp 数组, 为 n+1 方阵, 初始值均为 0;
        dp = [[0] * (n+1) for _ in range(n+1)]
        # jy: 倒序遍历 n, 作为 low 值; low 值其实可以从 n-1 开始倒序遍历, 因为 high 值至少会
        #    比 low 大 1, 且不会大于 n, 当 low 为 n 时, 是没有合适的 high 值存在的;
        for low in range(n-1, 0, -1):
        # for low in range(n, 0, -1):
            # jy: high 值设置为从 low+1 到 n+1 之间, 对该区间的值进行遍历;
            for high in range(low+1, n+1):
                # jy: dp[i][j] 表示猜测 i 到 j 之间的数至少需要多少钱能保证猜对(即最坏情况下需要的钱)
                #    由于一个确定的 n 值, 最明智的猜法是确定的, 此处的 min 就是获取那个最明智的猜法
                #    下的最差结果;
                dp[low][high] = min(x + max(dp[low][x-1], dp[x+1][high]) for x in range(low, high))

                # jy: test-only
                # if low == 1:
                #     print("======= ", [x + max(dp[low][x-1], dp[x+1][high]) for x in range(low, high)])
        return dp[1][n]



n = 10
# Output: 16
res = Solution().getMoneyAmount(n)
print(res)

n = 1
# Output: 0
res = Solution().getMoneyAmount(n)
print(res)


n = 2
# Output: 1
res = Solution().getMoneyAmount(n)
print(res)


n = 12
# Output: 21
res = Solution().getMoneyAmount(n)
print(res)


n = 21
# Output: 52
res = Solution().getMoneyAmount(n)
print(res)


n = 3
# Output: 2
res = Solution().getMoneyAmount(n)
print(res)


