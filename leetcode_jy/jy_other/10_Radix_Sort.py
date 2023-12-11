
"""
基数排序, 本质上是一种多关键字的计数排序;
对于数值, 每一位的数字即代表一个关键字, 可以从低到高排(即以下实现逻辑), 或者从高到低(分治思想, 待定)
"""


def radix_sort(ls_):
    max_ = len(str(max(ls_)))
    division = 1
    res = [-1] * len(ls_)
    # jy: 每次循环都进行一次稳定的计数排序(先按个位数的数值进行奇数排序, 对排序的结果再
    #     按高位数的数值进行奇数排序); 即多关键字排序;
    for i in range(max_):
        count = [0] * 10

        for val in ls_:
            num = val // division % 10
            count[num] += 1

        for j in range(1, len(count)):
            count[j] = count[j] + count[j-1]

        # jy: 依据累加数组进行稳定的对应位置上的排序;
        for m in range(len(ls_)-1, -1, -1):
            num = ls_[m] // division % 10
            res[count[num]-1] = ls_[m]
            count[num] -= 1

        # jy: 注意, 此处不能直接 "ls_ = res", 需要深拷贝, 否则后续更新 res 的同时也更新 ls_;
        ls_ = [i for i in res]
        division *= 10
    return res


ls_ = [421, 240, 115, 532, 305, 430, 124]
res = radix_sort(ls_)
print(res)


