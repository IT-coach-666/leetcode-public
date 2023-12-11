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
title_jy = "Palindrome-Permutation-II(array_dim_1)"
# jy: 记录不同解法思路的关键词
tag_jy = ""


"""
Given a string s, return all the palindromic permutations (without duplicates) of it.
Return an empty list if no palindromic permutation could be form.


Example 1:
Input: "aabb"
Output: ["abba", "baab"]

Example 2:
Input: "abc"
Output: []
"""



from typing import List
import itertools


class Solution:
    """
解法1: 在 266_Palindrome-Permutation.py 的基础上进行字符组合;

进行回文组合时只需要考虑回文的前半部分, 后半部分等于反转前半部分, 如果回
文数是奇数, 则需要额外添加该奇数到回文的中间位置;

定义 counts 记录各字符的数量, used_counts 记录各字符被使用的次数;
定义 generate 方法根据 counts 生成字符串组合, 遍历 counts, 如果当前字符
在 used_counts 中的数量达到了 counts 中数量的一半, 说明该字符已用尽, 则跳
过该字符, 否则 used_counts 中对应数量加 1, 同时递归调用 generate 生成除当
前字符外的字符串组合, 递归调用完成后将 used_counts 中对应字符数量减 1 进
行回溯;
    """
    def generatePalindromes_v1(self, s: str) -> List[str]:
        chars = set()
        counts = {}
        used_counts = {}

        for c in s:
            # jy: 如果字符 c 在集合中, 则去除; 如果不在, 则加入; 因此
            #    出现偶数次的字符最终都不会在集合 chars 中;
            if c in chars:
                chars.remove(c)
            else:
                chars.add(c)
            # jy: counts 记录各字符的数量; used_counts 记录各字符被使用的次数;
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
                used_counts[c] = 0
        # jy: 如果集合中最后剩余的字符多于 1 个, 表示该字符串无法组成回文, 直接返回 [];
        if len(chars) > 1:
            return []
        # jy: 以下等同于: middle = chars.pop()
        middle = next(iter(chars)) if len(chars) == 1 else ''
        # jy: 调用 _generate_v1 方法, 生成回文字符串中去除 middle 字符后的前半子串;
        # print(counts, used_counts)
        permutations = self._generate_v1(counts, used_counts)
        # print("=========permutations: ", permutations)
        if permutations:
            return [permutation + middle + permutation[::-1] for permutation in permutations]
        else:
            return [middle] if middle else []

    """
jy: 以最初传入的 counts 和 used_counts 如下为例进行分析:
counts:      {'a': 2, 'b': 2}
used_counts: {'a': 0, 'b': 0}

即该方法有两轮 for 循环(不考虑递归调用时的 for 循环),  每有效循环一轮, 得到一个目标排列组
合, 如(可在以下 for 循环的最后加 break 语句查看第一个(注意是第一个)构造出的 permutations):
第一轮循环先遍历 'a', 结束后(含子递归调用), 得到的 permutations 为 ['ab'] (实际个数根据字符
串的复杂程度而定, 如果字符串较复杂, 返回的组合可能有多个, 但每一轮最外层循环的返回结果中的
组合排列均以最外层循环遍历的字符开头)
    """
    def _generate_v1(self, counts, used_counts):
        """根据 counts 中所有字符的一半个数生成字符串组合"""
        # jy: 用于存放所有回文字符串的前半子串组合;
        permutations = []

        # jy: 循环遍历 counts 中的所有字符 key, 使用其中的所有字符的一半进行组合构建;
        for key, count in counts.items():
            # jy: 如果当前字符在 used_counts 中的数量达到了 counts 中数量的一半, 说明该
            #    数已用尽, 跳过该字符; 如果该字符出现奇数次, 则只会使用该字符 (count // 2) 次;
            #    例如出现一次的字符不会被使用, 出现 3 次则只会使用 1 次(构建回文前半子串
            #    只需使用总出现次数的一半即可);
            if count // 2 == used_counts[key]:
                continue

            print("============== key: ", key, "===========count: ", count)
            # jy: 将字符 key 的使用次数加 1(表明当前被使用 1 次), 随后在此基础上递归调用 _generate_v1
            used_counts[key] += 1
            # jy: 当 counts 中所有字符都已被使用其出现次数的一半后, rest_permutations 得到的是空列表;
            rest_permutations = self._generate_v1(counts, used_counts)
            print("=================rest_permutations: ", rest_permutations)

            # jy: 如果 rest_permutations 返回的是空列表, 表明当前使用 key 字符后, counts 中的所有字符
            #    就已经都被用完了(即用了一半了); 此时的 permutations
            if not rest_permutations:
                # jy: 注意此处不是为最终 permutations 的结果服务的(因为往往最终结果的排列组合不仅仅只有
                #    一个字符), 而是为子递归调用服务, 子递归调用中会将 permutations 的结果返回赋值给
                #    rest_permutations 变量, 随后该变量再结合 key 拼接为新的 permutations 结果(如果仍
                #    然是属于子递归中的 permutations, 依旧会返回赋值为 rest_permutations, 直到为最外
                #    层调用时, permutations 即为目标排列组合);
                permutations += [key]
                # pass
            else:
                print("=================permutations[before]: ", permutations)
                # jy: 以下 key 的位置随意放均可, 放在前则表示 permutations 的结果以当前循环的有效字
                #    符 key 开头, 放在后则表示以该当前循环的有效字符结尾;
                permutations += [key + permutation for permutation in rest_permutations]
                # permutations += [permutation + key for permutation in rest_permutations]
            print("=================permutations: ", permutations)
            # jy: 递归调用完成后将 used_counts 中对应的 key 字符数量减 1 进行回溯;
            used_counts[key] -= 1
            # break  # jy: 查看第一个的 permutations 结果时, 添加该语句;

        return permutations


    """
解法2: 在解法1(构造回文的顺序是从左往右构造一半回文)的基础上进行了优化:
1) 从中间开始向两边扩散构造整个回文, 省略了单独判断回文是奇数的步骤;
2) 省略了 used_counts 变量, 使用 counts 时每次减 2, 回溯时 counts 加 2;
    """
    def generatePalindromes_v2(self, s: str) -> List[str]:
        chars = set()
        counts = {}

        for c in s:
            if c in chars:
                chars.remove(c)
            else:
                chars.add(c)
            # jy: 统计字符出现的次数;
            counts[c] = counts.get(c, 0) + 1
        # jy: 如果无法构造回文, 则返回空列表;
        if len(chars) > 1:
            return []
        # jy: 获取回文的最中间字符; 以下等同于: middle = chars.pop()
        middle = next(iter(chars)) if len(chars) == 1 else ''

        return self._generate_v2(counts, middle, len(s))


    def _generate_v2(self, counts, permutation_so_far, target_length):
        # jy: 如果当前的排列长度等于目标回文长度, 则以列表形式返回该排列;
        if len(permutation_so_far) == target_length:
            return [permutation_so_far]

        permutations = []

        for key in counts:
            # jy: 如果字符的出现次数小于等于 1, 表明该字符不能再被使用;
            if counts[key] <= 1:
                continue

            # jy: 先将字符的个数减 2, 然后在当前的排列左右两边加上该字符
            counts[key] -= 2
            permutations += self._generate_v2(counts, key + permutation_so_far + key, target_length)
            # jy: 将该字符的个数加 2, 回溯, 不影响与当前循环平级的下轮循环;
            counts[key] += 2

        return permutations

    """
jy: 定义 counts 记录各字符的数量, 如果能组成回文, 则将遍历 counts 中的字符, 获取所有字符的半数字符构成
一个列表(出现 count 次的字符获取 count // 2 个该字符), 依据该列表中的字符求其所能组成的组合 permutations,
最后依据该组合中的元素进行回文构建:
return [permutation + middle + permutation[::-1] for permutation in permutations]
    """
    def generatePalindromes_jy(self, s: str) -> List[str]:
        chars = set()
        counts = {}

        for c in s:
            # jy: 如果字符 c 在集合中, 则去除; 如果不在, 则加入; 因此
            #    出现偶数次的字符最终都不会在集合 chars 中;
            if c in chars:
                chars.remove(c)
            else:
                chars.add(c)
            # jy: counts 记录各字符的数量; used_counts 记录各字符被使用的次数;
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        # jy: 如果集合中最后剩余的字符多于 1 个, 表示该字符串无法组成回文, 直接返回 [];
        if len(chars) > 1:
            return []

        half_str = ""
        for key, count in counts.items():
            half_str += key * (count // 2)
        # print("=============== half_str: ", half_str)
        # jy: 以下等同于: middle = chars.pop()
        middle = next(iter(chars)) if len(chars) == 1 else ''

        # jy: 排列后去重(不能直接组合, 因为如 "ab" 组合的话只有一个结果)
        permutations = ["".join(list(i)) for i in itertools.permutations(half_str)]
        permutations = [i for i in set(permutations)]
        # jy: 或调用含重复字符的不重复全排列函数:
        permutations = ["".join(i) for i in self.permuteUnique(list(half_str))]

        return [permutation + middle + permutation[::-1] for permutation in permutations]

    def permuteUnique(self, ls_str):
        """
        对字符列表中的字符进行排列组合(不重复)
        """
        res = []
        # jy: 先将列表进行排序, 让重复字符相邻;
        ls_str.sort()
        # jy: vt 列表, 用于判断该字符是否有相同并且已经处理过, 为真则跳过, 否则继续进入递归
        vt = [0] * len(ls_str)
        val = []

        def pu(res, ls_, val, vt):
            # jy: 如果 val 的长度等于目标长度, 则加入 res 中;
            if len(val) == len(ls_):
                res.append(val)
            # jy: 遍历列表中的字符;
            for i in range(0, len(ls_)):
                # jy: 如果该字符与前一个字符相同, 且前一个字符未被使用, 则跳过;
                if i > 0 and ls_[i] == ls_[i-1] and vt[i-1] == 0:
                    continue
                # jy: 如果当前字符未被使用, 则使用该字符进行递归, 随后将该字符设置为未使用状态(回溯);
                if vt[i] == 0:
                    vt[i] =1
                    pu(res, ls_, val + [ls_[i]], vt)
                    vt[i] = 0
        # jy: 调用 pu 方法
        pu(res, ls_str, val, vt)
        return res


s = "aabb"
# s = "aabbaaccc"
# Output: ["abba", "baab"]
res = Solution().generatePalindromes_v1(s)
print(res)


res = Solution().generatePalindromes_jy(s)
print("========= jy-res: ", res)

s = "abc"
# Output: []
res = Solution().generatePalindromes_v2(s)
print(res)


print(Solution().permuteUnique(["1","3","1"]))


