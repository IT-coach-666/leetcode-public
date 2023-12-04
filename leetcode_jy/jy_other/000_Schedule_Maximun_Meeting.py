
"""
一些项目要占用一个会议室宣讲, 会议室不能同时容纳两个项目宣讲;
给定每个项目的开始时间和结束时间, 求给你一个会议室, 最多可安排的宣讲场数是多少;
"""


class Solution:

    def get_next_meeting_idx(self, ls_, current_idx):
        """
        获取参加当前会议时, 下一个能参加的会议的下标(ls_ 已根据开始时间排序)
        """
        for i in range(current_idx + 1, len(ls_)):
            if ls_[i][0] >= ls_[current_idx][1]:
                return i
        return -1

    def schedule_maximun_meeting_v1(self, ls_):
        # jy: 记 dp[i] 表示第 i 个会议到最后一个会议中会议时间不相交叉的会议数;
        #     dp 均初始化为 1(表示至少能进行第 i 个会议, 不会与其它会议冲突);
        dp = [1] * len(ls_)
        # jy: 按会议开始时间进行排序;
        ls_.sort(key=lambda x: x[0])
        # print("sorted====== ", ls_)

        # jy: 从倒数第二个会议开始向前遍历(因为最后一个会议肯定是可以参加的, 且其对应
        #     的 dp[len(ls_) - 1] 也已经初始化为 1, 不需要再次计算)
        for i in range(len(ls_) - 2, -1, -1):
            # jy: 找出第 i 个会议之后能参加的会议的下标;
            next_idx = self.get_next_meeting_idx(ls_, i)
            # jy: 如果下一个可参加的会议存在, 则 dp[i] 为以下两种情况取其大:
            #    1) 参加当前会议(即可参加的会议数加 1, 相当于是加上 dp[i] 的初始值), 加上从下一个
            #       能参加的会议开始到最后一个会议中能参加的最大会议数;
            #    2) dp[i+1], 即当前会议 i 不参加, 则相当于第 i+1 个到最后一个会议中能参加的最多会议数;
            if next_idx != -1:
                # jy: dp[i] 为参加当前会议或者不参加当前会议,
                dp[i] = max(dp[i] + dp[next_idx], dp[i+1])
        # jy: 最终返回 dp[0], 即从第一个会议到最后一个会议, 能参加的最大数量;
        return dp[0]

    """
JY: 不仅记录最多个数, 还记录会议起始时间段;
    """
    def schedule_maximun_meeting_v2(self, ls_):
        ls_.sort(key=lambda x: x[0])
        # print(ls_)
        # jy: 注意, 需要数组排列后再初始化 dp (dp 中均初始化为参加当前会议);
        dp = [[1, [ls_[i]]] for i in range(len(ls_))]
        # print(dp)

        for i in range(len(ls_) - 2, -1, -1):
            next_idx = self.get_next_meeting_idx(ls_, i)
            if next_idx != -1:
                # jy: 如果参加当前会议, 加上从下一个可参加的会议开始的后续能参加的会议数更大, 则
                #     参加当前会议, 更新 dp[i][0] 和 dp[i][1] 的值为包含当前会议信息的值;
                if dp[next_idx][0] + dp[i][0] > dp[i+1][0]:
                    dp[i][0] = dp[next_idx][0] + dp[i][0]
                    dp[i][1] += dp[next_idx][1]
                # jy: 如果不参加当前会议, 从当前会议的下一个会议开始的后续能参加的会议数更大, 则更
                #     新 dp[i][0] 和 dp[i][1] 的信息为 dp[i+1][0] 和 dp[i+1][1]
                else:
                    dp[i][0] = dp[i+1][0]
                    dp[i][1] = dp[i+1][1]
        return dp[0]


ls_ = [[3, 6], [1, 4], [5, 7], [2, 5], [5, 9], [3, 8], [8, 11], [6, 10], [8, 12], [12, 14]]
# outPut: 4, 如选择: [[1, 4], [5, 7], [8, 11], [12, 14]] (不唯一)
res = Solution().schedule_maximun_meeting_v1(ls_)
print(res)
res = Solution().schedule_maximun_meeting_v2(ls_)
print(res)

print("-" * 66)

ls_ = [[1, 2], [2, 3], [3, 4], [1, 2]]
# Output: 3
res = Solution().schedule_maximun_meeting_v1(ls_)
print(res)
res = Solution().schedule_maximun_meeting_v2(ls_)
print(res)

print("-" * 66)

ls_ = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
# Output: 4
res = Solution().schedule_maximun_meeting_v1(ls_)
print(res)
res = Solution().schedule_maximun_meeting_v2(ls_)
print(res)

print("-" * 66)

ls_ = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]
# Output: 2
res = Solution().schedule_maximun_meeting_v1(ls_)
print(res)
res = Solution().schedule_maximun_meeting_v2(ls_)
print(res)

