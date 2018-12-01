# -*- coding:utf-8 -*-

"""
数据rdd action操作API
count() RDD 中的元素个数
mean() 元素的平均值
sum() 总和
max() 最大值
min() 最小值
variance() 元素的方差
sampleVariance() 从采样中计算出的方差
stdev() 标准差
sampleStdev() 采样的标准差
"""

from pyspark import SparkConf, SparkContext
from operator import add

conf = (SparkConf()
    .setMaster('local')
    .setAppName("num rdd action transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

alist = [1, 2, 3, 4, 5, 6]

rdd = sc.parallelize(alist)
rdd.stats() # (count: 6, mean: 3.5, stdev: 1.70782512766, max: 6.0, min: 1.0)
rdd.sum() # 21

