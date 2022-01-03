# -*- coding: utf-8 -*-
# -------------------------------------------------
# @Project  :sicp_exercise
# @File     :exercise1_17
# @Date     :2022-01-02 13:48
# @Author   : Liu
# @Software :PyCharm
# -------------------------------------------------


def multi(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return 0
    else:
        return a + multi(a, b - 1)


def fast_multi(a, b):
    """
    calculate the product of a,b, and the steps required is logn
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return 0

    if b % 2 == 0:
        return fast_multi(a + a, b // 2)
    else:
        return a + fast_multi(a, b - 1)


def fast_multi_iter(a, b, c):
    """
    the method up is recursive, this method is iterative
    :param a:
    :param b:
    :param c:
    :return:
    """
    if b == 0:
        return c
    elif b % 2 == 0:
        return fast_multi_iter(a + a, b // 2, c)
    else:
        return fast_multi_iter(a, b - 1, a + c)


if __name__ == '__main__':
    print(multi(2, 1))
    print(fast_multi(2, 1))
    print(fast_multi_iter(2, 1, 0))

