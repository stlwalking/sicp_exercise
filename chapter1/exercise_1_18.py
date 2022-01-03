# -*- coding: utf-8 -*-
# -------------------------------------------------
# @Project  :sicp_exercise
# @File     :exercise_1_18.py
# @Date     :2022-01-03 10:13
# @Author   : Liu
# @Software :PyCharm
# -------------------------------------------------


def multi(a, b, accumulator):
    """
    :param a:
    :param b:
    :param accumulator:
    :return:
    """
    if b == 0:
        return accumulator
    elif b % 2 == 0:
        return multi(a + a, b // 2, accumulator)
    else:
        return multi(a, b - 1, a + accumulator)


if __name__ == '__main__':
    print(multi(3, 5, 0))
    print(multi(2, 4, 0))
