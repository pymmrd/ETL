# -*- coding:utf-8 -*-

"""
flatMap将函数应用于RDD中的每个元素，将返回的迭代器的所有内容
构成新的RDD。通常用来切分单词
"""

from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("flatMap transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

rdd = sc.parallelize([[1, 2, 3],[4, 5, 6]])
flatRDD = rdd.flatMap(lambda x: x).collect()
for num in flatRDD:
    print "%i"  % num


