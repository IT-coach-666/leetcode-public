import random


def is_sort_algorithm_correct(len_ls, fun_sort_algorithm):
    """
    验证排序函数是否正确; 验证逻辑: 生成 range(0, len_ls) 并
    shuffle 且使用正确排序算法排序后比对

    len_ls: 列表长度
    fun_sort_algorithm: 实现排序功能的函数 
    """
    # jy: 生成数值为 0 到 len_ls - 1 的有序列表
    #     随后 shuffle (打乱顺序)
    ls_to_be_sort = list(range(len_ls))
    random.shuffle(ls_to_be_sort)

    # jy: 再次生成同样的有序列表, 用于后续的对比判断
    ls_object = list(range(len_ls))

    # jy: 执行排序函数, 对打乱的列表进行排序
    tmp = fun_sort_algorithm(ls_to_be_sort)
    # jy: 如果有返回值(即返回列表), 则判断与原有序列表是否相等
    if tmp:
        return tmp == ls_object
    return ls_to_be_sort == ls_object




