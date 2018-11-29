# -*- coding:utf-8 -*-

"""
   Pair RDD action 操作
"""
from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("pairrdd action")
    .set("spark.executor.memory", "2g")
)

sc = SparkContext(conf=conf)

alist = [(1, 2), (2, 4), (3, 6), (1, 4), (2, 3), (1, 3)]

rdd = sc.parallelize(alist, 3)

# 对每个键对应的元素分别计数
rdd.countByKey() # [(1, 3), (2, 2), (3, 1)]

# 将结果以映射表的形式返回，以便查询
rdd.collectAsMap() # {1: 3, 2: 3, 3: 6}

# 返回给定键对应的所有值
rdd.lookup(1) # [2, 4, 3]

