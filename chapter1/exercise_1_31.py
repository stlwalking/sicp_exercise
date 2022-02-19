# -*- coding: utf-8 -*-
# -------------------------------------------------
# @Project  :sicp_exercise
# @File     :exercise_1_31
# @Date     :2022/2/19 上午11:52
# @Author   : Liu
# @Software :PyCharm
# -------------------------------------------------


def product(func, a, next_func, b):
    """
    the template to get the product from a to b
    iterative version
    :param func:
    :param a:
    :param next_func:
    :param b:
    :return:
    """
    if a > b:
        return 1
    return func(a) * product(func, next_func(a), next_func, b)


def prod(func, a, next_func, b):
    """
    the template to gain the product from a to b
    the recursive version
    :param func:
    :param a:
    :param next_func:
    :param b:
    :return:
    """
    def _iter(x, result):
        if x > b:
            return result
        return _iter(next_func(x), result * func(x))

    return _iter(a, 1)


def get_factorial(a, b):
    """
    :param a:
    :param b:
    :return:
    """

    def identical(x):
        return x

    def next_(x):
        return x + 1

    return product(identical, a, next_, b)


def get_factorial_recursive(a, b):
    """
    :param a:
    :param b:
    :return:
    """

    def identical(x):
        return x

    def next_(x):
        return x + 1

    return prod(identical, a, next_, b)


def calculate_pi(a, b):
    """
    :param a:
    :param b:
    :return:
    """
    def func(x):

        flag = True if x % 2 == 0 else False
        numerator = x + (2 if flag else 1)
        denominator = x + (1 if flag else 2)

        return numerator / denominator

    def next_func(x):

        return x + 1

    return prod(func, a, next_func, b) * 4


if __name__ == '__main__':
    # get factorial
    # print(get_factorial(1, 5))
    # print(get_factorial_recursive(1, 5))
    print(calculate_pi(1, 500))
