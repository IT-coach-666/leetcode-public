
"""
微软初面: 给定一个数值 c, 求满足 a^2 + b^2 = c 的所有 (a, b) 组合(要求不重复)
"""

import math


def _sqrt_upper(x):
    """
    对正整数 x 开根号, 并对开根号结果向上取整;
    """
    low, high = 0, x
    while low < high:
        middle = low + (high - low) // 2
        square_middle = middle ** 2
        if square_middle > x:
            high = middle
        elif square_middle < x:
            low = middle + 1
        else:
            return middle
    return low


for i in range(1000):
    assert math.ceil(math.sqrt(i)) == _sqrt_upper(i)
print("_sqrt(i) is correctly coded")


def find_ab_v1(c):
    result = []

    # jy: 先对 c 进行开根号, 并对开根号的结果进行向上取整 (不使用 math 包, 通过二分
    #     查找实现; 二分查找比逐一循环遍历查找更高效);
    # x = math.ceil(math.sqrt(c))
    x = _sqrt_upper(c)

    # jy: a 和 b 的结果只可能是在 [0, x] 范围, 假设较小值为 a, 较大值为 b; 将 a 从 0 到 x
    #     之间不断循环尝试;
    for a in range(x + 1):
        square_b = c - a ** 2
        # jy: b 从 a 到 _sqrt(square_b) 中尝试(因为 b 不可能大于 _sqrt(square_b)), 且可以
        #     做如下优化: 当 a 大于 _sqrt(square_b) 时, 可以直接退出外层 for 循环(因为 a
        #     是小于或等于 b 的);
        b = _sqrt_upper(square_b)
        if a > b:
            break
        if b ** 2 == square_b:
            result.append([a, b])
    return result


def find_ab_v2(c):
    result = []

    # jy: a^2 和 b^2 的范围肯定是有一个小于或等于 c/2, 有一个大于或等于 c/2; 为了避免重复计
    #     算, 假设 a 是较小值, b 是较大值(a 和 b 顶多相等);
    x = _sqrt_upper(c // 2)
    if x ** 2 == c // 2:
        x += 1

    # jy: a 属于较小的那个值, 则以下的 square_b 肯定是对应较大 b 值的 平方; 不再需要判断 b 和 a
    #     的大小;
    # for a in range(x + 1):
    for a in range(x):
        square_b = c - a ** 2
        # jy: b 从 a 到 _sqrt(square_b) 中尝试(因为 b 不可能大于 _sqrt(square_b)), 且可以
        #     做如下优化: 当 a 大于 _sqrt(square_b) 时, 可以直接退出外层 for 循环(因为 a
        #     是小于或等于 b 的);
        b = _sqrt_upper(square_b)
        if b ** 2 == square_b:
            result.append([a, b])
    return result


"""
对解法 3 进行优化;
"""
def find_ab_v3(c):
    dict_ = {}

    # jy: a 从 0 开始, 将 {a^2: a} 的值存入字典, 假设 a 是较小的那个值, 则
    #     a^2 <= c // 2;
    a = 0
    while True:
        square_a = a ** 2
        if square_a > c // 2:
            break
        dict_[square_a] = a
        a += 1
    res = []

    # jy: 经过以上 while 循环, a-1 及其之前的数值的平方都将被记录到字典中(a 最终是被更新为其平
    #     方大于 c//2 的值), 如果 a-1 的平方等于 c // 2, 则可以确定如果存在符合条件的 b, 其平方
    #     也必定等于 c // 2 因此此时的 b 要从 a-1 开始计算起; 否则 b 可以直接从 a 算起; 通过该方
    #     式, 确保了当 a 方取最大值 c//2 时, b 方也能取到 c // 2
    b = a - 1 if (a - 1) ** 2 == c // 2 else a

    while True:
        square_b = b * b
        if square_b > c:
            break
        if c - square_b in dict_:
            res.append([dict_[c - square_b], b])
        b += 1
    return res


for i in range(1000):
    # print("-" * 66, i)
    res1 = find_ab_v1(i)
    res2 = find_ab_v2(i)
    res3 = find_ab_v3(i)
    assert res1 == res2
    # print("res1: ", res1, "res2: ", res2)
    if len(res1) != len(res2):
        print("-" * 66, i)
        print("res1: ", res1, "res2: ", res2)
