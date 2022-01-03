# -*- coding: utf-8 -*-
# -------------------------------------------------
# @Project  :sicp_exercise
# @File     :exercise_1_27
# @Date     :2022-01-03 13:55
# @Author   : Liu
# @Software :PyCharm
# -------------------------------------------------
import random


def check_prime(n):
    """
    根据小费马定理
    检查n是否是素数
    :param n:
    :return:
    """
    if n < 3:
        return n

    # tmp value that < n
    # 否则，随机m次，只要都能等于tmp，为素数的概率较大
    for i in range(10000):
        tmp = random.randint(2, n-1)
        # fermat test, 如果n是一个素数，a为小于 n 的任意正整数，那么a ** n % n == a % n
        if tmp ** n % n != tmp:
            return -1

    return n


if __name__ == '__main__':
    # exercise 1_27, Carmichael number, 561, 1105, 1729
    print(check_prime(561), " = = = " * 5)
    print(check_prime(1105), " = = = " * 5)
