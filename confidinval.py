# -*- coding: utf-8 -*-
import numpy as np


def confd():
    # 假设我们已知喜欢足球的比例
    love_soccer_prop = 0.65  # Real percentage of people who love soccer
    # 全部的人口
    total_population = 10**7  # Total population in the U.S. (325M)
    #  喜欢的人数
    num_people_love_soccer = int(total_population * love_soccer_prop)
    #  不喜欢的人数
    num_people_dont_love_soccer = int(total_population * (1 - love_soccer_prop))
    # 喜欢的人群，通过元素全为1的数组表示
    people_love_soccer = np.ones(num_people_love_soccer)
    # 不喜欢的人群，通过元素全为0的数组表示
    people_dont_love_soccer = np.zeros(num_people_dont_love_soccer)
    # 通过hstack合为一个数组
    all_people = np.hstack([people_love_soccer, people_dont_love_soccer])
    # 计算平均值，因为喜欢的都是为1，不喜欢的为0，除以总数，得到平均值，
    # 和之前的比例相同
    print np.mean(all_people)

    # 随机选出1000个人，实验10组
    for i in range(10):
        sample = np.random.choice(all_people, 1000)
        # print 'Sample', i , ':', np.mean(sample)
    # 结果是在0.65左右

    # 如果选择更多组，计算每组平均值的平均值
    values = []
    for i in range(1000):
        sample = np.random.choice(all_people, size=1000)
        mean = np.mean(sample)
        values.append(mean)
    print np.mean(values)
    # 取了1000组的样本，检查每个样本组中热爱足球的人的百分比，然后对于
    # 这些值计算平均，得到的平均值很接近0.65


if __name__ == '__main__':
    confd()