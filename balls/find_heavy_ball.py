# -*- coding: utf-8 -*-
import logging
import math

# 8 小球问题 https://mp.weixin.qq.com/s/4HE50AGq9ERhlHp9-pZv-w

def log(msg):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.info(msg)


class Ball(object):

    @classmethod
    def get_heavy_ball(cls, array_list):
        log("--------------------")
        length = len(array_list)
        log("length is %d" % length)
        if length == 1:
            log("heaviest one is : %s" % array_list[0])
            return
        # 获取 n, 其中 3^n <= length
        n = cls.get_pow(length)
        # 3^n 对比 3^n
        value = int(math.pow(3, n))
        log("value is %d" % value)
        sum_1 = 0
        sum_2 = 0
        sum_1_array = array_list[0 : value]
        sum_2_array = array_list[value : value*2]
        for i in sum_1_array:
            sum_1 += i
        for i in sum_2_array:
            sum_2 += i

        if sum_1 == sum_2:
            # 将剩余的球继续称重
            cls.get_heavy_ball(array_list[value*2 : length])
        elif length > 3:
            if sum_1 > sum_2:
                # 将 sum_1 继续称重
                log("sum_1 : %s" % sum_1_array)
                cls.get_heavy_ball(sum_1_array)
            else:
                # 将 sum_2 继续称重
                log("sum_2 : %s" % sum_2_array)
                cls.get_heavy_ball(sum_2_array)
        else:
            if sum_1 > sum_2:
                log("heaviest one is : %s" % sum_1_array)
            else:
                log("heaviest one is : %s" % sum_2_array)

    @classmethod
    def get_pow(cls, num):
        n = 0
        while (math.pow(3, n) < num):
            n += 1
        log("n is %d" % (n - 1))
        return (n - 1)


if __name__ == "__main__":
    # array_list = [2, 2, 3]
    # array_list = [2, 3, 2]
    # array_list = [2, 2, 2, 2, 3, 2, 2, 2]
    array_list = [2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    Ball.get_heavy_ball(array_list)
