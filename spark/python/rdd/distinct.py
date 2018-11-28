
# -*- coding:utf-8 -*-

"""
distinct去重
distinct() 操作的开销很大,因为它需要将所有数据通过网络进行
混洗(shuffle),以确保每个元素都只有一份
"""

from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("dictinct transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

rdd = sc.parallelize([[1, 2, 3, 3])
distinctRDD = rdd.distinct().collect()
print distinctRDD
