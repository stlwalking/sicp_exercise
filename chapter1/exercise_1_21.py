# -*- coding: utf-8 -*-
# -------------------------------------------------
# @Project  :sicp_exercise
# @File     :exercise_1_21
# @Date     :2022-01-03 11:49
# @Author   : Liu
# @Software :PyCharm
# -------------------------------------------------


def smallest_divisor(n):
    """
    find the smallest divisor of n
    :param n:
    :return:
    """
    return find_divisor(n, 2)


def find_divisor(n, test_divisor):
    """
    :param n:
    :param test_divisor:
    :return:
    """
    def _next():
        # exercise 1_23
        if test_divisor == 2:
            return 3
        return test_divisor + 2

    if test_divisor * test_divisor > n:
        return n
    elif n % test_divisor == 0:
        return test_divisor
    else:

        return find_divisor(n, _next())


if __name__ == '__main__':
    print(smallest_divisor(3))
    print(smallest_divisor(199))
    print(smallest_divisor(1999))
    print(smallest_divisor(19999))


