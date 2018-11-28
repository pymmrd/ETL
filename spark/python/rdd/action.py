# -*- coding:utf-8 -*-

"""
rdd action操作API
"""

from pyspark import SparkConf, SparkContext
from operator import add

conf = (SparkConf()
    .setMaster('local')
    .setAppName("rdd action transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

alist = [1, 2, 3, 3]

rdd = sc.parallelize(alist)

# 返回RDD中的所有元素
rdd.collect() # [1, 2, 3,3]

# 返回RDD中元素的个数
rdd.count() # 4

# 各元素在RDD中出现的次数
rdd.countByValue() #  defaultdict(<type 'int'>, {1: 1, 2: 1, 3: 2})
# 从RDD中返回num个元素
rdd.take(2) # [1, 2]

# 从RDD中按照提供的顺序返回最前面的num个数字
rdd.takeOrdered(2, key=lambda x: -x) # [3, 3]

# 从RDD中返回最前面的num个元素
rdd.top(2) # [3, 3]

# 从RDD中返回任意一个元素
rdd.takeSample(false, 1) # 非确定

# 并行整合RDD中所有数据
rdd.reduce(add) # 9
rdd.fold(0, add) # 9

# 和reduce相似，但是通常返回不同类型
rdd.aggregate(
    (0, 0),
    lambda x, y: (x[0] + y, x[1] + 1),
    lambda acc1, acc2: (acc1[0]+acc2[0], acc1[1]+acc2[1])
) # (9, 4)

# 对RDD中的每个元素使用给定的函数
rdd.foreach(print)
