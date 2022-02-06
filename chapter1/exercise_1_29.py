# -*- coding: utf-8 -*-
# -------------------------------------------------
# @Project  :sicp_exercise
# @File     :exercise_1_29
# @Date     :2022-02-06 14:46
# @Author   : Liu
# @Software :PyCharm
# -------------------------------------------------


import math


# translate demo from lisp to python


def cube(x):
    return math.pow(x, 3)


def normal_sum(func, a, next_func, b):
    """
    更一般形式的求和，求和的模版方法
    :param func:
    :param a:
    :param next_func:
    :param b:
    :return:
    """
    if a > b:
        return 0
    return func(a) + normal_sum(func, next_func(a), next_func, b)


def cube_sum(a, b):
    """
    求 a 到 b 的 立方和
    :param a:
    :param b:
    :return:
    """
    def inc(n):
        return n + 1

    return normal_sum(cube, a, inc, b)


def sum_integers(a, b):
    """
    求 a 到 b 的整数和
    :param a:
    :param b:
    :return:
    """
    def identity(x):
        return int(x)

    def inc(n):
        return n + 1

    return normal_sum(identity, a, inc, b)


def pi_sum(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    def pi_func(x):
        return 1 / (x * (x + 2))

    def pi_next(x):
        return x + 4

    return normal_sum(pi_func, a, pi_next, b)


def integral(f, a, b, dx):
    """
    定积分
    :param f:
    :param a:
    :param b:
    :param dx:
    :return:
    """
    def add_dx(x):
        return x + dx

    return normal_sum(f, a + dx / 2, add_dx, b) * dx


# 练习
def simpson(f, a, b, n):
    """
    辛普森规则求定积分
    :param f:
    :param a:
    :param b:
    :param n:
    :return:
    """
    def h():
        return (b - a) / n

    def factor(k):
        if k == 0 or k == n:
            return 1
        elif k % 2 == 0:
            return 2
        else:
            return 4

    def next_(x):
        return x + 1

    def func(c):
        return factor(c) * f(a + c * h())

    return normal_sum(func, a, next_, n) * h() / 3


if __name__ == '__main__':
    # print("cube sum :", cube_sum(1, 100))
    # print("integer sum: ", sum_integers(1, 10))
    # print("pi sum: ", pi_sum(1, 1000) * 8)
    print("integral sum: ", integral(cube, 0, 1, 0.01))
    print("simpson sum: ", simpson(cube, 0, 1, 100))