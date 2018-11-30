# -*- coding:utf-8 -*-

from pyspark import SparkConf, SparkContext

conf = (SparkConf()
    .setMaster('local')
    .setAppName("rdd transform")
    .set("spark.executor.memory", "2g")
)
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4], 2)
print sorted(rdd.glom().collect()) # [[1, 2], [3, 4]]
