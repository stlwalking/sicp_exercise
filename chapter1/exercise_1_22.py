# -*- coding: utf-8 -*-
# -------------------------------------------------
# @Project  :sicp_exercise
# @File     :exercise_1_22
# @Date     :2022-01-03 12:13
# @Author   : Liu
# @Software :PyCharm
# -------------------------------------------------
import random
import time


def timed_prime_test_(n):
    """
    根据小费马定理
    检查n是否是素数
    :param n:
    :return:
    """
    start = time.time_ns()
    if n < 3:
        print(" *** ", time.time_ns() - start)
        return n

    # tmp value that < n
    # 否则，随机m次，只要都能等于tmp，为素数的概率较大
    for i in range(5):
        tmp = random.randint(2, n-1)
        # fermat test, 如果n是一个素数，a为小于 n 的任意正整数，那么a ** n % n == a % n
        if tmp ** n % n != tmp:
            return -1

    print(" *** ", time.time_ns() - start)
    return n


def search_for_primes_(n):
    """
    查找n范围内的素数
    :param n:
    :return:
    """
    # 默认 n > 3

    res = [1, 2, 3]
    for i in range(3, n):
        if timed_prime_test(i) != -1:
            res.append(i)

    return res


################################# THE ANSWER #################################


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
    if test_divisor * test_divisor > n:
        return n
    elif n % test_divisor == 0:
        return test_divisor
    else:
        return find_divisor(n, test_divisor + 1)


def prime(n):
    """
    if n is prime
    :param n:
    :return:
    """
    return smallest_divisor(n) == n


def timed_prime_test(n):
    """

    :param n:
    :return:
    """
    return start_prime_test(n)


def start_prime_test(n):
    """
    :param n:
    :return:
    """
    start = time.time_ns()

    if prime(n):
        report_prime(n, time.time_ns() - start)


def report_prime(n, elapsed_time):
    """
    :param n:
    :param elapsed_time:
    :return:
    """
    print(" = = =  = = = = = ")
    print(n)
    print(" * * * ")
    print("time cost: ", elapsed_time)
    print(" = = =  = = = = = ")
    print(" ")


def search_for_prime(lower, upper):
    """
    :param lower:
    :param upper:
    :return:
    """
    def iter_(n):
        """
        :param n:
        :return:
        """
        while n <= upper:
            timed_prime_test(n)
            n += 2

    if lower % 2 == 1:
        iter_(lower)
    else:
        iter_(lower + 1)


if __name__ == '__main__':
    # print(timed_prime_test(10))
    # print(timed_prime_test(11))
    # print(timed_prime_test(111))
    # print(timed_prime_test(1111))

    print(search_for_prime(100000, 100200))


