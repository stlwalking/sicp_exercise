# -*- coding: utf-8 -*-
# -------------------------------------------------
# @Project  :sicp_exercise
# @File     :exercise1_16
# @Date     :2022-01-02 11:22
# @Author   : Liu
# @Software :PyCharm
# -------------------------------------------------


def fast_expt(b: int, n: int):
    """
    使用迭代的计算过程求b的n次幂, 要求 logn
    :param b:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    elif n % 2 == 1:
        return b * fast_expt(b, n - 1)
    else:
        return fast_expt(b * b, n // 2)


def fast_expt_ans(b: int, n: int):
    """
    迭代计算 b ** n, 要求logn
    :param b:
    :param n:
    :return:
    """
    return expt_iter(b, n, 1)


def expt_iter(b, n, a):
    """
    :param b:
    :param n:
    :param a:
    :return:
    """
    if n == 0:
        return a
    elif n % 2 == 0:
        return expt_iter(b * b, n // 2, a)
    else:
        return expt_iter(b, n - 1, b * a)


if __name__ == '__main__':
    print(fast_expt(3, 3))
    print(fast_expt_ans(3, 3))
