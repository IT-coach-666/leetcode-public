
"""
异或运算

认识异或运算: 相同为 0, 不同为 1 ( 0 ^ 1 = 1, 0 ^ 0 = 0, 1 ^ 1 = 0)
异或运算满足交换律
相同数值异或运算结果为 0
0 与任何数值的异或运算均为数值本身

1) 不引入临时变量交换两数值:
a = 甲
b = 乙
a = a ^ b （即 a = 甲 ^ 乙）
b = a ^ b （即 b = 甲 ^ 乙 ^ 乙 = 甲）
a = a ^ b （即 a = 甲 ^ 乙 ^ 甲 = 乙）

2) 一个数组中有一种数出现奇数次, 其它数均出现偶数次, 求出现奇数次的数
对所有数值进行异或运算即可

3) 提取整数类型的数中二进制最右侧的 1 :
num & (~num + 1)
   消掉整数类型的数的二进制最右侧的 1 :
num & (num - 1)
"""


def swap(a, b):
    """
    不引入临时变量交换两数值(只有当两数的内存地址不相同时才生效)
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# a = 10
# b = 20
# print(swap(a, b))
# a = [1, 2, 3]
# print(swap(a[0], a[1]), a)
# print(swap(a[0], a[0]), a)


def get_odd_num(arr):
    """
    一个数组中有一种数出现奇数次, 其它数均出现偶数次, 求出现奇数次的数
    """
    # jy: 对数组中的所有数值做异或运算, 结果即为出现奇数次的数
    eor = arr[0]
    for i in arr[1:]:
        eor ^= i
    return eor

# ls_ = [1, 2, 3, 1, 2, 3, 3]
# print(get_odd_num(ls_))


def get_rightest_one(num):
    """
    提取整数类型的数中二进制最右侧的 1
    """
    # jy: 取反(0 变 1, 1 变 0)加 1 后与原数值做与运算即可
    return num & (~num + 1)

# print(get_rightest_one(3))


def get_two_odd_num(arr):
    """
    数组中有两种数出现了奇数次，其它数都出现了偶数词，找出这两种数
    """
    # jy: 假设两种出现奇数次的数值分别是 a 和 b, 则 a ^ b != 0
    # jy: 对数组中的元素进行异或运算, 结果 eor 肯定不为 0(必然有一个位置上是 1);
    eor = arr[0]
    for num in arr[1:]:
        eor ^= num
    # jy: 提取 eor 的最右位的 1, 该最右位的 1 肯定是来自 a 或 b (a 或 b 中有且只有一个在该位置为 1,
    #     另一个在该位置为 0; arr 中的数值也分为两派, 一派是该位置为 1 的, 另一派是该位置为 0 的)
    rightOne = eor & (~eor + 1)
    rightOne_num = 0
    for i in arr:
        # jy: 找出数组中该位置为 1 的一派, 并对其进行异或运算, 由于其它数值均出现偶数次, 异或运算后
        #     结果为 0, 剩下出现奇数次的该位置为 1 的数值(假设是 a)
        if i & rightOne != 0:
            rightOne_num ^= i
    # jy: 经过以上方式找到 a 后, 再对 a 进行异或运算即可找到 b (eor 即为 a ^ b, 在以上找到 a 后, 再
    #     进行 a ^ eor, 即 a ^ a ^ b = b)
    return rightOne_num, eor ^ rightOne_num

# ls_ = [1, 2, 4, 1, 2, 4, 3, 4]
# print(get_two_odd_num(ls_))


def get_binary_one(num):
    """
    统计一个数值的二进制形式中有多少个 1
    """
    count = 0
    while num != 0:
        # jy: 提取二进制数值中最右侧的 1
        right_one = num & ((~num) + 1)
        count += 1
        num ^= right_one

    return count

# a = get_binary_one(7)
# print(a)

# print(0 ^ 1, 0 ^ 0, 1 ^ 1)






