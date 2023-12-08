
"""
01 背包问题
参考: 
https://www.cnblogs.com/mfrank/p/10533701.html
"""

from functools import lru_cache

class Solution:
    def __init__(self, obj_value_weight):
        """
        传入的 obj_value_weight 为一个字典, key 为某物品的价值, value 为装该物品的所需容量;
        """
        # jy: 为了方便处理, 将数组 ws 和 vs 都增加了一个补位数 0, 防止数组越界;
        #     同时, 使得第 i 个物品的价值和容量可直接使用 self.vs[i] 和 self.ws[i] 表示;
        self.vs = [0]
        self.ws = [0]
        for v, w in obj_value_weight.items():
            self.vs.append(v)
            self.ws.append(w)

        self.pseudo_dp = [[0 for _ in range(knapsack_capacity + 1)] for _ in range(len(self.vs))]
        self.memo = {}
        
    """
解法1: 递归求解;
    """
    def knapsack_01_v1(self, knapsack_capacity):
        # jy: 记录物品个数, 第 i 个物品的价值和重量分别为 self.vs[i] 和 self.ws[i];
        obj_num = len(self.vs) - 1
        return self._ks(obj_num, knapsack_capacity)

    def _ks(self, i, c):
        """
        计算背包容量为 c, 从第 1 个物品到第 i 个物品选择性装入时的最大价值;
        """
        result = 0
        # jy: 初始条件: 如果容量为 0, 或者已经没有待装物品了, 则最大价值为 0;
        if i == 0 or c == 0:
            result = 0
        # jy: 现有容量 c 装不下第 i 个物品( c < self.ws[i]), 则最大价值的装法只
        #     能从第 1 个物品到第 i-1 个物品中选择性装入, 容量仍为 c;
        elif self.ws[i] > c:
            result = self._ks(i-1, c)
        # jy: 现有容量 c 可以装下第 i 个物品( c >= self.ws[i]), 则可以选择装下
        #     第 i 个物品, 或不装第 i 个物品;
        else:
            # jy: 如果选择不装第 i 个物品, 则从第 1 个物品到第 i-1 个物品选择性
            #     装入, 此时背包容量仍为 c;
            tmp1 = self._ks(i-1, c)
            # jy: 如果选择装入第 i 个物品, 则能获取到第 i 个物品的价值 self.vs[i], 
            #     同时背包的容量减小 self.ws[i], 此时可以继续从第 1 个物品到第 i-1
            #     个物品中选择性装入, 此时的容量为 c - self.ws[i]
            tmp2 = self._ks(i-1, c - self.ws[i]) + self.vs[i]
            # jy: 在装与不装两种方案之间, 选择价值更大的方案(注意, 并不是装的方案最
            #     大化价值, 比如但第 i 个物品很占容量, 但价值又极低时, 装该物品只会
            #     占用容量, 对价值增加没多大帮助, 此时不装该物品, 留足容量装其它物品
            #     就显得更有利于最大化价值)
            result = max(tmp1, tmp2)
        return result


    """
解法2: 递归 + 缓存(减少不必要的重复计算); 

该方案仍不是真正意义上的动态规划; dp 的初始化没必要参照动态规划中
的 dp 初始化, 直接使用字典保存碰到的 (i, c) 即可, 更节省空间;

缓存还可直接使用 @lru_cache(None) 装饰器;
    """
    def knapsack_01_v2(self, knapsack_capacity):
        obj_num = len(self.vs) - 1
        # jy: 初始化均为 0;
        return self._ks2(obj_num, knapsack_capacity)


    # jy: 该装饰器用于替代递归方法中的缓存(二者保留其一即可)
    @lru_cache(None)  
    def _ks2(self, i, c):
        result = 0

        # jy: 在解法1 中的递归基础上增加判断, 如果 (i, c) 对应的组合已经被
        #     计算过, 则直接返回原先的计算结果即可(避免重复运算)
        #if self.pseudo_dp[i][c]:
        #    return self.pseudo_dp[i][c]
        if (i, c) in self.memo:
            return self.memo[(i, c)]
     
        if i == 0 or c == 0:
            result = 0
        elif self.ws[i] > c:
            result = self._ks2(i-1, c)
        else:
            tmp1 = self._ks2(i-1, c)
            tmp2 = self._ks2(i-1, c - self.ws[i]) + self.vs[i]
            result = max(tmp1, tmp2)

        #self.pseudo_dp[i][c] = result
        self.memo[(i, c)] = result
        return result

    """
解法3: 动态规划
    """
    def knapsack_01_v3(self, knapsack_capacity):
        # jy: 记 dp[j] 表示容量为 j 时选择性装物品取得的最大收益; 目标即求 dp[knapsack_capacity] 
        #     初始化均为 0, 表示当前未装入任何物品, 收益为 0; 长度为 knapsack_capacity + 1, 确保
        #     容量为 knapsack_capacity 的最大收益直接使用 dp[knapsack_capacity] 就可表示;
        dp = [0 for _ in range(knapsack_capacity + 1)]

        # jy: 逐个比遍历物品(由于 i 表示物品编号, 而结合 self.vs 和 self.ws 可知物品编号是从 1 开
        #     始的, 故可以直接从 1 开始遍历); 每一轮 i 循环完成后, 都会更新 dp 中所有容量对应的记
        #     录, 其中 dp[x] 表示从第 1 个物品到第 i 个物品中选择性放入容量为 x 的背包中, 最大的收
        #     益是多少; 当 i 遍历到最后为最大值时, dp[x] 即表示从第 1 个物品到最后一个物品选择性的
        #     放入容量为 x 的背包中, 最大的收益; 最终 dp[knapsack_capacity] 即为背包容量最大时的最
        #     大收益; 
        # jy: 每轮 i 循环, 都是在填写一张 n 行 capacity 列的二维表, 其中 dp 仅保留最后更新的行, 因
        #     为下一行的推导只需要上一行的结果就够了)
        for i in range(1, len(self.vs)):
        #for i in range(len(self.vs)):
            #"""
            # jy: 背包容量从后往前(从最大容量往 0)遍历, 
            for j in range(knapsack_capacity, 0, -1):
                # jy: 确保 j - self.ws[i] >= 0 时, dp[j - self.ws[i]] 才有含义;
                if j >= self.ws[i]:
                    # jy: dp[j] 表示容量为 j 时, 不装当前物品 i 时的最大收益;
                    #     dp[j - self.ws[i]] + self.vs[i] 表示容量为 j 时, 装当前物品 i 时的最大收益, 
                    #     其中 dp[j - self.ws[i]] 表示容量为 j - self.ws[i] 时所装物品的最大收益(截止
                    #     第 i-1 个物品)
                    dp[j] = max(dp[j], dp[j - self.ws[i]] + self.vs[i])
                else:
                    break
            #print(dp)
            '''
[0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
[0, 0, 2, 4, 4, 6, 6, 6, 6, 6, 6]
[0, 0, 2, 4, 4, 6, 6, 6, 7, 7, 9]
[0, 0, 2, 4, 4, 7, 7, 9, 11, 11, 13]
            '''
            #"""

            """
            # jy: 一下方法适用于一个物品可以多次放入背包的场景(即同类物品有任一多个);
            for j in range(1, knapsack_capacity + 1):
                if j >= self.ws[i]:
                    dp[j] = max(dp[j], dp[j - self.ws[i]] + self.vs[i])
            print(dp)
            '''
[0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10]
[0, 0, 2, 4, 4, 6, 8, 8, 10, 12, 12]
[0, 0, 2, 4, 4, 6, 8, 8, 10, 12, 12]
[0, 0, 2, 4, 4, 7, 8, 9, 11, 12, 14]
            '''
            """
            
        return dp[knapsack_capacity]



obj_value_weight = {
2:2, 
4:3, 
3:5, 
7:5}
knapsack_capacity = 10
#print(obj_value_weight)
res = Solution(obj_value_weight).knapsack_01_v1(knapsack_capacity)
print(res)

res = Solution(obj_value_weight).knapsack_01_v2(knapsack_capacity)
print(res)

res = Solution(obj_value_weight).knapsack_01_v3(knapsack_capacity)
print(res)


