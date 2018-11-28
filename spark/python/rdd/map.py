# -*- coding:utf-8 -*-

"""
map函数，将函数应用于RDD中的每个元素,将返回值构成新的RDD
"""


from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("map transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
squared = rdd.map(lambda x: x * x).collect()
for num in squared:
    print "%i"  % num


