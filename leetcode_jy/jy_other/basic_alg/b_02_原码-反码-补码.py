
"""
正数: 直接用原码表示，如 5 在计算机中的表示为: 0000 0101
负数: 补码(即除符号位外的每一位取反(即正数的反码)基础上加 1)形式表示, 如单 -5 在计算机中表示为: 1111 1011


原码: 即该数的正常二进制表示(最高位为符号位, 0 表示正, 1 表示负), 如:
00000000 00000000 00000000 00000101 是 5 的原码
10000000 00000000 00000000 00000101 是 -5 的原码


反码:
正数: 反码与原码相同
负数: 反码为原码除符号位外各位取反
5 的反码为:   00000000 00000000 00000000 00000101
-5 的反码为: 11111111 11111111 11111111 11111010  (原码除符号位外的每一位均取反)


补码(计算机中负数就是以补码形式表示):
正数: 补码与原码相同
负数: 补码为反码(原码除符号位外的每一位均取反)的最后一位加 1
以 -5 为例:
原码: 10000000 00000000 00000000 00000101
反码: 11111111 11111111 11111111 11111010
补码: 11111111 11111111 11111111 11111011   (对应的十六进制即为: 0xFFFFFFFB)

-1 在计算机中的表示(补码表示):
原码: 10000000 00000000 00000000 00000001
反码: 11111111 11111111 11111111 11111110 (原码基础上除符号位外的每一位均取反)
补码: 11111111 11111111 11111111 11111111 (对应的 16 进制即为: 0xFFFFFF)

因此, 有如下等式始终成立(无论 x 是正整数、负整数还是 0):
当 x 为 0 时: x 取反对应的数值为 -1, 等式两边相等
当 x 为正整数时, x 取反后加 1 即为 -x (负数) 在计算机中的表示法
当 x 为负整数时, x 取反即为补码取反, 补码取反后加 1 即为该数的原码的形式(不含符号位)
-x = ~x + 1
"""


print("python 中 int 内置函数是依据数值的二进制原码进行转换，而负数通常以原码的补码方式表示 ==========")
print("如果负数")
# jy: 以下是 -5 的二进制表示, 但 python 转换为 int 时是不识别最高位为 1 时代
#     表负数的, 以下转换的结果为 2147483653
print(int("10000000000000000000000000000101", 2))
# jy: 当最高位为 1 时(代表负数), 此时的实际数值应该是 2^31 (即最高位为 1, 其余位
#     为 0 所代表的数值) 减去该值实际转换的结果; 由于最高位为 1 代表负值, 此时相
#     减的结果即为减去最高位, 且得到的值也正好是负数;
print((1 << 31) - int("10000000000000000000000000000101", 2))


'''
如下等式始终成立(无论 x 是正整数、负整数还是 0):
当 x 为 0 时: x 取反对应的数值为 -1, 等式两边相等
当 x 为正整数时, x 取反后加 1 即为 -x (负数) 在计算机中的表示法
当 x 为负整数时, x 取反即为补码取反, 补码取反后加 1 即为该数的原码的形式(不含符号位) 
'''
x = -0
print(-x == ~x + 1)
print(-x - 1 == ~x)
print(~0)  # -1
